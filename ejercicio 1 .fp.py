
franck=input(str("ingrese nombre\n ")) 

perez=input(str("ingrese nombre\n "))
 
c=input("ingrese su edad\n")

while c.isdigit() != True:
     print("el dato que ingresó no es un numero")
     c=input("ingrese su edad\n ")

d=input(str("digite su direccion:\n "))

e=(input("digite su numero de telefono \n "))

while e.isdigit() != True:
     print("el dato que ingresó no es un numero")
     e=input("ingrese su numero de telefono\n ")


f=str(input("digite su genero:\n "))


print("\n  \n  \n")

print("su nombre completo es:\n "+(franck+" "+perez))
print("su edad es: "+str(c)+ " años")
print("su direccion: \n "+ d)
print("su numero de telefono es :\n  "+str(e))
print("genero: "+(f))

