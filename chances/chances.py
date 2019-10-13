from .chances_error import ChancesError
# kropka oznacza, żeby brać z katalogu, w którym teraz jestem

class Chances:
    # jak szanse się wyczerpią, to klasa obsłuży błąd
    def __init__(self, chances = 9):
        # self.chances = 9 if chances is None else chances
        # pod szanse wstaw 9, jeśli wartość chance nie została podana, w przeciwnym wypadku podaj wartość 'chance'
        self.chances = chances

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1

        if self.chances == 0
            raise ChancesError('Nie masz już szans :P')