meta_calorica = 2900

calorias_consumidas = int(input("¿cuantas calorias has consumido hoy?"))
calorias_restantes = meta_calorica - calorias_consumidas
print(f"Te quedan {calorias_restantes} calorias para alcanzar tu meta diaria de {meta_calorica} calorias.")

if calorias_restantes == meta_calorica:
    print(f"¡Buen trabajo! Has alcanzado tu meta diaria de calorias de {meta_calorica}.")
elif calorias_restantes < 0: 
    print(f"¡Cuidado! Has excedido tu meta diaria de calorias por {-calorias_restantes} calorias.")