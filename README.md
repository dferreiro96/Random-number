# Random Number Guessing Game

A simple console game built in Python where the program generates a random number between two limits you choose, and you have to guess it.

## How it works

1. You enter a lower and an upper limit.
2. The program generates a random number in that range.
3. You try to guess it, and the program tells you if the number is higher or lower.
4. When you guess correctly, it shows how many attempts you needed and the list of all numbers you tried.

## Features

- Input validation (only accepts numbers).
- Ensures the lower limit is smaller than the upper limit.
- Shows hints (higher/lower) after each attempt.
- Keeps a list of every number you guessed during the session.
- Option to play again or exit.

## Requirements

- Python 3.x

## How to run

    python "numero aleatorio mejorado.py"

## Example

    Introduzca el primer número: 1
    Introduzca el segundo número: 100
    Bien, ahora introduzca un número entre 1 y 100: 50
    El numero es MENOR. Introduzca otro: 25
    El numero es MAYOR. Introduzca otro: 37
    FELICIDADES. El número es 37. Lo logró en 3 intentos.

## Author

Daniel Ferreiro