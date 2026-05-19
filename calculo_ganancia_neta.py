# 1. Creamos nuestra función usando 'def' y le ponemos los 3 parámetros que necesita recibir
# Ejemplo: def mi_funcion(dato1, dato2):
def calcular_ganancia_neta(precio_venta, costo_producto, cpa_ads):
    
    # 2. Adentro de la función (con sangría), crea una variable llamada 'ganancia' 
    # que reste el costo_producto y el cpa_ads al precio_venta
    
    ganancia = precio_venta - costo_producto - cpa_ads

    # 3. Usa la palabra reservada 'return' para devolver el valor de 'ganancia'
    # Ejemplo: return mi_variable
    return ganancia

# --- Aquí termina la función (quitamos la sangría) ---

print("--- Calculadora de Rentabilidad ---")

# 4. Ahora vamos a USAR (llamar) a nuestra función con datos reales.
# Imagina que vendes un pack de ropa a 120000, te costó 50000 y el CPA fue de 25000.
# Llama a tu función pasándole esos 3 números en orden, y guarda el resultado en una variable.
# Ejemplo: resultado1 = mi_funcion(100, 20, 10)
resultado1 = calcular_ganancia_neta(120000, 50000, 25000)

# 5. Imprime el resultado de tu primera prueba
# Ejemplo: print(f"La ganancia de la primera venta fue: ${resultado1}")
print(f"La ganancia neta de la primera venta fue: ${resultado1}")

# 6. Llama a la función OTRA VEZ, pero ahora simulando un escenario donde el CPA se subió muchísimo
# Ejemplo de datos: precio_venta=120000, costo=50000, cpa=65000. 
# Guarda esto en otra variable llamada 'resultado2' e imprímelo.

resultado2 = calcular_ganancia_neta(120000, 50000, 65000)
print(f"La ganancia neta de la segunda venta fue: ${resultado2}")