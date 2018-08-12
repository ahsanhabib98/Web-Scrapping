from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
	def __init__(self):
		self.name = ""
		self.link = ""

def get_player_list():

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_='landing__module / landing__leaders')

	#print(div.prettify())
	player_list = []
	for table in div.find_all('table'):
		for a in table.find_all('a'):
			#print(a.text)
			#print(a['href'])
			# home = "http://stats.nba.com"
			new_player = Player()
			new_player.name = a.text
			new_player.link = "http://stats.nba.com"+a['href']
			player_list.append(new_player)

	for one_player in player_list:
		print(one_player.name)
		print(one_player.link)

	driver.quit()

	return player_list

get_player_list()	