from django.db import models

from .managers import ProductManager


class Product(models.Model):
    """Represents a product from the openfoodfacts API."""

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField('product name', max_length=255)
    url = models.CharField('openfoodfacts url', max_length=255)
    nutriscore = models.CharField('product nutriscore', max_length=1)
    description = models.TextField('product description')
    image_url = models.CharField('product image url', max_length=255)
    image_nutrition_url = models.CharField(
        'product nutrition image url', max_length=255
    )
    categories = models.ManyToManyField(
        'categories.Category', related_name='products'
    )

    objects = ProductManager()

    class Meta:
        verbose_name_plural = "products"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def image_url_200(self):
        return self.image_url.replace('full.', '200.')

    @property
    def image_url_400(self):
        return self.image_url.replace('full.', '400.')

    @property
    def image_nutrition_url_200(self):
        return self.image_nutrition_url.replace('full.', '200.')

    @property
    def image_nutrition_url_400(self):
        return self.image_nutrition_url.replace('full.', '400.')
