import requests

file = open('login.html', 'w', encoding='utf-8')
url = 'https://www.douban.com/'
headers = {
    'Cookie':'td_cookie=2380433857; ll="118093"; bid=EW5_N0OHfu8; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __utmc=30149280; __utmz=30149280.1550976721.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=AsXl6qqEKUaeUMgDZzdAzpcDAxEVmxlN; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19047; ps=y; dbcl2="190475381:EuZvFYfp9Rg"; ck=e70u; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1550986601%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmGzM7FclgMgxQDZD886euZ8dQFb3_xIWr9q1O1FkMDS%26wd%3D%26eqid%3Dffd24d7700015c62000000035c7206cf%22%5D; _pk_id.100001.8cb4=844fc0e938a14d18.1550939883.3.1550986601.1550979377.; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.880546056.1550939884.1550976721.1550986602.3; __utmt=1; __utmb=30149280.2.10.1550986602; RT=r=https%3A%2F%2Fwww.douban.com%2F&ul=1550986711178'
}
html = requests.get(url=url, headers=headers)
html.encoding = html.apparent_encoding
try:
    file.write(html.text)
except UnicodeEncodeError:
    pass

