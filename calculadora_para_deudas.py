# 1. Definimos las variables iniciales 

saldo_deuda_actual = 6400000
meses = 0

print("--- Simulador de Pagos ---")
print(f"Deuda inicial: ${saldo_deuda_actual}")

# 2. Iniciamos el ciclo while.
# La traducción literal es: "Mientras la deuda sea mayor a 0, repite lo siguiente:"
while saldo_deuda_actual > 0: 
    meses += 1 # Esto es lo mismo que escribir: meses = meses + 1 

    abono_texto = input(f"Mes {meses} | Cuanto deseas abonar: ")
    abono = int(abono_texto)

    # Restamos el abono a la deuda actual
    # "deuda -= abono" es el atajo para "deuda = deuda - abono"

    saldo_deuda_actual = saldo_deuda_actual - abono

    # 3. Condicional de seguridad: Evitamos que la deuda quede en números negativos
    # Si el cliente paga de más, simplemente ajustamos la deuda a cero.

    if saldo_deuda_actual < 0:
        saldo_deuda_actual = 0

    print(f"Deuda restante: ${saldo_deuda_actual}\n")

    # 4. Imprimimos el mensaje final de éxito
print("🎉 ¡Felicidades! Has liquidado tu obligación financiera.")
print(f"⏳ Tiempo total: {meses} meses.")