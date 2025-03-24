import requests
from bs4 import BeautifulSoup

def get_news_articles(company_name):
    search_url = f'https://news.google.com/search?q={company_name}&hl=en'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.find_all('article'):
        title = item.find('h3').text
        summary = item.find('p').text if item.find('p') else 'No summary available'
        articles.append({
            'title': title,
            'summary': summary
        })
        
    return articles[:10]
