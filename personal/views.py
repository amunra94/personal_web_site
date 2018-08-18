from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/contacts.html', context={'email': 'andre.rudnitskii@yandex.ru',
                                                              'phone': '+7(977)-269-6705',
                                                              'address':'Moscow',
                                                     })

def about(request):
    return render(request, 'personal/about.html')
