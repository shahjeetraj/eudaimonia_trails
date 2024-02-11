from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from email.message import EmailMessage
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import ssl
import smtplib
from .models import *

# Create your views here.

def home(request):
    return render(request, "web/home.html")

def about(request):
    return render(request, "web/about.html")

def contact(request):
    return render(request, "web/contact.html")

def travelslowlife(request):
    return render(request, "web/travelslowlife.html")

def faq(request):
    return render(request, "web/faq.html")

def tandc(request):
    return render(request, "web/tandc.html")

def privacy(request):
    return render(request, "web/privacy.html")

def bidjourney(request):
    return render(request, "web/bidjourney.html")

def dropdata(request):
    return render(request, "web/dropdata.html")

def tripkart(request):
    return render(request, "web/tripkart.html")

    
def send_email(request):
    subject = "Eudaimonia Trails website contact page comments"
    sender = request.POST.get("contact-email", "")
    name = request.POST.get("contact-name", "")
    message = name+"\n"+sender+"\n"+request.POST.get("contact-message", "")
    
    em = EmailMessage()
    em['From'] = settings.EMAIL_HOST_USER
    em['To'] = settings.EMAIL_HOST_USER
    em['Subject'] = subject
    em.set_content(message)
    context = ssl.create_default_context()
    
    if message:
        try:        
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.sendmail(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, em.as_string())
                info = "Message sent successfully!"
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return render(request, "web/contact.html",{
        "info" : info
        })
    else:
        return HttpResponse("Make sure all fields are entered and valid.")
    
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))