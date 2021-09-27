import math

# lectura de datos de entrada
g = float(input('Ingresa la constante g: '))
r = int(input('Ingresa el radio del planeta en km: '))

# radio a metros
r = r * 1000

# calcular velocidad de escape
ve = math.sqrt(2 * g * r)

#resultado del programa
print(f"La velocidad de escape es {ve} [m/s]")