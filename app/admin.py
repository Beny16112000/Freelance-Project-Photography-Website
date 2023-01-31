from django.contrib import admin
from .models import HomeImages, About, Reviews, Category, CategoryImages, Prices, Contact


# Register your models here.


class HomeImagesAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(HomeImages, HomeImagesAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('phone','image_tag')
admin.site.register(About, AboutAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name','image_tag')
admin.site.register(Reviews, ReviewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)


class CategoryImagesAdmin(admin.ModelAdmin):
    list_display = ('category','image_tag')
admin.site.register(CategoryImages, CategoryImagesAdmin)


class PricesAdmin(admin.ModelAdmin):
    list_display = ('service','price')
admin.site.register(Prices, PricesAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone')
admin.site.register(Contact, ContactAdmin)

