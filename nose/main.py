# Supongo que el codigo va a hablar solo (debido a sus sintaxis), gracias a mis bases a otros lenguajes o sintaxis, solo en lo necesario haré enfasis en esas partes que muy profundas del lenguaje propio :D



# Hola Mundo ;)
#print('Hola mundo') 



# Concatenaciones
from cmd import PROMPT


# nombre = 'Tai'
# edad = 19

# print('Hola mundo soy ' + nombre  + ' y tengo ' + str(edad) + ' anios')

# texto = 'Hola mundo soy ' + nombre  + ' y tengo ' + str(edad) + ' anios'

# print(texto)



# If
""" nombre = input('Como te llamas?')
print('Hola ' + nombre)

# Cabe a aclarar que el valor que se le asigne a input sera un strT
edad = int(input('Que edad tenes?'))
 """
""" 
if edad > 18: 
  print('Es mayor de edad')
print('Este print se ejecutara independientemente debido a que necesitas hacer tab para que entre en el scope de nuestro condicional')  
 """
""" 
masDe12 = edad >= 12
respuestaHijoDelDuenio = input('Eres hijo del duenio?') 
esHijoDelDuenio = respuestaHijoDelDuenio == 'si' or 'chi'
puedePasar = masDe12 or esHijoDelDuenio


if puedePasar:
  print(puedePasar)
  print('Puedes pasar a la montania rusa ' + nombre + '!') #Tenes que tener codigo con la indentacion del codigo, esto va nuestro bloque de codigo (en este caso nuestro)
else:
  print(puedePasar)
  print('No podes pasar a la montania rusa') """



  # Operadores aritmeticos
  # Los mismos que js dx
""" 
numero = int(input('Ingrese un numero'))

if numero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es inpar') """



  #Funciones (def)

  # Calculadora de IMC
  # IMC = Peso / (Altura * Altura)
  # < 19: delgadez
  # entre 20 y 25: normal
  # entre 26 y 30: sobrepeso
  # > de 30: obesidad
""" 
def calcularIMC(peso, alturaEnM):
    imc = peso / (alturaEnM * alturaEnM)
    return imc # Asi va a sacar nuestra variable del scope


def pedirIMC():
  peso = int(input('Ingresa tu peso en kg'))
  alturaEnCm = int(input('Ingresa tu altura en cm'))
  alturaEnM = alturaEnCm / 100
  imc = calcularIMC(peso, alturaEnM)

  print('Su indice de masa corporal es ' + str(imc))

  if imc < 20:
      print('Estado de delgadez')
  if imc >= 20 and imc < 26:
      print('Peso normal')
  if imc >= 26 and imc < 30:
      print('Peso de sobrepeso')
  if imc >= 30:
      print('Obesidad')

pedirIMC()
pedirIMC()
 """
# El debugging se hace con los breakpoints de VSCODE, y obviamente con debug mode.
""" 

contador = 0
while contador < 5:
  contador += 1
  if contador == 3:
      continue #omitira lo siguente
  print("El valor de contador es: " + str(contador)) """


# EJERCICIO CON EMOJIS xd
""" seguirChat = True
while seguirChat: 
    texto = input(">")
    if texto == "salir":
        seguirChat = False
    texto = texto.replace(":)", "🥵")
    texto = texto.replace(":(", "😿")
    texto = texto.replace(":p", "😸")
    texto = texto.replace("uwu", "🍆")
    print(texto)

#🥵🥱 """




# Arrays & For
""" 
arreglo = ["chanchito", "feliz", "triste", "felipe"]
arreglo.reverse()
arreglo.remove("triste")
arreglo.append("pipi") # Agrega al FINAL de los demas hijos

print(arreglo)

for palabra in arreglo:
    if palabra.endswith("feliz"):
      break #paramos el ciclo cuando se cumpla la condicion
    print("La palabra es: " + palabra) """
""" 
texto = "Hola Mundo"

for letra in texto:
    print(letra)
 """
""" 
for numero in range(3, 10): #Especificacion de rango (minimo y maximo)(final no incluido)
    if (numero > 5):
        print(numero) """




# Diccionarios || Objetos (in JS)

diccionario = {
  "Programar": "Programar es transformar el cafe en codigo",
  "POO": "Programacion Orientada a Objetos",
  "MVC": "Modelo Vista Controlador",
  "SPA": "Single Page Application",
  "DOM": "Document Object Model",
  "API": "Application Programming Interface",
  "REST": "Representational State Transfer"
}

numeros = {
  "0": "cero",
  "1": "uno",
  "2": "dos",
  "3": "tres",
  "4": "cuatro",
  "5": "cinco",
  "6": "seis",
  "7": "siete",
  "8": "ocho",
  "9": "nueve",
  "salir": "salir"
}

""" 
print(diccionario["REST"])  #Para acceder a un indice de manera directa
print(diccionario["SPA"]) """

chat = True

while chat:
    texto = input("Ingrese un numero:") 
    if texto == "salir":
        chat = False

    textoFinal = ""

    for letra in texto:
      textoFinal += numeros[letra] + " "
    
    print(textoFinal)
     
     