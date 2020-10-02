#crear menu con 3 opciones
import os
def Numeros():
	#ingresar n numeros donde n es numero ingresado por teclado
	#mostrar cantidad de numeros positivos, negativos y iguales a 0
	pos=0
	neg=0
	cero=0
	cant=int(input("ingrese cantidad de números a ingresar: "))
	for i in range(cant):
		nume=int(input(str(i+1)+" Digite los numeros: "))
		if(nume>0):
			pos=pos+1
		elif(nume<0):
			neg=neg+1
		else:
			cero=cero+1
	print("La cantidad de numeros ingresados es " + str(cant))
	print("La cantidad de numeros positivos es " + str(pos))
	print("La cantidad de numeros negativos es " + str(neg))
	print("La cantidad de numeros igual a cero es " + str(cero))
	print("------------------------------------------------------")
	pausa = input("Digite cualquier tecla para continuar: ")

def Personas():
	#Ingresar para n personas: nombre y edad. Mostrar promedio de todas las edades ingresadas
	suma=0
	cont=0
	can=int(input("Digite la cantidad de edades que desea ingresar: "))
	for i in range(can):
		nom=input(str(i+1) + " Ingrese el nombre: ")
		edad=int(input(str(i+1) + " Ingrese la edad: "))
		suma+=edad
		cont+=1  
	print("EL promedio de las edades es: " + str(suma/cont))
	print("------------------------------------------------------")
	pausa = input("Digite cualquier tecla para continuar: ")


seguir=True
while (seguir):
	os.system('cls')
	print("1. Numeros")
	print("2. Datos personales")
	print("3. Finalizar")
	op=int(input("Digite un numero: "))
	if(op==1):
		Numeros()
	if(op==2):
		Personas()
	if(op==3):
		print("Programa finalizado")
		pausa = input("Digite cualquier tecla para continuar: ")
		break	