from product.models import ProductCategory, ProductBrand, Product, ProductTag
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = (
            'id', 'title', 'url_title', 'is_active', 'is_delete'
        )

    def validate_title(self, attrs):
        lower_title = attrs.lower()
        if ProductCategory.objects.filter(title__exact=lower_title).exists():
            msg = _('the title is already exists!')
            raise serializers.ValidationError(msg)
        return lower_title


class ProductBrandSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ProductBrand
        fields = (
            'id', 'title', 'is_active', 'products',
        )

    def validate_title(self, data):
        lower_title = data.lower()
        if ProductBrand.objects.filter(title__exact=lower_title).exists():
            msg = _('the title is already exists!')
            raise serializers.ValidationError(msg)
        return lower_title


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ProductCategory.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'brand',
            'price',
            'short_description',
            'description',
            'is_active',
            'is_delete',
            'image',
        )

class ProductDetailSerializer(ProductSerializer):
    category = ProductCategorySerializer(many=True, read_only=True)

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'image')
        read_only_fields = ('id',)

class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = ('id', 'caption', 'product')

