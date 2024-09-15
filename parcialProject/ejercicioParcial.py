# Entero a cadena
num = 123
num_str = str(num)
print(num_str)  # '123'

# Cadena a entero
num_str = "456"
num = int(num_str)
print(num)  # 456

# Cadena a decimal
num_str = "789.01"
num_float = float(num_str)
print(num_float)  # 789.01

# Decimal a cadena
num_float = 123.45
num_str = str(num_float)
print(num_str)  # '123.45'

multilinea = """Soy estudiante 
de ingenieria de sistemas"""
print(multilinea)

print(len(multilinea))

# Obtener los primeros n caracteres
n = 4
print(multilinea[:n])

# Obtener los caracteres de en medio
inicio = 5
fin = 10
print(multilinea[inicio:fin])

# Obtener los últimos n caracteres
print("Quiubo")
n = 5
print(multilinea[-n:])

print(multilinea.upper())

print(multilinea.lower())

multilinea_caracteres = """Danilo Collo"""
print(multilinea_caracteres)

print(multilinea_caracteres.strip())

print(multilinea_caracteres.replace("Collo", "Medina"))

print(multilinea_caracteres.split(" "))

nombre = "Danilo"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años.")





