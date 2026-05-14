hook = input("Escribe el hook de tu proximo video: ")
print("\n--- Analizando tu Copy ---")
print(len(hook))

longitud_hook = len(hook)

if longitud_hook > 50:
    print("⚠️ Cuidado, tu título es muy largo y se puede cortar en pantalla.")
elif longitud_hook <= 50:
    print("✅ Longitud perfecta, directo al grano.")

if "secreto" in hook or "amor" in hook: 
    hook = hook.lower() # Convertimos el hook a minúscula para hacer la comparación sin importar mayúsculas o minúsculas
    print("✅ Excelente, estás usando palabras poderosas que generan curiosidad.")
else:
    print("💡Tip: Considera incluir palabras poderosas como 'Secreto' o 'Amor' para aumentar la curiosidad.")

print(f"\n--- Listo para copiar y pegar ---\n{hook.upper()}")