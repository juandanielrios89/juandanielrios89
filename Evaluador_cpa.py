# 1. Crea una variable con tu límite estricto: cpa_maximo = 25000
cpa_maximo = 25000

# 2. Crea una lista VACÍA llamada lista_cpas donde guardaremos los datos. 
# (Recuerda que se usan corchetes cuadrados [])

lista_cpas = []

# 3. Pide al usuario: "¿Cuántos Ad Sets tiene tu campaña?" y conviértelo a número entero (int)

cantidad_de_conjuntos_de_anuncios_texto = input("¿Cuántos Ad Sets tiene tu campaña? ")
cantidad_de_conjuntos_de_anuncios_texto = int(cantidad_de_conjuntos_de_anuncios_texto) # Convertimos el texto a un número entero usando int()   

print("\n--- Registro de Datos ---")
# 4. Crea tu PRIMER CICLO FOR que dé tantas vueltas como la cantidad de Ad Sets
for i in range(cantidad_de_conjuntos_de_anuncios_texto):
    numero_de_ad_set = i + 1 # Calculamos el número del Ad Set actual sumando 1 a i (porque i empieza en 0)
  # a. Dentro del ciclo: pide el CPA de ese Ad Set específico y conviértelo a entero
    cpa_texto = input(f"Ingresa el CPA actual del Ad Set {numero_de_ad_set}: ") 
    cpa = int(cpa_texto) # Convertimos el texto a un número entero usando int()

    lista_cpas.append(cpa) # b. Agrega el CPA a la lista usando append()


print("\n--- Auditoría de la Campaña ---")
# 5. Crea tu SEGUNDO CICLO FOR. Puede ser exactamente igual al primero usando range()
for i in range(cantidad_de_conjuntos_de_anuncios_texto):
    
    # a. Extrae el valor de la lista para evaluarlo. 
    cpa_actual = lista_cpas[i]
    # (Pista: puedes leer la lista usando el índice: cpa_actual = lista_cpas[i])
    
    # b. Usa un condicional IF: Si el cpa_actual es menor o igual al cpa_maximo...
    if cpa_actual <= cpa_maximo:
        print(f"El Ad Set #{i+1} está Rentable 🟢 (CPA: {cpa_actual})")
        # Imprime que el Ad Set está Rentable 🟢
        
    # c. Usa el ELSE (si no se cumplió lo de arriba)...
    else:
        print(f"El Ad Set #{i+1} está dando Pérdida 🔴 (CPA: {cpa_actual})")