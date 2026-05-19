productos_crudos = [
    "  body OsiTo polar  ",
    " set toallas Baño\n",
    "pijama termica  "
]

catalogo_de_skus = []
print("--- Generador de Códigos SKU ---")

for producto in productos_crudos:
    item_limpio = producto.strip().upper()
    catalogo_de_skus.append(item_limpio)
    sku = item_limpio.replace(" ", "-")
    partes = sku.split("-")
    categoria_producto = partes[0]
    
    print(f"✅ SKU Generado: {sku} | Categoría: {categoria_producto}")

    print("\n--- Catálogo de SKUs Listo para Inventario ---")
    print(catalogo_de_skus)