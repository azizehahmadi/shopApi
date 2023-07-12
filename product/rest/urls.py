from django.urls import path, include
from product.rest.views import ProductCategoryView, ProductCategoryDetailView,\
    ProductCategoryCreateView, ProductBrandView, ProductBrandDetailView, ProductCategoryViewBYAdmin, \
    ProductBrandViewBYAdmin, ProductBrandCreateView, BrandOfProduct, ProductViewSet, ProductTagViewSet, TagsOfProduct
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', ProductViewSet),
router.register('product-tags', ProductTagViewSet),

urlpatterns = [

    path('product-category-by-admin/', ProductCategoryViewBYAdmin.as_view(), name='product-category-by-admin'),
    path('product-category/<str:title>/', ProductCategoryView.as_view(), name='product-category'),
    path('product-category-detail/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('product-category-create/', ProductCategoryCreateView.as_view(), name='product-category-create'),


    path('product-brand-by-admin/', ProductBrandViewBYAdmin.as_view(), name='product-brand-by-admin'),
    path('product-brand/<str:title>/', ProductBrandView.as_view(), name='product-brand'),
    path('product-brand-detail/<int:pk>/', ProductBrandDetailView.as_view(), name='product-brand-detail'),
    path('product-brand-create/', ProductBrandCreateView.as_view(), name='product-brand-create'),
    path('brand/<int:pk>/products/', BrandOfProduct.as_view(), name='brand-product'),

    path('product-tags/<int:pk>/tags/', TagsOfProduct.as_view(), name='tag_of_product'),

    path('', include(router.urls))


]

