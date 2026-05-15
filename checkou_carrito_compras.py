carrito = [
    {"producto": "Bodies", "precio": 39900, "cantidad": 3},
    {"producto": "Medias", "precio": 6900, "cantidad": 5},
    {"producto": "Baberos", "precio": 5000, "cantidad": 3}
]

print("--- Resumen de tu Pedido ---")

total_a_pagar = 0
for item in carrito:
    subtotal = item["precio"] * item["cantidad"]
    
    print(f"{item['producto']} x {item['cantidad']} = Subtotal: ${subtotal}")

    total_a_pagar = total_a_pagar + subtotal

print("----------------------------")
print(f"Total final a pagar: ${total_a_pagar}")