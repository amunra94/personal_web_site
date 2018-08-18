# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = 'a89605330004@yandex.ru'
            try:
                send_mail(subject, message, from_email, ['andre.rudnitskii@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "askme/askme.html", {'form': form})

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, "askme/success.html")
