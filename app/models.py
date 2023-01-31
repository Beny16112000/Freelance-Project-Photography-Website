from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from django_cleanup import cleanup


# Create your models here.


class HomeImages(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='media/home_images')

    class Meta:
        verbose_name_plural = 'Home Images'

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % (self.img.url))



class About(models.Model):
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    instegram = models.CharField(max_length=70)
    instegram_link = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=70)
    img = models.ImageField(upload_to='media/about_images')

    class Meta:
        verbose_name_plural = 'About'

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % (self.img.url))



class Reviews(models.Model):
    name = models.CharField(max_length=70)
    role = models.CharField(max_length=55)
    detail = models.TextField(blank=True)
    img = models.ImageField(upload_to='media/reviews')

    class Meta:
        verbose_name_plural = 'Reviews'

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % (self.img.url))



class Category(models.Model):
    name = models.CharField(max_length=15)
    detail = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Category'



class CategoryImages(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/category')

    class Meta:
        verbose_name_plural = 'Category Images'

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % (self.img.url))



class Prices(models.Model):
    service = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()

    class Meta:
        verbose_name_plural = 'Prices'



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contact'


