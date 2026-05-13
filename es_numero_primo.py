''' * Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100'''

#for i in range(1, 101):
#    if i > 1:  # Los números primos son mayores que 1
#        for j in range(2, int(i**0.5) + 1):  # Verificar divisibilidad hasta la raíz cuadrada de i
#            if i % j == 0:  # Si i es divisible por j, no es primo
#                break
#        else:  # Si no se encontró ningún divisor, es primo
#            print(i)

for i in range(1, 101):
   if i > 1: 
      for j in range(2, int(i**0.5) + 1):
         if i % j == 0:
            break
      else:
            print(i) 