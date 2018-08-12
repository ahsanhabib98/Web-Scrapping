from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

class Player():
	def __init__(self):
		self.name = ""
		self.link = ""
		self.height = ""
		self.weight = ""
		self.born = ""
		self.age = ""

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
			new_player = Player()
			new_player.name = a.text
			new_player.link = "http://stats.nba.com"+a['href']
			player_list.append(new_player)

	for one_player in player_list:
		print(one_player.name)
		print(one_player.link)

	driver.quit()
	return player_list

def get_detail_for_all_players(player_list):
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	for p in player_list[0:2]:
		# url = 'http://stats.nba.com/player/203083/'
		url = p.link
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'lxml')

		# div = soup.find('div', class_='landing [ columns large-9 ]')

		h = soup.find('div', class_='player-stats__item player-stats__height n-p stats-link columns small-3 medium-6')
		w = soup.find('div', class_='player-stats__item player-stats__weight n-p stats-link columns small-3 medium-6')
		a = soup.find('div', class_='player-stats__item player-stats__age n-p stats-link columns small-3 medium-6')
		b = soup.find('div', class_='player-stats__item player-stats__birthdate n-p columns small-3 medium-6')
		p.height = h.text
		p.weight= w.text
		p.born = b.text
		p.age = a.text
	driver.quit()
	return player_list


def get_all_player_image(player_list):
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')

	for player in player_list:

		url = player.link
		driver.get(url)

		time.sleep(2)

		soup = BeautifulSoup(driver.page_source, 'lxml')
		div = soup.find('div', class_='player-summary__image-block')
		img = div.find('img')

		print(img['src'])

		if not os.path.exists('nba_player\{0}.jpg'.format(player.name)):

			f = open('nba_player\{0}.jpg'.format(player.name),'wb')
			f.write(requests.get(img['src']).content)
			f.close()

	driver.quit()

get_all_player_image(get_player_list())

