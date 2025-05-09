from django.db import models
class Category(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=50, blank=True, null= True)
    image = models.ImageField(upload_to='images/')
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null = True)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    children = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    sorting = models.SmallIntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)


    def __str__(self):
        return self.name
