from django.shortcuts import render


def home(request):
    return render(request, 'skul/index.html')

def login(request):
    return render(request, 'skul/login.html')

def post(request):
    return render(request, 'skul/post.html')

def about(request):
    return render(request, 'skul/about.html')

# Create your views here.
