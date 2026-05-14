# 1. Pregunta al usuario: "¿Cuántos packs de ropita quedan en inventario?" y conviértelo a entero (int)
inventario_stock_texto = input("¿Cuántos packs de recien nacido quedan en inventario?")
inventario_stock = int(inventario_stock_texto)

# 2. Usa un condicional IF para evaluar si el stock es MAYOR (>) a 10
if inventario_stock > 10:
    # a. Adentro del if: Imprime "Stock óptimo. ¡Acelerar campañas en Meta Ads! 🚀"
    print("Stock óptimo. ¡Acelerar campañas en Meta Ads! 🚀")

# 3. Usa un ELIF combinando dos condiciones con AND. 
# La lógica es: "Si el stock es mayor o igual a 1 Y ADEMÁS el stock es menor o igual a 10"
# (Pista: elif stock >= 1 and stock <= 10: )
elif inventario_stock >= 1 and inventario_stock <= 10:
    # a. Adentro del elif: Imprime "Stock bajo. Reducir presupuesto de Ads y pedir más mercancía ⚠️"
    print("Stock bajo. Reducir presupuesto de Ads y pedir más mercancía ⚠️")

# 4. Usa un ELSE (que atrapará automáticamente cuando el stock sea 0 o negativo)
else:
    # a. Adentro del else: Imprime "Agotado. ¡Pausar anuncios inmediatamente! 🛑"
    print("Agotado. ¡Pausar anuncios inmediatamente! 🛑")