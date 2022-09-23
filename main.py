from urllib.request import urlopen
from bs4 import BeautifulSoup

# urllib.request() : URL에서 데이터를 가져오는 기본 기능을 제공
# urlopen() : 기본이 Get 방식으로 작동
html = urlopen("https://maplestory.nexon.com/News/Notice")
# print(html.read(500).decode('utf-8'))

# BeautifulSoup : 결과를 보기 편하게 정리해준다.
# html.parser : HTML 문법 규칙에 따른 문자열을 문법에 따라 분석해주는 것
# prettify() : 이 메서드는 html 결과를 예쁘게 들여쓰기 해서 보여줍니다!
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

# 뉴스의 제목들을 긁어오기
title_list = []
news_board = soup.select_one("div.news_board")
titles = news_board.select("ul>li>p>a>span")
titles = (str(titles).split("<span>"))
for title in titles:
    title_list.append(title[:-9])

date_list = []
dates = soup.select("div.heart_date")
for date in dates:
    date = date.select("dl>dd")
    date_list.append(str(date)[5:-7])

news_list = [news for news in zip(title_list, date_list)]
for news in news_list:
    print(news)