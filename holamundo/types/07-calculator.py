n1 = input("Agrega un numero: ")
n2 = input("Agrega otro numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multi es {multi}.
El resultado de la div es {div}.
"""

print(mensaje)
