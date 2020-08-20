## parser.py
import requests
from bs4 import BeautifulSoup

def crawling() :
    ## HTTP GET Request
    req = requests.get('https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001',  verify=False)

    ## HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select( '#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt > a')

    ## my_titles는 list 객체
    for title in my_titles:
        ## Tag안의 텍스트
        print(title.text.strip())
        ## Tag의 속성을 가져오기(ex: href속성)
        #print(title.get('href'))