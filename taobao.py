from selenium import webdriver
import time
from lxml import etree
import pymongo


client = pymongo.MongoClient()
mydb = client.mydb
taobao = mydb.taobao
driver = webdriver.PhantomJS()
driver.maximize_window()


def get_info(url, page):
    page = page + 1
    driver.get(url)
    driver.implicitly_wait(10)
#    print(driver.page_source)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        data = info.xpath('div/div/a')[0]
        goods = data.xpath('string(.)').strip()
        price = info.xpath('div/div/div/strong/text()')[0]
        sell = info.xpath('div/div/div[@class="deal-cnt"]/text()')[0]
        address = info.xpath('/div[2]/div[3]/div[2]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')
        commodity = {
            "good": goods,
            "price": price,
            "sell": sell,
            "shop": shop,
            "address": address
        }
#        print(commodity)
        taobao.insert_one(commodity)
    if page <= 50:
        NextPage(url, page)
    else:
        pass


def NextPage(url, page):
    driver.get(url)
    driver.implicitly_wait(10)
    print(driver.page_source)
    driver.find_element_by_css_selector('a.J_Ajax.num.icon-tag').click()
    time.sleep(4)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    get_info(driver.current_url, page)


if __name__ == '__main__':
#    word = input("please input the good you want:")
    page = 1
    url = 'https://s.taobao.com/'
    driver.get(url)
    driver.save_screenshot('taobao.png')
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')
    driver.find_element_by_class_name('btn-search').click()
    driver.implicitly_wait(5)
    driver.find_element_by_class_name('tb-logo-cn').click()
    driver.implicitly_wait(5)
    driver.save_screenshot('taobao.png')
    get_info(driver.current_url, page)
