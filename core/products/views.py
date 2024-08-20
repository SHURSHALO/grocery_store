from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseBadRequest,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.views import View

from typing import Any

from products.models import Category, Product, Shopping
from products.forms import ShoppingForm


class CategoryListView(ListView):
    """
    Представление для отображения списка категорий с пагинацией.
    """

    model = Category

    ordering = 'id'

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = self.object_list.prefetch_related('subcategories')
        context['categories'] = categories
        return context


class ProductListView(ListView):
    """
    Представление для отображения списка продуктов с пагинацией.
    """

    model = Product

    ordering = 'id'

    paginate_by = 5


class ShoppingListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка товаров в корзине пользователя с пагинацией.
    Пользователь должен быть аутентифицирован.
    """

    model = Shopping
    ordering = 'id'
    paginate_by = 5

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        """
        Обрабатывает запросы и проверяет права доступа пользователя к корзине.
        """
        if 'pk' in self.kwargs and request.user.id != self.kwargs.get('pk'):
            return HttpResponseForbidden(
                'You are not allowed to access this shopping cart.'
            )
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Возвращает список товаров в корзине, относящихся к текущему пользователю.
        """
        return Shopping.objects.filter(user=self.request.user).select_related(
            'product'
        )

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст данные о количестве и общей стоимости товаров в корзине.
        """
        context = super().get_context_data(**kwargs)
        cart_items = self.get_queryset()

        total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))[
            'total_quantity'
        ]

        total_price = cart_items.aggregate(
            total_price=Sum(F('quantity') * F('product__price'))
        )['total_price']

        context['total_quantity'] = total_quantity
        context['total_price'] = total_price
        return context


class ShoppingManageView(LoginRequiredMixin, View):
    """
    Представление для управления товарами в корзине (добавление, редактирование, удаление).
    Пользователь должен быть аутентифицирован.
    """

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы для отображения формы добавления/редактирования товара.
        """
        pk = kwargs.get('pk')
        if pk:
            shopping_item = get_object_or_404(
                Shopping, pk=pk, user=request.user
            )
            form = ShoppingForm(instance=shopping_item)
        else:
            form = ShoppingForm()

        return render(request, 'products/shopping_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запросы для сохранения товара в корзину.
        """
        pk = kwargs.get('pk')
        if pk:
            shopping_item = get_object_or_404(
                Shopping, pk=pk, user=request.user
            )
            form = ShoppingForm(request.POST, instance=shopping_item)
            if form.is_valid():
                form.save()
                return redirect('products:shopping_cart')
        else:
            form = ShoppingForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect('products:shopping_cart')
        return HttpResponseBadRequest('Invalid form data')

    def delete(self, request, *args, **kwargs):
        """
        Обрабатывает DELETE-запросы для удаления товара из корзины.
        """
        pk = kwargs.get('pk')
        if pk:
            shopping_item = get_object_or_404(
                Shopping, pk=pk, user=request.user
            )
            shopping_item.delete()
            return redirect('products:shopping_cart')
        return HttpResponseBadRequest('No item specified')

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        """
        Обрабатывает запросы, проверяет права доступа и делегирует их соответствующим методам.
        """
        pk = kwargs.get('pk')

        if pk:
            shopping_item = Shopping.objects.filter(
                pk=pk, user=request.user
            ).first()
            if not shopping_item:
                return HttpResponseForbidden(
                    'You do not have permission to access this item.'
                )

        action = request.GET.get('action')
        if action == 'delete' and request.method == 'POST':
            return self.delete(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)


@login_required
def clear_cart(request):
    """
    Представление для очистки корзины текущего пользователя.
    """
    Shopping.objects.filter(user=request.user).delete()
    return redirect('products:shopping_cart')
