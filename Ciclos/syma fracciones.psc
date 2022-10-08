Algoritmo sin_titulo
	Definir n,f,suma,contador,resultado Como Real
	contador <- 1
	suma <- 0
	n <- 2
	f <- 0.000001
	resultado <- 1
	Escribir 'Potencia Fracción Suma'
	Mientras resultado>f Hacer
		resultado <- (1/n)
		suma <- suma+resultado
		Escribir contador,' ',resultado,' ',suma
		n <- 2^(contador+1)
		contador <- contador+1
		Esperar Tecla
	FinMientras
FinAlgoritmo
