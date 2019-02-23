import requests
from lxml import etree
import pymongo
import re
import json
from multiprocessing import Pool
import time


client = pymongo.MongoClient()
mydb = client.mydb
weeklyhot = mydb.weekly


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
}


def get_url(url):
    #print('en')
    html = requests.get(url, headers=headers)
    #print('html')
    selector = etree.HTML(html.text)
    user_parts = selector.xpath('//ul[@class="note-list"]/li/div/a/@href')
    #print('get_url')
    for user_part in user_parts:
        get_info(user_part)


def get_info(user_url):
    url = 'https://www.jianshu.com/' + user_url
    html = requests.get(url, headers=headers)
    #print(html.text)
    selector = etree.HTML(html.text)
    #print(selector)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    print(author)
    article = selector.xpath('//h1[@class="title"]/text()')[0]
    date = selector.xpath('//span[@class="publish-time"]/text()')[0]
    word_number = selector.xpath('//span[@class="wordage"]/text()')[0].split(' ')[-1]
    view = re.findall('"views_count":(.*?),', html.text, re.S)
    comment = re.findall('"comments_count":(.*?),', html.text, re.S)[0]
    like = re.findall('"likes_count":(.*?),', html.text, re.S)[0]
    id = re.findall('"id":(.*?),', html.text, re.S)[0]
    gain_url = 'https://www.jianshu.com/notes/{}/rewards?count=20'.format(id)
    #gain_url = 'https://www.jianshu.com/notes/41753278/rewards?count=20'
    wb_data = requests.get(gain_url, headers=headers)
    print(wb_data.text)
    json_data = json.loads(wb_data.text)
    gain = json_data['rewards_count']
    info = {
        'author': author,
        'article': article,
        'date': date,
        'word': word_number,
        'view': view,
        'comment': comment,
        'like': like,
        'gain': gain
    }
    weeklyhot.insert_one(info)


if __name__ == "__main__":
    urls = ['https://www.jianshu.com/trending/weekly?page={}'.format(str(i)) for i in range(0, 11)]
    pool = Pool(processes=4)
    print('pool')
    pool.map(get_url, urls)
    #for url in urls:
    #   get_url(url)
    print('OK')
