print("ingrese una cantidad de segundos ")
while True :
	try :
		franck=float(input("segundos (s) \n"))
		break
	except ValueError: 
		print("digite un valor valido \n")
franck=franck
perez=franck/60
h=franck/3600
print("Esos son exactamente :",franck,"segundos",perez,"minutos",h,"horas")
