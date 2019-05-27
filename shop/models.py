from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])

    class Meta:
        ordering = ['name']
        verbose_name_plural = ' კატეგორიები'
        verbose_name = ' კატეგორია'


    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 verbose_name=' კატეგორია',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name=' დასახელება')
    slug = models.SlugField(max_length=200, db_index=True,allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y%m%d', blank=True,
                              verbose_name=' პროდუქტის გამოსახულება')
    description = models.CharField(max_length=200, verbose_name=' პროდუქტის აღწერა')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=' ფასი')
    stock = models.PositiveIntegerField(verbose_name=' საწყობშია')
    available = models.BooleanField(default=True, verbose_name=' ხელმისაწვდომია')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    class Meta:
        verbose_name_plural = ' პროდუქტები'
        ordering = ['name']
        index_together = [
            ['id', 'slug']
]
    def __str__(self):
        return self.name