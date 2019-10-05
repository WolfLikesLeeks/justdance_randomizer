import requests 
from bs4 import BeautifulSoup 

# url = 'https://justdance.fandom.com/wiki/Just_Dance_Unlimited'
url = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited'
url2 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited?from=Kurio+ko+uddah+le+jana'
r = requests.get(url2)
data = r.text 
soup = BeautifulSoup(data, 'html.parser')

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


f = open('just_dance_list_example.csv', 'w')
for song in songList:
    f.write(song + '\n')
f.close()

print("FINISHED SCRAPING AND WRITING")