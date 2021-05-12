from selenium import webdriver
from bs4 import BeautifulSoup
import csv

chrome = webdriver.Chrome('./chromedriver')
chrome.maximize_window()
chrome.get('https://downtowndallas.com/experience/stay/')
chrome.refresh()

def click_on_place(href):

    global info_text, links
    chrome.get(href)
    chrome.implicitly_wait(20)

    html_info = BeautifulSoup(chrome.page_source, features="lxml")

    title = html_info.find('h1').get_text()
    info = html_info.select('div.place-info')

    for i in info:
        info_text = " ".join(i.get_text().split())

    img_url = html_info.select('body > main > div > img:nth-child(1)')

    for lin in img_url:
        links = lin.get('src')

    return write_to_csv(title, info_text, links)

# writing to csv

def write_to_csv(title, info, img_link):
    with open('database.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([title, info, img_link])

html_info = BeautifulSoup(chrome.page_source, features="lxml")

buttons = html_info.find_all('a',class_='place-square__btn')

for links in buttons:
    href = links.get('href')
    click_on_place(href)






