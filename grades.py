import math


print("Digite cuantos grados farenheith: quiere convertir a celsius \n")

while True:
	try:
		franck=float(input("Grados (Fh): \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

C= ((franck-32)/1.8)	
print("en grados celsius son : ",C)

print("\n Digite cuantos grados farenheith: quiere convertir a kelvin \n")
while True:
	try:
		a=float(input("Grados (Fh): \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

perez= (((franck-32)*5/9) + 273.15)
print("en grados kelvin son : ",perez)
print("\n Digite cuantos grados kelvin: quiere convertir a celsius \n")
while True:
	try:
		a=float(input("Grados (K): \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
C= (a-273.15)		
print("en grados celsius son : ",C)