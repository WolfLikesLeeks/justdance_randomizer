import random
from time import sleep

number = int(input("How many songs? "))
file = open('just_dance_list.csv', 'r')
songRead = file.readlines()
file.close()
playlist = []
for j in range(number):
    for i in range(10):
        songIndex = random.randint(0, len(songRead)-1)
        songName = songRead[songIndex]
        print('', end="\r")
        print("RANDOMIZED SONG: {}".format(str(songName[:-1])), end="\r")
        sleep(0.01)
    playlist.append(songName)

print('!'*128)
print('\n\n\n')
for x in playlist:
    st = x + '\n'
    print(st)
print('\n\n\n')
print('!'*128)
