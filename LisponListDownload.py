from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import Comment
import lxml
import re

url = "https://lispon.moe/lispon/fe/act170531/voice?vc_id=74552"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.binary_location = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chrome.exe'
driverpath = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chromedriver.exe'
driver = webdriver.Chrome(driverpath, options=options)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
driver.close()

songtitles = soup.select("div#songList h3")
f = open('download.txt', mode='w', encoding='utf-8')
titles = []
dir = 'dir'
for h in songtitles:
    titles.append(h.text)
c = soup.select_one("div#songList").find_all(string=lambda text: isinstance(text, Comment))
n = 0
for i in c:
    if re.match('.*voice-url.*',i)!=None:
        tag = BeautifulSoup(i+'</a>')
        str = tag.select_one('a').get('voice-url')
        str += "\n \t dir=" + dir + "\n \t output=" + titles[n] + str[-4:] + "\n"
        f.write(str)
        n += 1
f.close()