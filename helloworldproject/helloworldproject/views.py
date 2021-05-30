from django.http import HttpResponse
from django.views.generic import TemplateView
import os


def helloworldfunction(request):
    returnobject = HttpResponse("<h1>hello world</h1>")
    return returnobject


class HelloWorldView(TemplateView):
    template_name = "hello.html"  # HelloWorldViewが呼び出されたらhello.htmlを返すよう記述している
