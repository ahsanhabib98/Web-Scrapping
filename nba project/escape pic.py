from selenium import webdriver
from bs4 import BeautifulSoup
import requests


driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://stats.nba.com/player/203076/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', class_='player-summary__image-block')
img = div.find('img')

print(img['src'])

f = open('name.jpg','wb')
f.write(requests.get(img['src']).content)
f.close()

driver.quit()
