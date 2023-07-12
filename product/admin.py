from django.contrib import admin

from product.models import *


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url_title',
        'is_active',
        'is_delete',

    )
    list_filter = (
        'title',
        'is_active',
        'is_delete'
    )


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url_title',
        'is_active',

    )
    list_filter = (
        'title',
        'is_active',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'brand',
        'price',
        'short_description',
        'description',
        'is_active',
        'is_delete',
        'image'

    )
    list_filter = (
        'id',
        'title',
        'brand',
        'price',
        'short_description',
        'description',
        'is_active',
        'is_delete',
        'image'

    )


@admin.register(ProductTag)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'caption',
        'product',
    )
    list_filter = (
        'id',
        'caption',
        'product',
    )