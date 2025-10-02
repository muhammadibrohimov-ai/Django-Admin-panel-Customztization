from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'
        ordering = ['created_at']
    
    
class Book(models.Model):
    GENRE_CHOICES = [
        ['badiiy', 'Badiiy'],
        ['fantastik', 'Fantastik'],
        ['ilmiy', 'Ilmiy'],
        ['romantik', 'Romantik'],
        ['diniy', 'Diniy'],
    ]
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Book'
        ordering = ['created_at']
