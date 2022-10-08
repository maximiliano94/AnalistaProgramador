Algoritmo Divisores
	// Escriba un programa que entregue todos los divisores del número entero ingresado:
	// ej:
	// Ingrese numero: 200
	// 1 2 4 5 8 10 20 25 40 50 100 200
	Definir i,_numero Como Entero
	Escribir 'ingrese un numero'
	Leer _numero
	Para i<-1 Hasta _numero Hacer
		Si (_numero MOD i=0) Entonces
			Escribir '','  ',i Sin Saltar
		FinSi
	FinPara
FinAlgoritmo
