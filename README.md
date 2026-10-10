# The Hidden Number / El Número Oculto

A Python guessing game where the computer generates a random number and the player tries to guess it.

Un juego de adivinanzas en Python donde la computadora genera un número aleatorio y el jugador intenta adivinarlo.

## Features / Funcionalidades

- Random number generation with `random.randint()` / Generación de número aleatorio con `random.randint()`
- Custom range (lower and upper limits) / Rango personalizado (límite inferior y superior)
- Input validation with `try/except` for non-numeric values / Validación de entrada con `try/except` para valores no numéricos
- Validation that the lower limit is less than the upper limit / Validación de que el límite inferior sea menor que el superior
- Attempt counter / Contador de intentos
- Session history (all attempted numbers) / Historial de sesión (todos los números intentados)
- **Menu-driven interface** (Play / Exit) / **Interfaz con menú** (Jugar / Salir)
- **Modular code with functions** for reusability / **Código modular con funciones** para reutilización
- Hints: "the number is higher" or "lower" / Pistas: "el número es mayor" o "menor"


## Requirements / Requisitos

Python 3

## What I Learned / Lo que Aprendí


- Using random.randint() to generate random numbers / Usar random.randint() para generar números aleatorios

- Validating user input with try/except / Validar entradas del usuario con try/except

- Using while loops for game logic / Usar bucles while para la lógica del juego

- Storing data in lists / Guardar datos en listas

- Refactoring code into functions for better organization / Refactorizar código en funciones para mejor organización

- Creating reusable helper functions (pedir_numero, pedir_opcion) / Crear funciones auxiliares reutilizables

- Using a main() function to control the program flow / Usar una función main() para controlar el flujo del programa


## Author / Autor
[dferreiro96]

## How to Run / Cómo Ejecutar

```bash
python adivinar_numero.py