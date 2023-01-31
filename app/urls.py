from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.views.defaults import page_not_found


# App Url's


handler404 = page_not_found


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('gallery/<str:name>',views.single_category,name='single_category'),
    path('pricing',views.price_page,name='price_page'),
    path('contact',views.contact_page,name='contact_page'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


