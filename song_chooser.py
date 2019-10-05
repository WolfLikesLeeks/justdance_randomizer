import random
from time import sleep

file = open('just_dance_list.csv', 'r')
songRead = file.readlines()
file.close()

for i in range(100):
    songIndex = random.randint(0, len(songRead)-1)
    songName = songRead[songIndex]
    print('', end="\r")
    print("RANDOMIZED SONG: {}".format(str(songName[:-1])), end="\r")
    sleep(0.01)
print('!'*128)
print('\n\n\n\t{}\n\n\n'.format(songName))
print('!'*128)