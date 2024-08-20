from django.urls import path, re_path

from products import views


app_name = 'products'

urlpatterns = [
    path(
        'categories/', views.CategoryListView.as_view(), name='category_list'
    ),
    path('', views.ProductListView.as_view(), name='product_list'),
    path('cart/', views.ShoppingListView.as_view(), name='shopping_cart'),
    re_path(
        r'^cart/manage(?:/(?P<pk>\d+))?/$',
        views.ShoppingManageView.as_view(),
        name='shopping_manage',
    ),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]
