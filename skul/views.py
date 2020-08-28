from django.shortcuts import render


def home(request):
    return render(request, 'skul/base.html')

# Create your views here.
