from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from bs4 import Comment
import lxml
import re
import getopt
from sys import argv
from sys import exit

BIN_LOC = r'' #put full path of chrome.exe here
DR_LOC = r'' #put full path of chromedriver.exe here
#BIN_LOC = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chrome.exe' #example here
#DR_LOC = r'D:\Portable\GoogleChromePortable\App\Chrome-bin\chromedriver.exe' #example here
if not (BIN_LOC and DR_LOC):
    print('Please specify you location of chrome.exe and chromedriver.exe as BIN_LOC and DR_LOC')
    exit(2)
    
try:
  opts, args = getopt.getopt(argv[1:],"o:d:")
except getopt.GetoptError:
  print('LisponListDownload.py -o OUTPUT -d DIR <LISTID>')
  exit(2)

output = ''
dir = ''
for opt,arg in opts:
    if opt == '-o':
        output = arg
    elif opt == '-d':
        dir = arg

if not output:
    output = 'download.txt'
url = 'http://lispon.moe/lispon/fe/act170531/voice?vc_id='+args[0]
#url = "http://lispon.moe/lispon/fe/act170531/voice?vc_id=74552"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs) #disable image loading
options.binary_location = BIN_LOC
driverpath = DR_LOC
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
f = open(output, mode='w', encoding='utf-8')
#f = open('download.txt', mode='w', encoding='utf-8')
titles = []
if not dir:
    dir = soup.select_one('h1.header-title').text
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
