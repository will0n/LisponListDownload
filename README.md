# LisponListDownload
Extract audio urls from a Lispon list and save them to a text file.

## Requirement:

You need to intall __Selenium, lxml, BeautifulSoup4__

Chrome browser and chromedriver.exe is needed.

__You have to specify the locations of chrome.exe and chromedriver.exe in the script first.__

## Usage

LisponListDownload.py -o FILE -d DIR \<LISTID\>

Then urls are saved in a form like

>http://s.lispon.moe/lispon/vaqa/2019/04/23/rotoaxa-atIDvTkLGMP.WAV.m4a
>
>&nbsp;&nbsp;&nbsp;&nbsp; dir=はとむぎASMR【全て】 	 
>	 
>&nbsp;&nbsp;&nbsp;&nbsp; output=はとむぎ化粧水で耳のマッサージ.m4a

Use "aria2 --input-file=FILE" to download these audios.

The default FILE name is __download.txt__, and the default DIR name is title of the list.
