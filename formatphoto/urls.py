from django.contrib import admin
from django.urls import path, include


# Main Url's


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('manage/',include('manage_app.urls'))
]

