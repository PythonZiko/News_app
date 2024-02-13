from django.db import models
from django.contrib.auth.models import User

from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model
from ckeditor.fields import RichTextField


# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonalar'


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Categoriyalar'
        

class New(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Sarlavha")
    description = models.CharField(max_length=600, verbose_name = "Tavsif", help_text="Yangilikni qisqacha tavsifi")
    body = RichTextField()
    image = models.ImageField(upload_to="news_images/", verbose_name="Rasm", help_text="Rasm qo'yish uchun joy")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan", help_text="Yaratilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Yangilangan")
    views = models.PositiveBigIntegerField(default=0, verbose_name = "Qarashlar")
    shares = models.PositiveBigIntegerField(default=0, verbose_name = "Ulushlar")
    is_active = models.BooleanField(default=True, verbose_name = "Faoldir")
    hashtags = models.CharField(max_length=70, verbose_name = "Xeshteg")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Aftor", help_text="Aftorni tanlang")
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name = "Zona", help_text="Zonani tanlang")
    category = models.ManyToManyField(Category, verbose_name="Kategoriya")


    @property
    def views(self):
        hit_count = get_hitcount_model().objects.get_for_object(self)
        return  hit_count.hits
    

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-id', '-created']


    def __str__(self):
        return self.title