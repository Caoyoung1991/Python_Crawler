from bs4 import BeautifulSoup
import requests


def get_links():
    urls = []
    list_view = 'http://bj.58.com/pbdnipad/'
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
    return urls

def get_info( ):

    urls = get_links()
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')

        data = {
            'title' : soup.title.text.strip('\r\n').strip('\r\n      '),
            'price' : soup.select('.price_now')[0].text if soup.find_all('span','price_now') else None,
            'place' : soup.select('.palce_li')[0].text.strip('\n') if soup.find_all('div','palce_li') else None,
            'view'  : soup.select('.look_time')[0].text.strip('次浏览') if soup.find_all('span','look_time') else None
        }
        print(data)

get_info( )