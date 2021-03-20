from words import palabras
from colorama import Fore, Style, init
import random
init()
print("Bienvenido al ahorcado de insectos")

def get_valid_word(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra
mi_palabra = get_valid_word(palabras)
print(mi_palabra +'\n', Fore.RED + '_ ' * len(mi_palabra))