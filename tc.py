import math
print("ingrese los lados del triangulo rectangulo ")
while True :
	try :
		franck=float(input("lado A (Cateto adyacente)  \n"))
		break
	except ValueError: 
		print("digite un valor valido \n")
while True :
	try :
		perez=float(input("Lado B (Cateto opuesto)  \n"))
		break
	except ValueError: 
		print("digite un valor valido \n")		


c=(franck*franck)+(perez*perez)
d=math.sqrt(c)
Area=((franck*perez)/2)		
	
p=franck+perez+d
print("El perimetro del triangulo es :",p)
print("El area del triangulo es : ",Area)		