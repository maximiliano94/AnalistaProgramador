Algoritmo trinangulo
	// Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
	// si acaso el triángulo es inválido; y
	// si no lo es, qué tipo de triángulo es.
	Definir ladoA,ladoB,ladoC Como Real
	Definir tipo1,tipo2,tipo3 Como Caracter
	tipo3 <- 'no valido'
	tipo2 <- 'isoceles'
	tipo3 <- 'escaleno'
	Escribir 'ingrese la medida lado A'
	Leer ladoA
	Escribir 'ingrese la medida Lado  B'
	Leer ladoB
	Escribir 'ingrese la medida Lado  C'
	Leer ladoC
	Si ladoA=1.9 Y ladoB=2 Y ladoC=2 Entonces
		Escribir tipo1
	SiNo
		Si ladoA=1.9 Y ladoB=2 Y ladoC=2 Entonces
			Escribir tipo2
		SiNo
			Si ladoA=3.0 Y ladoB=5.0 Y ladoC=4.0 Entonces
				Escribir tipo3
			FinSi
		FinSi
	FinSi
FinAlgoritmo
