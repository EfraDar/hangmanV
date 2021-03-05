from words import palabras
import random

print("Bienvenido al ahorcado de insectos")

def get_valid_word(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra
mi_palabra = get_valid_word(palabras)
print(mi_palabra + '\n' , len(mi_palabra))