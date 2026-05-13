# 1. Definimos nuestros gastos fijos y porcentajes
gasolina = 12000
porcentaje_comision_app = 0.10
ahorro = 0.20

# 2. Pedimos la cantidad de viajes para saber cuántas vueltas dará el ciclo
cantidad_viajes_texto = input("Ingrese la cantidad de viajes que realizaste: ")
cantidad_viajes = int(cantidad_viajes_texto) # Convertimos el texto a un número entero usando int() 
print("")

# 3. Inicializamos nuestro ACUMULADOR en cero antes de entrar al ciclo
ingreso_bruto = 0

# 4. Usamos un ciclo FOR para repetir el proceso de calcular el ingreso por cada viaje
for i in range(cantidad_viajes):
    numero_viaje = i + 1  # Para mostrar el número del viaje (empezando desde 1)

    # Pedimos el valor de este viaje específico
    valor_viaje_texto = input(f"Ingrese el valor del viaje {numero_viaje}: ")
    valor_viaje = int(valor_viaje_texto) # Convertimos el texto a un número entero usando int()

# ACUMULAMOS: Al total que ya teníamos, le sumamos el valor de este nuevo viaje

    ingreso_bruto = ingreso_bruto + valor_viaje
# --- Al terminar todas las vueltas del ciclo for, el código continúa aquí abajo ---

# 5. Cálculos de descuentos sobre el gran total acumulado
comision_app = ingreso_bruto * porcentaje_comision_app
ganancia_neta = ingreso_bruto - gasolina - comision_app

# 6. Cálculos de distribución del dinero libre
aporte_ahorro = ganancia_neta * ahorro
dinero_libre = ganancia_neta - aporte_ahorro

# 7. Imprimimos el reporte final
print("\n--- Cierre de Turno ---")
print(f"Ingreso Bruto: ${int(ingreso_bruto)}")
print(f"- Comisión App (10%): ${int(comision_app)}")
print(f"- Gasolina: ${int(gasolina)}")
print("-----------------------")
print(f"Ganancia Neta: ${int(ganancia_neta)}\n")

print(f"💰 Aporte a Fondo de Emergencia (20%): ${int(aporte_ahorro)}")
print(f"💵 Disponible para el bolsillo: ${int(dinero_libre)}")
