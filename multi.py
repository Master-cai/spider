import requests
import re
import multiprocessing


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
}


def rescr(url):
    res = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    for id in ids:
        print(id)


if __name__ == "__main__":
    urls = ['https://www.qiushibaike.com/text/page/{}'.format(i) for i in range(1, 36)]
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool()
    print(1)
    pool.map(rescr, urls)
    print(2)
    #for url in urls:
    #    rescr(url)
