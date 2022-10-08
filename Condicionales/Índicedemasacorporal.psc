Algoritmo Índicedemasacorporal
	// El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:
	// edad < 45	edad >= 45
	// IMC < 22.0	bajo	medio
	// IMC >= 22.0	medio	alto
	// El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.
	// Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
	Definir Potencia Como Entero
	Potencia <- 2
	// Definición de variables
	Definir IMC Como Real
	Definir Peso Como Real
	Definir Estatura Como Real
	Definir Diagnostico Como Caracter
	// Entrada
	Escribir 'Por favor, digite su peso (en kilogramos): '
	Leer Peso
	Escribir 'Por favor, digite su estatura (en metros): '
	Leer Estatura
	// Proceso
	IMC <- Peso/Estatura^Potencia
	Si (IMC<18.5) Entonces
		Diagnostico <- 'BAJO PESO'
	SiNo
		Si (IMC>=18.5) Y (IMC<25) Entonces
			Diagnostico <- 'PESO IDEAL'
		SiNo
			Si (IMC>=25) Y (IMC<30) Entonces
				Diagnostico <- 'SOBREPESO'
			SiNo
				Si (IMC>=30) Y (IMC<35) Entonces
					Diagnostico <- 'OBESIDAD'
				SiNo
					Si (IMC>=35) Y (IMC<40) Entonces
						Diagnostico <- 'OBESIDAD SEVERA'
					SiNo
						Diagnostico <- 'OBESIDAD MORBIDA'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	// Salida
	Escribir 'Su IMC es: ',IMC,' kg/m²'
	Escribir 'Su diagnóstico es: ',Diagnostico
FinAlgoritmo
