from django.db import models 

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 100, unique = True)

    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name', )

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args = [self.slug])


class Product(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 100, db_index = True)        
    description = models.TextField()

    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE) 
    image = models.ImageField()

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args = [self.id, self.slug])
