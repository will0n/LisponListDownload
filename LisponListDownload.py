from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from bs4 import Comment
import lxml
import re

url = "http://lispon.moe/lispon/fe/act170531/voice?vc_id=74552"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs) #disable image loading
options.binary_location = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chrome.exe'
driverpath = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chromedriver.exe'
driver = webdriver.Chrome(driverpath, options=options)
driver.get(url)
delay = 10 # seconds
try: #wait some time until page scripts load complete
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
driver.close()
#print(soup.prettify())

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
        tag = BeautifulSoup(i+'</a>','lxml')
        str = tag.select_one('a').get('voice-url')
        str += "\n \t dir=" + dir + "\n \t output=" + titles[n] + str[-4:] + "\n"
        f.write(str)
        n += 1
f.close()
