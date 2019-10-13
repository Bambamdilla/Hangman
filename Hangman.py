from .chances import Chances
from .words_from_file import Words as RandomWord


class Hangman:
    def __init__(self):
        self.word_to_find = [letter for letter in RandomWord().get_chances()] # POPRAWIC, BO TU JEST BLAD!!!
        # bierze wyraz z RandomWord i od razu rozbija go na literki
        self.chances = Chances()
        # informacja o szansach
        self.word = ['_' for i in self.word_to_find]
        # wstawiamy tyle znaków podkreślenia, ile jest literek w słowie

    def get_chances(self):
        return self.chances.get_chances()

    def get_word_to_guess(self) -> str:
        # zwróć stringa
        return '_'.join(self.word)

    def guess_letter(self, letter: str) -> None:
        # nasza litera jest stringiem, nie zwracamy nic
        # self.chances.decrease_chances rzuca wyjątek
        if letter not in self.word_to_find:
            # jeśli litera nie jest w słowie, to
            self.chances.decrease_chances()
            # zmniejsz szanse, a w razie 0 szans rzuci wyjątkiem
            # wydajniejsze dla programu
        self.append_letter(letter)
        # a jak jest litera w słowie, to dodaj literę

    def are_all_letters_found(self) -> bool:
        return '_' not in self.word

    def append_letter(self, letter: str) -> None:
        tstart = 0
        # 'tstart' to nazwa indeksu
        for i in range(0, self.word_to_find.count(letter)):
            # liczy ile razy dana literka wystąpiła w tekście
            index = self.word_to_find.index(letter, tstart)
            # indeks pierwszego wystąpienia naszej litery
            self.word[index] = letter
            # znak podkreślenia zamieniamy na literę
            tstart = index + 1
            # idziemy z indeksem dalej

    def is_it_word_to_find(self, word: str) -> bool:
        # cokolwiek by to nie było, niech to będzie string i nazywa się 'word', nieważnie jak wcześniej się nazywało
        return word == self.get_word_to_find()

    def get_word_to_find(self) -> str:
        return ''.join(self.word_to_find)
        # ww kod sprawia, że to jest string, tak jak ma być
