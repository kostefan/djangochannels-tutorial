from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('chat', include('chat.urls')),
    path('admin', admin.site.urls),
]