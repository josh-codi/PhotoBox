from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Service(models.Model):
    title       = models.CharField(max_length=200, blank=False)
    details     = models.TextField(blank=True)
    image       = models.ImageField(upload_to="images/")
    slug        = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('-id',)
    
    def __str__(self):
        return self.title