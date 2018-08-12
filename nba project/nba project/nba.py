from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
import os


class PlayerTeam():
	def __init__(self):
		self.name = ""

class Player():
	def __init__(self):
		self.name = ""
		self.link = ""
		self.height = ""
		self.weight = ""
		self.born = ""
		self.age = ""


def get_player_team_list():

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url = 'https://stats.nba.com/players/'
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_='landing__leaders-body [ row / collapsed ]')

	#print(div.prettify())
	player_team = []
	for h in div.find_all('h2', class_='category-header__name'):
		for a in h.find_all('a'):
			new_team = PlayerTeam()
			new_team.name = a.text
			os.makedirs(new_team.name)
			player_team.append(new_team)

	for one_team in player_team:
		print(one_team.name)

	driver.quit()
	return player_team

# get_player_team_list()


def get_player_list():

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url = 'https://stats.nba.com/players/'
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

	for one_player in player_list[0:40]:
		print(one_player.name)
		print(one_player.link)

	driver.quit()
	return player_list

# get_player_list()


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
		
		# h = h.find('a')
		# w = w.find('a')
		# a = a.find('a')

		p.height = h.text
		p.weight= w.text
		p.born = b.text
		p.age = a.text
		# h = h.find('a')
		# w = w.find('a')
		# a = a.find('a')

		# print(h.text)
		# print(w.text)
		# print(a.text)
		# print(b.text)

	driver.quit()
	return player_list

player_list = get_detail_for_all_players(get_player_list())


with open('nba_player.csv', 'w') as new_file:
	csv_writer = csv.writer(new_file, delimiter='\n')

	def rowparser(row):
		row = row.replace('\n', '')
		return row

	for one_player in player_list[0:2]:

		player = []

		player.append(rowparser(one_player.name))
		player.append(rowparser(one_player.link))
		player.append(rowparser(one_player.height))
		player.append(rowparser(one_player.weight))
		player.append(rowparser(one_player.born))
		player.append(rowparser(one_player.age))

		print(player)

		csv_writer.writerow(player)
