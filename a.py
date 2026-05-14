import random

print("--- Simulador de Meta Ads (A/B Testing) ---\n")

ganchos = ["La vida es Bella", "A veces hay que pedir", "El Amor es la solución", "El éxito es tu destino", "El futuro es ahora", "La felicidad es una elección", "El poder de la mente", "El cambio comienza contigo", "La magia está en ti", "El tiempo es oro"]

texto_ganador = random.choice(ganchos)
ctr_potencial = random.randint(1, 10)

print(texto_ganador)
print(f"CTR calculado: {ctr_potencial}")

if ctr_potencial >= 4:
    print("Anuncio Ganador, escalar presupuesto.")
else:
    print("Anuncio Perdedor, probar nuevo gancho.")