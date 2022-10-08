Algoritmo Hexagono
	Definir lado,lado2,contador,resta,LargoCadena,salto Como Entero
	Definir espacios,mensaje,astericos Como Caracter
	// incializar variables
	salto <- 0
	LargoCadena <- 0
	contador <- 0
	espacios <- ''
	astericos <- ''
	Escribir 'ingrese lado '
	Leer lado
	// variable auxiliar para la continuacion del hexagono
	lado2 <- lado
	// primeros asteriscos
	Mientras contador<lado Hacer
		astericos <- astericos+'*'
		espacios <- espacios+' '
		contador <- contador+1
	FinMientras
	Repetir
		mensaje <- Concatenar(espacios,astericos)
		LargoCadena <- Longitud(mensaje)
		mensaje <- Subcadena(mensaje,salto,LargoCadena)
		Escribir mensaje
		astericos <- astericos+'**'
		salto <- salto+1
		lado <- lado-1
	Hasta Que lado==0
	// continua
	contador <- 0
	resta <- 5
	Mientras contador<(lado2-1) Hacer
		Escribir (mensaje)
		mensaje <- ' '+mensaje
		mensaje <- Subcadena(mensaje,0,Longitud(mensaje)-3)
		contador <- contador+1
	FinMientras
FinAlgoritmo
