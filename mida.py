def med(valores):
	return sum(valores)/len(valores)

print("a continuación inserte 3 numero para calcular la media aritmetica\n")
while True:
	try:
		franck=int(input("ingrese un numero: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		perez=int(input("ingrese un numero: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")

while True:
	try:
		c=int(input("ingrese un numero: \n "))
		break

	except ValueError:
		print("digite un valor valido \n")


print("la media aritmetica es : \n")
print(med((franck,perez,c)))
