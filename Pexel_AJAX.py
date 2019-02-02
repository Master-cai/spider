from bs4 import BeautifulSoup
import requests


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'
}
urls = ['https://www.pexels.com/search/book/?page={}'.format(i) for i in range(1, 20)]
path = 'D:/new/python/Pexel/'


for url in urls:
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('article > a> img')
    for img in imgs:
        photo_url = img.get('src')
        pic = requests.get(photo_url, headers=headers)
        file = open(path+photo_url.split('?')[0][-10:], 'wb')
        file.write(pic.content)
        file.close()

