from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_='landing__module / landing__leaders')

#print(div.prettify())

for table in div.find_all('table'):

	for a in table.find_all('a'):
		print(a.text)
	
driver.quit()	