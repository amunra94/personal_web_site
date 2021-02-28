# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    sended = False
    message_client = "Thanks for your question! I will try to answer in near time.\n\n\n" \
                     "Rudnitskiy Andrey"
    admin_email = 'mail@arudnitskiy.ru'

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'From email: ' + from_email + '\n' + message
            recipients = ['andre.rudnitskii@yandex.ru']
            try:
                send_mail(subject, message, admin_email, recipient_list=recipients)
                sended = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            try:
                send_mail(subject, message_client, admin_email, recipient_list=[from_email])
            except:
                return HttpResponse('Invalid header found.')

            render(request, "askme/askme.html", {'form': form, 'sended': sended})

    return render(request, "askme/askme.html", {'form': form, 'sended': sended})
