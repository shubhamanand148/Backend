from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    text = request.POST['text']
    no_of_words = len(text.split())
    return render(request, 'count.html', {'number': no_of_words})