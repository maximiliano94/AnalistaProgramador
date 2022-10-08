Algoritmo LetraONumero
	// Escriba un programa que determine si un caracter
	// ingresado es letra, número, o ninguno de los dos. En caso que sea 
	// letra, determine si es mayúscula o minúscula.
	Definir letra Como Caracter
	Escribir 'ingrese un caracter'
	Leer letra
	Si letra>='0' Y letra<='9' Entonces
		Escribir 'el  caracter es un numero',' ',letra
	SiNo
		Si letra>='a' Y letra<='z' Entonces
			Escribir 'el  caracter es Minusculas',' ',letra
		SiNo
			Si letra>='A' Y letra<='Z' Entonces
				Escribir 'el  caracter es Mayusculas',' ',letra
			SiNo
				Escribir 'no es ni letra ni numero'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
