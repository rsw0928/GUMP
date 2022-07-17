from django.shortcuts import render

def index(request):
    return render(request, 'archive/archive.html')
# Create your views here.
