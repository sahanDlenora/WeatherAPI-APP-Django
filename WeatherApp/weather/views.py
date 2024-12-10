import requests
from django.shortcuts import render

def get_weather_data(city):
    api_key = '89f1500c2b9447889b872044241012'  # Replace with your API key
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}&aqi=no"
    response = requests.get(url)

    # Print the response for debugging
    print(response.status_code)
    print(response.json())  # This will print the response body in the console

    if response.status_code == 200:
        return response.json()
    else:
        return None

def index(request):
    weather_data = None
    error = None
    if request.method == "POST":
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
        if not weather_data:
            error = "City not found or API error."

    return render(request, 'index.html', {'weather_data': weather_data, 'error': error})
