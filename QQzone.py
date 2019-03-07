import time
from selenium import webdriver
import csv
import pymongo


client = pymongo.MongoClient()
mydb = client.mydb
qq_zone = mydb.qq_zone
driver = webdriver.PhantomJS()
#driver.maximize_window()


def get_info(qq):
    driver.get('https://user.qzone.qq.com/1214631990/311')
    driver.implicitly_wait(10)
    driver.save_screenshot('qq.png')
    try:
        driver.find_element_by_id('login_div')
        a = True
        driver.save_screenshot('qq.png')
    except:
        a = False
        print('find_error')
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('719591339')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('789520asd***')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        driver.save_screenshot('qq.png')
        b = True
    except:
        b = False
        print('login_error')
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        contents = driver.find_elements_by_css_selector('.content')
        times = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for content, tim, in zip(contents, times):
                data = {
                    'time': tim.text,
                    'content': content.text
                }
                print(data)
                #qq_zone.insert_one(data)


if __name__ == '__name__':
    qq_list = [1214631990]
    for qq in qq_list:
        get_info(1214631990)
