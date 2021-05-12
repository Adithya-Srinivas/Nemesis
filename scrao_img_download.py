from selenium import webdriver
from bs4 import BeautifulSoup

chrome = webdriver.Chrome('./chromedriver')
chrome.maximize_window()
chrome.get('https://downtowndallas.com/experience/stay/')
chrome.refresh()

page = []

# using page[] to loop through pages

def download_img(page):
    for count,value in enumerate(page):
      chrome.get(value)
      chrome.save_screenshot(f'{count}.png')

# Getting the links from href to go to image source page

def get_images(links):

    global src
    chrome.get(links)
    html_info = BeautifulSoup(chrome.page_source, features="lxml")
    img_url = html_info.select('body > main > div > img:nth-child(1)')

    for lin in img_url:
        src = lin.get('src')
        page.append(src)

    return download_img(page)


# Using beautifulsoup get info of the source page

html_info = BeautifulSoup(chrome.page_source, features="lxml")
buttons = html_info.find_all('a',class_='place-square__btn')

# Getting href
for links in buttons:
    link = links.get('href')
    get_images(link)