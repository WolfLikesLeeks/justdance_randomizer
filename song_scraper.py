import requests 
from bs4 import BeautifulSoup 

# url = 'https://justdance.fandom.com/wiki/Just_Dance_Unlimited'
url = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited'
url2 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited?from=Kurio+ko+uddah+le+jana'
r = requests.get(url2)
data = r.text 
soup = BeautifulSoup(data, 'html.parser')

# def scrapeAll(content):
# print(soup.prettify())

# def pullSongName(context):
# for item in range(len(soup)):
#     print("{}: {}".format(item, soup[item]))

songList = []
for element in soup.find_all('a'):
    try:
        title = element['title']
        if "Just Dance" in title:
            continue
        else:
            if title not in songList:
                print("Appending {}".format(title))
                songList.append(title)
                if title == "Worth It":
                    break
    except TypeError:
        continue
    except KeyError:
        continue

print("FINISHED")

# Writing to CSV
# with open('just_dance_list_example.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter='\n')
#     csv_writer.writerow(songList)

f = open('just_dance_list_example.csv', 'w')
for song in songList:
    f.write(song + '\n')
f.close()

# Reading CSV

# file = open('just_dance_list.csv', 'r')
# songRead = file.read()
# file.close()

# Random Song Selector
import random

def chooseSong():
    songIndex = random.randint(0, len(songRead))
    print(songRead[songIndex])