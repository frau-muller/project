from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
# Create your views here.

def home(request):
    myapp = Questions.objects.order_by('-created_at')
    context = {
        'myapp': myapp,
        'title': 'Список новостей'
    }
    return render(request, template_name='myapp/home.html', context=context)