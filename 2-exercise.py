""" 
Se le da una cadena s y un entero n. 
Devuelve la longitud de la subcadena más larga en s que contiene como máximo n caracteres distintos.

Por ejemplo, dada la cadena:
aabcdefff y n = 3, entonces la subcadena más larga con 3 caracteres distintos sería defff. 

Ejemplo 2, dada la cadena:
aaabbbbccdddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddeee y n = 3,
entonces la subcadena más larga con 3 caracteres distintos sería dddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddeee. 
"""

string = "aabcdefff"

duplicates = {}
for char in string:
   if char in duplicates:
      duplicates[char] += 1
      print(duplicates)
   else:
      duplicates[char] = 1


for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")

# duplicados ={}
# no_duplicados = {}
# for char in string:
#     if char in duplicados:
#         if duplicados[char] != duplicados[char+1]:
#             duplicados.append(duplicados[char])
#         else:
#             count = 0
#             count=+1
#             if count>3:
#                 print
#             print(duplicados)

