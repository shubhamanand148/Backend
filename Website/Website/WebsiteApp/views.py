from django.shortcuts import render, redirect
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    '''
    feature1 = Feature()
    feature1.id = 1
    feature1.title = "Quick"
    feature1.description = "We deliver fast."
    feature1.image = 'images/call-icon.png'

    feature2 = Feature()
    feature2.id = 2
    feature2.title = "Affordable"
    feature2.description = "We are affordable."
    feature2.image = 'images/time-seat-icon.png'

    feature3 = Feature()
    feature3.id = 3
    feature3.title = "Always Available"
    feature3.description = "We are always up to serve you."
    feature3.image = 'images/watch-icon.png'

    features = [feature1, feature2, feature3]
    '''

    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

#The below block allows the users to call the register.html file where users can create/register account
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email id']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #Check if the user is already registered and redirect him to the register screen with the message.
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered previously.')
                return render(request, 'register.html')

            #Check if the username is already used.
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken. Please use another username.')
                return render(request, 'register.html')

            #If the Email ID and Username are unique, create user.
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password is not same.')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def posts(request, pk):
    return render(request, 'posts.html', {'pk': pk})
