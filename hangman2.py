import random
import string
from words import palabras

ahorcado = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

def random_word():
    choice = random.choice(palabras)
    while '-' in choice or ' ' in choice:
        choice = random.choice(palabras)
    return choice

def display_board(word_letters, tries): #Aqui vamos a ejecutar el dibujito del ahorcado
    print(ahorcado[tries])
    print('')
    print(word_letters)

def ejecutar(): # Esta funcion ejecutara la corrida del programa
    word = random_word()
    word_letters = ['-'] * len(word)
    tries = 0

    while True:
        display_board(word_letters, tries) # Mostramos el ahorcado
        print('Tu numero de itentos erroneos es: ', tries)
        user_letter = str(input('Escoge una letra: ')) # Pedimos las letras

        used_letters = []
        for choice in range(len(word)): # Aqui se va a checar si la letra esta entre las letras de la palabra
            if word[choice] == user_letter:
                used_letters.append(choice)
        if len(used_letters) == 0: # En caso de no estar nos arrojara esta alerta 
            tries += 1
            print("Error character")
       
            if tries == 6: # Aqui ponemos el numero de intentos posibles
                display_board(word_letters, tries)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for choice in used_letters: # Aqui se agrega la letra a la lista de letras correctas en caso de atinarle
                word_letters[choice] = user_letter
            used_letters = []

        try:
            word_letters.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':
    print('Que empiece el juego, podras equivocarte solo 6 veces')
    ejecutar()