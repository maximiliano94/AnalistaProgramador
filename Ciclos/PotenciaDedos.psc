Algoritmo PotenciaDedos
	// Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
	Definir _numero,potencia Como Entero
	acumulador <- 0
	Escribir 'ingrese el nummero'
	Leer _numero
	Para i<-1 Hasta _numero Hacer
		Escribir Sin Saltar 'POTENCIA','   ',i
		Si i=1 Entonces
			acumulador <- 1
		SiNo
			acumulador <- acumulador*2
		FinSi
		potencia <- acumulador
		Escribir Sin Saltar'valor de potencia','  ',potencia
		Escribir ''
	FinPara
	Escribir 'valor del acumulador ',acumulador
FinAlgoritmo
