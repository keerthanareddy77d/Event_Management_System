from . import models
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import Register
import qrcode
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse

def about(request):
    return render(request,'aboutus.html')

def halls(request):
    return render(request,'halls.html')

def catering(request):
    return render(request,'catering.html')
def celebs(request):
    return render(request,'celebs.html')
def cards(request):
    return render(request,'cards.html')

def login(request):
    return render(request, 'loginpagehtml.html')

def register(request):
    return render(request, 'registeruser.html')

def home(request):
    return render(request, 'carousel.html')

def qrcode3(request):
    return render(request,'qrcode1.html')

from django.http import FileResponse
def qrcode12(request):
    if request.method == 'POST':
        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        data1=sid+sname
        #creating an instance of QRCode class
        qr=qrcode.QRCode(version=1,box_size=30,border=5)
        #Adding data to the instance 'qr'
        qr.add_data(data1)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        img.save('static/images/KLU.png')
        img1=open('static/images/KLU.png','rb')
        #rb-read binary
        response = FileResponse(img1)
        return response
    else:
        return HttpResponse("not working")




import requests

def showweather(request):
    return render(request, 'weather.html')

def weather(request):
    api_key = ''
    cname = request.POST.get('cname')
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={cname}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        # print("No City Found")
        return HttpResponse("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        # °C = [(°F-32)×5] / 9
        temp1 = (((temp - 32) * 5) / 9)
        # print(type(temp))
        # print(f"The weather in {cname} is: {weather}")
        # print(f"The temperature in {cname} is: {temp}ºF")
        # print(f"The temperature in {cname} is: {temp1}ºC")
        data_details = {'Weather': f"{weather}", 'Temparature in F': f"{temp}", 'Temparature': f"{temp1}"}
        return HttpResponse(json.dumps(data_details))

def loginInput(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'carousel.html')
            # assuming 'index' is a valid URL
        else:
            messages.info(request,'Invalid credentials')
            return render(request, 'loginpagehtml.html')

    else:
        return render(request, "login.html")

def registerInput(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        confirm =request.POST.get('uconfirm')
        email= request.POST.get('ucall')
        mobile= request.POST.get('umobile')
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'Registeruser.html')
            else:
                user = User.objects.create_user(username=username, password=confirm)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'loginpagehtml.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'Registeruser.html')
        return render(request, "login.html")
    else:
        return render(request, "Registeruser.html")




def contact(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['keerthanareddy77d@gmail.com'],
                  fail_silently=False)
    return render(request, 'contact.html')

