from django.shortcuts import render
from .models import Feature


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

    features = [feature1, feature2]
    return render(request, 'index.html', {'feature': feature1})
