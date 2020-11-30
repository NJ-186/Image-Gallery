from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):

    tag_choices = [
        ('portrait','portrait'),
        ('sketch','sketch'),
        ('landscape','landscape'),
        ('nature','nature'),
        ('b&w','b&w'),
        ('wildlife','wildlife')
    ]

    tag = models.CharField( 
        max_length = 10 , 
        default = 'portrait',
        choices = tag_choices
    )

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        db_table = 'tag'

    def __str__(self):
        return self.tag

class ImageObject(models.Model):
    
    image_file = models.FileField(upload_to='pics')
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'image object'
        verbose_name_plural = 'image objects'
        db_table = 'image_object'