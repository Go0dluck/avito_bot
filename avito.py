import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_date(html):
    soup = BeautifulSoup(html, 'lxml')
    date_board = soup.find('div', class_='js-item-date c-2').get('data-relative-date')
    url_board = soup.find('a', class_='snippet-link').get('href')
    return date_board

def get_title(html):
    soup = BeautifulSoup(html, 'lxml')
    name_title = soup.find('a', class_='snippet-link').get('title')
    return name_title

def get_url_board(html):
    soup = BeautifulSoup(html, 'lxml')
    url_board = soup.find('a', class_='snippet-link').get('href')
    return url_board

def main():
    token = "905542382:AAH-d88AYAZZRWW_pwVAhVKsG_gxsbIRRmk"
    url_telegram = "https://api.telegram.org/bot"
    channel_id = "262700170"
    url_telegram += token
    method = url_telegram + "/sendMessage"

    url_avito = "https://www.avito.ru"
    url = "https://www.avito.ru/kazan/avtomobili/s_probegom/kia/rio/avtomat/ne_bityy?cd=1&pmax=440000&s=104&radius=0&f=188_2845b0"
    html = get_html(url)
    result_data = get_date(html)
    if result_data == "1 час назад":
        text = (get_title(html) + " " + url_avito + get_url_board(html))
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
if __name__ == '__main__':
    main()