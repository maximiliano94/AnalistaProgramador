Algoritmo Division
	// Escriba un programa que pida dos n�meros enteros y que calcule la divisi�n, indicando si la divisi�n es exacta o no.
	Definir divisor,dividendo Como Entero
	Definir cociente,resto Como Real
	Escribir 'ingrese el dividendo'
	Leer dividendo
	Escribir 'ingrese el divisor'
	Leer divisor
	cociente <- dividendo/divisor
	Si dividendo MOD divisor<>0 Entonces
		resto <- dividendo MOD divisor
		aux <- trunc(cociente)
		Escribir ' la division no es exacta '
		Escribir 'cociente es :',aux
		Escribir 'resto : es',' ',resto
	SiNo
		resto <- dividendo MOD divisor
		aux <- trunc(cociente)
		Escribir 'la division es exacta'
		Escribir 'cociente es ;',' ',cociente
		Escribir 'el resto es :',resto
	FinSi
FinAlgoritmo
