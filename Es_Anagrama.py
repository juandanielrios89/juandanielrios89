def es_anagrama(palabra1, palabra2):

    #lower() convertir ambas palabras a minusculas para evitar problemas de mayúsculas y minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if palabra1 == palabra2:
        return False    

    return sorted(palabra1) == sorted(palabra2) 
'''sorted(): Esta es la "magia" de la función. En Python, sorted("amor") toma la cadena de texto y 
la convierte en una lista de caracteres ordenados alfabéticamente: ['a', 'm','''   

print(es_anagrama("amor", "roma"))  # True
print(es_anagrama("hola", "adios"))  # False
print(es_anagrama("listen", "silent"))  # True
print(es_anagrama("triangle", "integral"))  # True