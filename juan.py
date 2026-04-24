import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatorio: {numero_aleatorio}")

# Generar una lista con 5 números aleatorios
numeros = [random.randint(1, 50) for _ in range(5)]
print(f"Lista de números aleatorios: {numeros}")

# Seleccionar un elemento aleatorio de una lista
frutas = ["manzana", "plátano", "naranja", "fresa", "uva"]
fruta_aleatoria = random.choice(frutas)
print(f"Fruta aleatoria: {fruta_aleatoria}")

# Barajar una lista
cartas = list(range(1, 11))
random.shuffle(cartas)
print(f"Cartas barajadas: {cartas}")
