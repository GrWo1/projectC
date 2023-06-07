import requests
import json
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render
from search_app.models import Word


def index(request):
    return render(request, 'index.html')

def search_view(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        url = f'https://bkrs.info/slovo.php?ch={query}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find('div', id='xinsheng_fullsearch').find_all('div')
        for item in data:
            try:
                key = item.find('div').text
                if key[0].isdigit():
                    key = key[key.find(' ') + 1:]
                results.append(key)
            except AttributeError:
                pass

        # results = list(Word.objects.filter(name__icontains=query).values('name'))
    return JsonResponse(results, safe=False)