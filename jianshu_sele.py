from selenium import webdriver
url = 'https://www.jianshu.com/p/5d2fb7693d88'


def get_info(url):
    include_title = []
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.implicitly_wait(10)
    author = driver.find_element_by_xpath('//span[@class="name"]/a').text
    date = driver.find_element_by_xpath('//span[@class="publish-time"]').text
    word = driver.find_element_by_xpath('//span[@class="wordage"]').text
    view = driver.find_element_by_xpath('//span[@class="views-count"]').text
    comment = driver.find_element_by_xpath('//span[@class="comments-count"]').text
    like = driver.find_element_by_xpath('//span[@class="likes-count"]').text
    include_names = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
    for include_name in include_names:
        include_title.append(include_name.text)
    print(author, date, word, view, comment, like, include_title)


if __name__ == "__main__":
    get_info(url)
