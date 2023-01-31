from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# Manage App Url's


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.singin,name='singin'),
    path('logout',views.signout,name='signout'),
    path('delete/image/<int:id>',views.home_delete,name='home_delete'),
    path('about',views.about,name='about'),
    path('reviews',views.reviews,name='reviews'),
    path('reviews/<int:id>',views.delete_review,name='delete_review'),
    path('category',views.category,name='category'),
    path('category/<int:id>',views.delete_category,name='delete_category'),
    path('gallery/<str:name>',views.single_gallery,name='single_gallery'),
    path('gallery/<str:name>/<int:id>',views.delete_image,name='delete_image'),
    path('prices',views.prices_page,name='prices_page'),
    path('prices/<int:id>',views.delete_prices,name='delete_prices'),
    path('contact',views.contact,name='contact'),
    path('contact/<int:id>',views.delete_contact,name='delete_contact'),
    path('download/contacts',views.export_contact_xlsx,name='export_contact_xlsx'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

