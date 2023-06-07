import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def search_view(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        url = f'https://bkrs.info/slovo.php?ch={query}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find('div', id='xinsheng_fullsearch').text
        data = data.replace('\n\n', '')
        list_data = data.split('\n')
        results = []
        for i in range(0, len(list_data) - 1, 2):
            rus_word = list_data[i + 1]
            ch_word = list_data[i]
            if rus_word[0].isdigit():
                rus_word = rus_word[rus_word.find(' ') + 1:]
            item = rus_word + " - " + ch_word
            results.append(item)
    return JsonResponse(results, safe=False)