Algoritmo ordenamiento
	// Escriba un programa que reciba como entrada dos números,
	// y los muestre ordenados de menor a mayor:
	Definir num1,num2 Como Entero
	contador <- 0
	Escribir 'ingrese el numero 1'
	Leer num1
	Escribir 'ingrese numero 2'
	Leer num2
	Si num1>num2 Entonces
		contador <- num2-num1
		Escribir num2
		Escribir num1
	SiNo
		Escribir 'no has ingresado ningun dato '
	FinSi
FinAlgoritmo
