from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return  render(request, 'index.html') 
    else:
        return  redirect('/')

from django.http import JsonResponse, HttpResponseBadRequest
import requests
from textblob import TextBlob
api_url = 'https://kgsearch.googleapis.com/v1/entities:search'
api_key = 'AIzaSyCh3bQd3iZsvQu1muV7iI9ktayLMhDbXYc'
session = requests.Session()
def process_input(request):
    if request.method == 'POST':
        input_data = request.POST.get('inputData')

        if input_data.lower() != 'quit':
            # Perform auto-correction

            params = {
                'query': input_data,
                'limit': 3,
                'indent': True,
                'key': api_key,
            }
            response = session.get(api_url, params=params)
            results = ''
            if response.status_code == 200:
                data = response.json()
                max_iterations = min(4, len(data['itemListElement']))
                for i in range(max_iterations):
                    try:
                        results = results + data['itemListElement'][i]['result']['detailedDescription']['articleBody'] + '\n'
                        response = {
                            'message': results,
                            'userInput': input_data
                        }
                        return JsonResponse(response)
                    except KeyError:
                        response = {
                            'message': 'No results found',
                            'userInput': input_data
                        }
                        JsonResponse(response)
            else:
                response = {
                                            'message': 'No results found',
                                            'userInput': input_data
                                        }
                JsonResponse(response)
    print('urg')
    return redirect('/', HttpResponseBadRequest)