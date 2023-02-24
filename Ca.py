import math


print("Inserte el radio de la circunferencia :\n")
while True :
	try :
		franck=float(input("Radio de la circunferencia (Grados°)  \n"))
		break
	except ValueError: 
		print("Digite un valor valido \n")
pi=3.1416
A=(pi*(franck*franck))
L=(2*pi*franck)
print("El area del circulo es: ",A)
print("El perimetro del la circunferencia es :",L)		