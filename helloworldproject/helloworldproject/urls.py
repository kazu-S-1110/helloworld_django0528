from django.contrib import admin
from django.urls import path
from .views import helloworldfunction, HelloWorldView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", helloworldfunction),
    path("hello2/", HelloWorldView.as_view())
]
