from django.shortcuts import render


# Renders Home/Index Page
def index(request):
    return render(request, 'blog/home.html')


def contact(request):
    return render(request, 'blog/basic.html', {'content':['If you would like to contact me, please email me at','J.morrissette@jamdevs.com']})
