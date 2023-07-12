from django.db import models
import uuid
import os

def product_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/products/', filename)

class ProductCategory(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    url_title = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    url_title = models.CharField(max_length=300, db_index=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    short_description = models.CharField(null=True, db_index=True, max_length=360)
    description = models.TextField(db_index=True, null=True)
    is_active = models.BooleanField(default=False, null=True)
    is_delete = models.BooleanField(null=True)
    image = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)

    def __str__(self):
        return f"{self.title}({self.price})"


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags', null=True)

    def __str__(self):
        return self.caption


