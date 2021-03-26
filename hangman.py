from words import palabras
#from colorama import Fore, Style, init
import random
import string
#init()
print("Bienvenido al ahorcado de insectos")

def get_valid_word(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabras[palabra]

def hangman():
    word=get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


while len(word_letters) > 0:
    user_letter = input('Guess a letter: ').upper()
if user_letter in alphabet - used_letters:
    used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)
        print("letter is not in word.")
    elif user_letter in used_letters:
            print("You have already used that character. Please try again ")
    else:
            print("Invalid character. Please try again.")

# mi_palabra = get_valid_word(palabras)
# print(mi_palabra +'\n', Fore.RED + '_ ' * len(mi_palabra))