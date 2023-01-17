from django.shortcuts import render, redirect
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.title = "Quick"
    feature1.description = "We deliver fast."
    feature1.image = "{% static 'images/call-icon.png' %}"

    feature2 = Feature()
    feature2.id = 2
    feature2.title = "Affordable"
    feature2.description = "We are affordable."
    feature2.image = "{% static 'images/time-seat-icon.png' %}"
    

    #features = [feature1, feature2]
    return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2 })

#The below block allows the users to call the register.html file. And then users can create account/register
def register(request):
    if request.method == 'Post':
        username = request.Post['username']
        email = request.Post['email id']
        password = request.Post['password']
        password2 = request.Post['password2']

        if password == password2:
            #Check if the user is already registered and redirect him to the register screen with the message.
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered previously.')
                return redirect('register')

            #Check if the username is already used.
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already user. Please use another username.')
                return redirect('register')

        return render(request, 'register.html')
