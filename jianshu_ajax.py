import requests
import pymongo
from lxml import etree

client = pymongo.MongoClient('localhost', 2017)
mydb = client.mydb
timeline = mydb.timeline
print('connected')
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}


def get_time_info(url, page):
    user_ids = url.split('/')
    user_id = user_ids[4]
    if url.find('page='):
        page = page + 1
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd = info.xpath('div/div/div/span/@data-datatime')[0]
        type = info.xpath('div/div/div/span/@data-type')
        timeline.insert_one({'date': dd, 'type': type})
    id_infos = selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(id_infos) > 1:
        feed_id = id_infos[-1]
        max_id = feed_id.split('-')[1]
        next_url = 'http://www.jianshu.com/u/%s/timeline?max_id=%s&page=%s' % (user_id, max_id, page)
        get_time_info(next_url, page)


if __name__ == '__main__':
    get_time_info('https://www.jianshu.com/u/9104ebf5e177/timeline', 1)
    print('OK')
