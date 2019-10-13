from Hangman import Hangman
from chances import ChancesError


class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()

    def play(self):
        while True:
            print(f'Pozostała liczba szans: {self.hangman.get_chances()}')
            print(self.hangman.get_word_to_guess())
            letter = input('Podaj literę lub słowo: ')

            if self.hangman.is_it_word_to_find(letter):
                # jeśli wpisane słowo jest tym, którego szukamy, to wygrana
                self.win()
                break
                # jeśli wpisana jest litera, a więc nie słowo, to leci dalej

            try:
                # decreasa_chances rzuca wyjątek, który trzeba przechwycić i rzucić dalej (pokazać)
                self.hangman.guess_letter(letter)
            except ChancesError:
                self.lose()
                break

            if self.hangman.are_all_letters_found():
                # nie można tego połączyć z self.hangman.are_all_letters_found()
                # bo nie uzna, że całe słowo jest odgadnięte, kiedy litera nie jest jeszcze wsdtawiona
                self.win()
                break


    def lose(self):
        print('\nSłabiaku!!!')
        self.print_word_to_find()

    def win(self):
        print("\nGratulacje!!!")
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'Szukane słowo to: {self.hangman.get_word_to_find()}')
        # wyprintuje hangman, czyli zmienną, którą podstawiliśmy na początku i podpięliśmy do niego klasę Hangman

def main_game():
    while True:
        game = HangmanGame()
        game.play()

        if input('Chcesz grać ponownie? [t/n]: ') == 'n':
        # to skrót od "answer = input('text')"
            break

if __name__ == '__main__':
main_game()
