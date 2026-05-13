# 1. Definimos los precios base de nuestro e-commerce

precio_paquete = 50000
costo_envio_base = 13000

# 2. Pedimos al usuario la cantidad y la convertimos a un número entero (int)

cantidad_texto = input("ingrese la cantidad de paquetes que desea comprar: ")
cantidad = int(cantidad_texto) # Convertimos el texto a un número entero usando int()

# 3. Calculamos el subtotal (precio sin ningún descuento)
subtotal = precio_paquete * cantidad 

# 4. Lógica de descuentos usando condicionales (if, elif, else)
if cantidad >= 3 and cantidad <= 4:
    descuento = subtotal * 0.10  # 10% de descuento
    texto_descuento = "10%"

elif cantidad >= 5:
    descuento = subtotal * 0.20  # 20% de descuento
    texto_descuento = "20%"
else:
    descuento = 0.0   # Sin descuento
    texto_descuento = "Sin descuento"

# Calculamos cuánto vale la ropa aplicando la rebaja
precio_con_descuento = subtotal - descuento

# 5. Lógica del costo de envío
# la regla dice que el envío gratis depende del precio DESPUÉS de descuentos

costo_envio_nacional = costo_envio_base
if precio_con_descuento >= 150000: 
    costo_envio_nacional = 0.0  # Envío gratis
    texto_envio = "Totalmente Gratis"
else: 
    texto_envio = f"${costo_envio_nacional}"

#6 . Calculamos el total a pagar sumando el precio con descuento y el costo de envío
total_a_pagar = precio_con_descuento + costo_envio_nacional

# 7. Imprimimos el resultado final al usuario
print("\n--- Resumen de tu compra ---")
print(f"subtotal: ${int(subtotal)}")
print(f"descuento aplicado: {texto_descuento} (${int(descuento)})")
print(f"costo de envío: {texto_envio}")
print(f"total a pagar: ${int(total_a_pagar)}")