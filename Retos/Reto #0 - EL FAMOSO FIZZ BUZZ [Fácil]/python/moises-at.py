"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
  for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
      print("fizzbuzz")
    elif x % 3 == 0:
      print("fizz")
    elif x % 5 == 0:
      print("buzz")
    else:
      print(x)

if __name__ == "__main__" :
    fizzbuzz()
    
    