from django.shortcuts import render


# Renders Home/Index Page
def index(request):
    return render(request, 'personal/home.html', {'skills':['Python','HTML','CSS'],'frameworks':['Django']})


def contact(request):
    return render(request, 'personal/contact.html', {'content':['If you would like to contact me, please email me at',
                                                            'J.morrissette@jamdevs.com']})
