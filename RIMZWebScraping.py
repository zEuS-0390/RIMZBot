from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from datetime import datetime

url = "https://news.abs-cbn.com/"
response = urlopen(url)
raw_html = response.read()
page_soup = BS(raw_html, "html.parser")
containers = page_soup.findAll("div", {"class": ["tab-content", "w-tab-content"]})

def getLatestArticles(length):
    articlesList = {}
    latestNews = containers[0].findAll("div", {"id":"latestnews"})
    for news in latestNews:
        articles = news.findAll("article", {"class": ["post-content", "post-item"]})
        for number in range(0, length):
            try:
                dateTime = articles[number].find("time", {"class":["timeago", "timestamp"]})["datetime"]
                timePosStart = dateTime.find("T")+1
                timePosEnd = dateTime.find("+")
                unformattedTime = dateTime[timePosStart:timePosEnd]
                formattedTime = datetime.strptime(unformattedTime, "%H:%M:%S")
                time = str(formattedTime.strftime("%I:%M:%S %p"))
            except:
                time = "Unknown"
            article = articles[number].a.text.strip()
            articlesList[time] = article
    return articlesList
