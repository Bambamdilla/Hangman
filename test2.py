from test1 import Test1

# jeżeli typ pliku to main, to plik zostaje uruchomiony bezpośrednio
# Jeżęli jednak test1 zostanie zaimportowany, to jako moduł, bo nie chcemy go przecież uruchomić
# Jeżeli chcemy zaimportować plik, to po prostu:
# hangman_text_game.main_game()

import test1

print(test1)