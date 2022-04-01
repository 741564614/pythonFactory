# 爬虫爬取网页
import requests  # 导入requests包
from bs4 import BeautifulSoup


def resolving(url):
    '''解析网页内容'''
    strHtml = requests.get(url)  # Get方式获取网页数据
    html = strHtml.text
    bf = BeautifulSoup(html, "html.parser")
    if str(bf).find("文章页跳转")>=0:#处理转跳的情况
        bf=BeautifulSoup(requests.get("https://new.qq.com/rain/a"+url[url.rindex("/"):url.rindex(".")]).text,"html.parser")
    title = bf.find_all('h1')[0].string
    content = bf.find_all('div', class_='content clearfix')[0]
    for item in content.find_all('img'):
        item['src'] = str(item['src']).replace("//", "http://")
    res = [title, str(content)]
    return res

# url="https://new.qq.com/rain/a/20220331A0230700"
# strHtml = requests.get(url)  # Get方式获取网页数据
# html = strHtml.text
# bf = BeautifulSoup(html,"html.parser")
# if str(bf).find("文章页跳转")>=0:
#     bf=BeautifulSoup(requests.get("https://new.qq.com/rain/a"+url[url.rindex("/"):url.rindex(".")]).text,"html.parser")
# title=bf.find_all('h1')[0].string
# content=bf.find_all('div', class_='content clearfix')[0]
# # content.img['src']=str(content.img['src']).replace("//","http://")
# for item in content.find_all('img'):
#     item['src']=str(item['src']).replace("//","http://")
# res=[title,content]
# print(res[0])
# print(res[1])
# # print(bf.div['content clearfix'])
