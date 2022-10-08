Algoritmo MultiplicarV2
	// Escriba un programa que muestre una tabla de multiplicar como la siguiente:
	// 1   2   3   4   5   6   7   8   9  10
	// 2   4   6   8  10  12  14  16  18  20//
	// 3   6   9  12  15  18  21  24  27  30
	// 4   8  12  16  20  24  28  32  36  40
	// 5  10  15  20  25  30  35  40  45  50
	// 6  12  18  24  30  36  42  48  54  60
	// 7  14  21  28  35  42  49  56  63  70
	// 8  16  24  32  40  48  56  64  72  80
	// 9  18  27  36  45  54  63  72  81  90
	// 10  20  30  40  50  60  70  80  90 100
	// Los números deben estar alineados a la derecha.
	Definir i Como Entero
	Para i<-1 Hasta 10 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 10)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-2 Hasta 20 Con Paso 2 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 20)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-3 Hasta 30 Con Paso 3 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 30)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-4 Hasta 40 Con Paso 4 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 40)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-5 Hasta 50 Con Paso 5 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 50)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-6 Hasta 60 Con Paso 6 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 60)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-7 Hasta 70 Con Paso 7 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 70)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-8 Hasta 80 Con Paso 8 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 80)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-9 Hasta 90 Con Paso 9 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 90)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
	Para i<-10 Hasta 100 Con Paso 10 Hacer
		Escribir '','  ',i Sin Saltar
		Si (i MOD 100)==0 Entonces
			Escribir ' '
		FinSi
	FinPara
FinAlgoritmo
