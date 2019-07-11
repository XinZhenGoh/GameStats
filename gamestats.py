
# coding: utf-8

# In[56]:


# import libraries
import urllib
import urllib.request
from bs4 import BeautifulSoup


# In[23]:


# specify the url
quote_page = 'http://store.steampowered.com/stats/'
# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# data = soup.find_all('tr', class_='player_count_row')
# data.decompose()

game_list = soup.find_all(class_='player_count_row')


i=0;

for category in game_list:              
    gname = category.find(class_='gameLink').text
    gcount = category.find(class_='currentServers').text
    print(gname+"   "+'\033[1m'+gcount+" ONLINE"+'\033[0m'+'\n')
    i+=1
    #NUMBER OF GAMES TO DISPLAY, YOU CAN CHANGE THIS
    if i == 8:
        break






# In[57]:






#*********************************************************

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
page = opener.open('https://steamcharts.com/app/216150')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='num')

print('MapleStory '+'\033[1m'+game_list.text+" ONLINE"+'\033[0m'+'\n')

#*********************************************************

page = opener.open('https://steamcharts.com/app/560380')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='num')

print('MapleStory2 '+'\033[1m'+game_list.text+" ONLINE"+'\033[0m'+'\n')

#*********************************************************

page = opener.open('https://aries.elluel.net/')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='online-count')

print('AriesMS '+'\033[1m'+game_list.text+'\033[0m'+'\n')
#*********************************************************

page = opener.open('https://steamcharts.com/app/440')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='num')

print('Team Fortress 2 '+'\033[1m'+game_list.text+" ONLINE"+'\033[0m'+'\n')

#*********************************************************

page = opener.open('https://steamcharts.com/app/905640')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='num')

print('CombatArms:Reloaded '+'\033[1m'+game_list.text+" ONLINE"+'\033[0m'+'\n')


# In[32]:






#*********************************************************

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
page = opener.open('')

soup = BeautifulSoup(page, 'html.parser')

game_list = soup.find(class_='num')

print('NONAME')
print(game_list.text+'\n')
