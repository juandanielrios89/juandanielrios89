producto = {
    "nombre": "pack de 3 baby bodies",
    "precio": 99000,
    "Stock": 25

}
print("--Ficha del producto--")
print("Nombre: ", producto["nombre"])
print(producto["precio"])
print("Stock: ", producto["Stock"])

producto["Stock"] = producto["Stock"] - 1
print("Stock actualizado: ", producto["Stock"])

producto["color"] = "blanco" 

print("\n--- Base de datos actualizada ---")
print(producto)

producto["Descuento"] = 0.12
producto["Precio con descuento"] = producto["precio"] * (1 - producto["Descuento"])

print("\n--- Base de datos actualizada con descuento ---")
print(producto)