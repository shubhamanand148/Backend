from django.shortcuts import render
import json, urllib.request
# Create your views here.
def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        try:
            req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()

            json_data = json.loads(req)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temperature": str(json_data['main']['temp']) + ' K',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
                "data_da": str(json_data['main']['pressure'])
            }

        except urllib.error.HTTPError as err:
            data = "null"

    else:
        city = ''
        data = ''
    return render(request, 'index.html', {'data': data, 'city': city})
