from django.contrib import admin

from products.models import Subcategory, Category, Product, Shopping


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class SubcategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
        'category',
    )


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class ShoppingAdmin(admin.ModelAdmin):
    search_fields = ('product',)


admin.site.empty_value_display = 'Не задано'
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Shopping, ShoppingAdmin)
