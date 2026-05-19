# 1. Base de datos exportada (con errores de tipeo típicos de usuarios)
leads_sucios = [
    "   Juan.Perez@GMAIL.com ",
    "MARIA99@hotmail.com\n", # Ese \n es un salto de línea invisible
    "  carlos_dev@YAHOO.COM  "
]

# 2. Lista donde guardaremos los datos listos para producción
correos_limpios = []

print("--- Iniciando Depuración de Leads ---")

# 3. Recorre la lista de leads_sucios
for lead in leads_sucios:
    
    # a. Limpia el texto: quita espacios a los lados (.strip()) y pásalo a minúsculas (.lower())
    lead_arreglado = lead.strip().lower()
    # Ejemplo: lead_arreglado = lead.strip().lower()
       
    
    # b. Agrega el lead_arreglado a tu lista de correos_limpios
    correos_limpios.append(lead_arreglado)
    
    # c. Usa .split('@') en el lead_arreglado para separar el nombre del dominio.
    # Recuerda que split() te devuelve una lista de 2 posiciones. 
    # El dominio quedará en la posición [1].
    # Ejemplo: partes = lead_arreglado.split('@')
    # dominio = partes[1]

    partes = lead_arreglado.split('@')
    dominio = partes[1]
    
    
    # d. Imprime un mensaje mostrando el resultado
    # Ejemplo: print(f"✅ Guardado: {lead_arreglado} | Proveedor: {dominio}")

    print(f"✅ Guardado: {lead_arreglado} | Proveedor: {dominio}")
    

# 4. Imprime la base de datos final
print("\n--- Base de Datos Lista para Mailing ---")
print(correos_limpios)