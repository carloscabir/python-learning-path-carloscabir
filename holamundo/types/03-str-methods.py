animal = "  chancHIto feliz"

# Upper case
print(animal.upper())
# Lower case
print(animal.lower())
# Convertir el primer indice a mayuscula y el resto a minuscula
print(animal.strip().capitalize())
# Convertir a un titulo un str
print(animal.title())

# Remover todos los espacios en blanco al rededor del str -un trim en JS-
print(animal.strip())
# Strip left
print(animal.lstrip())
# Strip right
print(animal.rstrip())

# Buscar un caracter
# Si lo encuentra mostrara su indice si no devolvera -1
print(animal.find("HI"))
print(animal.find("CHI"))

# Buscar y remplazar
# Lo mismo de arriba
print(animal.replace("feliz", "triste"))

# Buscar y devolver un booleano -conforme a la palabra clave-
print("feliz" in animal)
print("triste" in animal)
print("feliz" not in animal)
print("triste" not in animal)

if "feliz" in animal:
    print("el chanchito esta feliz!!!")
