from django.shortcuts import render


# Renders Home/Index Page
def index(request):
    return render(request, 'blog/home.html')
