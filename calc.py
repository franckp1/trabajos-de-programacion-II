import math

print("ingrese dos numero para sumar")
while True:
	try:
		a=int(input("numero 1: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		b=int(input("numero 2 \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

franck = a + b
print("la resultado es: ",franck)
print("\n")

print("ingrese dos numero para restar")
while True:
	try:
		a=int(input("numero 1: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		b=int(input("numero 2 \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
r = a - b
print("la resultado es: ",r)
print("\n")

print("ingrese dos numero para dividir")
while True:
	try:
		a=int(input("numero 1: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		b=int(input("numero 2 \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
perez = a / b
print("la resultado es: ",perez)
print("\n")

print("ingrese dos numero para multiplicar")
while True:
	try:
		a=int(input("numero 1: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		b=int(input("numero 2 \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
m = a * b
print("la resultado es: ",m)
print("\n")

print("inserte una base: ")
while True:
	try:
		a=int(input("Base: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
print("inserte una potencia: ") 
while True:
	try:
		b=int(input("Exponente: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
 
c=pow(a,b)

print("el resultado es: ",c)
print("\n")
 
print("inserte un numero para sacar raiz cuadrada")
while True:
	try:
		a=int(input("Exponente: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
b= (math.sqrt(a))
print("el resultado es:",b)
print("\n")

 
print("inserte un numero como cantidad total")
while True:
	try:
		a=int(input("Inserte un numero: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
print("inserte el porcentaje que quiere calcular (solo numeros)")
while True:
	try:
		b=int(input("porcentaje%: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
c= ((b/100)*a)
print("el resultado es: ",c)
