# HT
# WT
# AGE
# BORN

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://stats.nba.com/player/203083/'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

# div = soup.find('div', class_='landing [ columns large-9 ]')

details = ""
h = soup.find('div', class_='player-stats__item player-stats__height n-p stats-link columns small-3 medium-6')
details += h.text

w = soup.find('div', class_='player-stats__item player-stats__weight n-p stats-link columns small-3 medium-6')
details += w.text

age = soup.find('div', class_='player-stats__item player-stats__age n-p stats-link columns small-3 medium-6')
details += age.text

born = soup.find('div', class_='player-stats__item player-stats__birthdate n-p columns small-3 medium-6')
details += born.text
details.strip()
print(details)
# #print(div.prettify())
# for a in div.find_all('a'):
# 	print(a.text)
	
# driver.quit()	