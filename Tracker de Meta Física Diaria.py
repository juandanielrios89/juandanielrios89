# 1. Crea una variable llamada meta_diaria y asígnale el valor 50
meta_diaria = 50

# 2. Pregunta al usuario: "¿Cuántas flexiones hiciste hoy?" y conviértelo a entero (int)
flexiones_hoy_texto = input("cuantas flexiones hiciste hoy? ")
flexiones_hoy = int(flexiones_hoy_texto) # Convertimos el texto a un número entero usando int()

# 3. Crea un condicional IF para evaluar si las flexiones hechas son mayores o iguales a la meta
if flexiones_hoy >= meta_diaria:
    # a. Si es verdad, imprime un mensaje de éxito (ej: "¡Excelente! Meta cumplida.")
    print("¡Excelente! Eres un ganador")

# 4. Usa un ELSE para el caso en que no se haya cumplido la meta
else: 
    # a. Dentro del else, crea una variable (ej: faltantes) que reste la meta menos las hechas
    faltantes = meta_diaria - flexiones_hoy
    
    # b. Imprime un mensaje diciendo cuántas faltan (ej: "Aún te faltan X flexiones. ¡Tú puedes!")
    print(f"Aún te faltan {faltantes} flexiones. ¡Tú puedes!")