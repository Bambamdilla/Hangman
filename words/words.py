from random import randint


class RandomWord:
    # klasa do losowania wyrazów
    def __init__(self):
        self.words = ('test', 'testtest')

    def get_word(self) -> str:
        # losujemy liczbę, ktęra wskazuję nam słowo z tablicy (tupli)
        index = randint(0, len(self.words) - 1)
        # -1, ponieważ bierzemy długość tablicy minus jeden
        # ostatni element tupli tp -1
        # jak działa zakres tablicy? Dlaczego robimy to na tuplach?
        return self.words[index]
        # nawias kwadratowy, bo wybieramy element tupli
