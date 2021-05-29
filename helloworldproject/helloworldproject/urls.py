from django.contrib import admin
from django.urls import path
from .view import helloworldfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", helloworldfunction)
]
