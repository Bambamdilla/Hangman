from random import randint
import os

# wczytać zawartość pliku (może do listy?)
# wylosować słowo z listy (albo innej takiej)
# zwrócić wylosowane słowo

class Words:

    def get_word():
        with open('words.txt', 'r') as file:
            data = file.readlines()
            data = [i.replace('\n', '') for i in data]
            # print(data)

        index = randint(0, len(data))
        print(data[index])

    get_word()