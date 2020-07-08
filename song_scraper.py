import requests 
from bs4 import BeautifulSoup 

# url = 'https://justdance.fandom.com/wiki/Just_Dance_Unlimited'
url_1 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited'
url_2 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited?from=Kurio+ko+uddah+le+jana'
url_3 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_Unlimited?from=There+Is+Nothing+Better+In+The+World+%28%D0%9D%D0%B8%D1%87%D0%B5%D0%B3%D0%BE+%D0%BD%D0%B0+%D1%81%D0%B2%D0%B5%D1%82%D0%B5+%D0%BB%D1%83%D1%87%D1%88%D0%B5+%D0%BD%D0%B5%D1%82%D1%83%29'
url_4 = 'https://justdance.fandom.com/wiki/Category:Songs_in_Just_Dance_2020'
bypass = []
urls = [url_1, url_2, url_3, url_4]
songList = []
for url in urls:
    r = requests.get(url)
    data = r.text
    data = data.encode('ascii', 'ignore')
    soup = BeautifulSoup(data, 'html.parser')

    
    for element in soup.find_all('a'):
        try:
            title = element['title']
            if 'Just Dance' in title:
                continue
            elif 'Add new page' in title:
                continue
            elif 'Fandom' in title:
                continue
            elif 'Category:Songs' in title:
                continue
            elif 'Special:Categories' in title:
                continue
            else:
                if title not in songList:
                    if title not in bypass:
                        print("Appending {}".format(title))
                        songList.append(title)
                    else:
                        break
                    
        except TypeError:
            continue
        except KeyError:
            continue
##        except UnicodeEncodeError:
##            continue

songList.append("Just Dance") #For Lady Gaga's song
f = open('just_dance_list.csv', 'a')
for song in songList:
    f.write(song + '\n')
f.close()

print("FINISHED SCRAPING AND WRITING")
