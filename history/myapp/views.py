from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
# Create your views here.
def home(request):
    posts = Questions.objects.all()
    return render(request, 'myapp/home.html', {'posts':posts})

def test(request):
    return HttpResponse('<h1>Test Page</h1>')