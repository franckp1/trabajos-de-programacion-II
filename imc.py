import math


print("para calcular el indice de masa corporal digite los siguientes parametros: \n")
print("1 altura: ")
while True:
	try:
		franck=float(input("altura (M): \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

print("2 Peso corporal: ")
while True:
	try:
		perez=float(input("peso (Kg): \n "))
		break

	except ValueError:
		print("digite un valor valido \n")
icm=(perez/(franck*franck))
print("su imc es :  \n",imc)


