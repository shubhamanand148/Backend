from django.shortcuts import render

# Create your views here.
def room(request):
    return render(request, 'room.html')

def home(request):
    return render(request, 'home.html')
