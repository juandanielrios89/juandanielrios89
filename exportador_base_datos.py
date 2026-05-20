
#1. Creo lista de clientes vip y la guardo en un archivo de texto
clientes_vip = ["juan.rios@email.com", 
    "maria.gomez@email.com", 
    "carlos.dev@email.com"]

print("--- Iniciando Exportación ---")

with open('clientes_vip.txt', 'w') as file: #"w" significa Write (Escribir).
    for cliente in clientes_vip:
        file.write(cliente + '\n')

print("✅ Archivo 'clientes_vip.txt' guardado exitosamente en tu disco duro.")

print("\n--- Leyendo el Archivo desde el Disco Duro ---")

with open('clientes_vip.txt', 'r') as file: #"r" significa Read (Leer).
    clientes_vip = file.read()

print(clientes_vip)