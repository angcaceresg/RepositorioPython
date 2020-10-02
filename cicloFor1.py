#Crear ciclo for que permita ingrsar 10 numeros. Mostrar cuantos son numeros
#pares y cuantos son numeros impares
par=0
impar=0
for i in range(10):
	nume=int(input("DIGITE UN NUMERO: "))
	if(nume%2==0):
		par=par+1
	else:
		impar=impar+1
print("La cantidad par de numeros pares es:   " + str(par))
print("La cantidad par de numeros impares es: " + str(impar))
