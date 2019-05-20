import requests
from bs4 import BeautifulSoup

def SearchMethod(query):
    URL = 'https://search.naver.com/search.naver?&where=news&query='
    fullURL = URL + query
    data = requests.get(fullURL).text
    soup = BeautifulSoup(data, 'html.parser')
    news_titles = soup.find_all(class_='_sp_each_title')
    title_list = []
    for title in news_titles:
        title_list.append({'url': title.get('href'), 'title': title.get('title')})

    return title_list