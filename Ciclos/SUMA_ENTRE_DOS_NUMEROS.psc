Algoritmo SUMA_ENTRE_DOS_NUMEROS
	// Escriba un programa que pida al usuario dos n�meros enteros, y 
	// luego entregue la suma de 
	// todos los n�meros que est�n entre ellos. Por ejemplo, si los n�meros son
	// 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
	Definir inicial,final,suma Como Entero
	Escribir 'Ingrese valor inicial: '
	Leer inicial
	Escribir 'Ingrese valor final: '
	Leer final
	suma <- 0
	Para i<-inicial Hasta final Hacer
		suma <- suma+i
	FinPara
	Escribir 'La suma es: ',suma
FinAlgoritmo
