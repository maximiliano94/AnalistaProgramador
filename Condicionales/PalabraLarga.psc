Algoritmo PalabraLarga
	// Escriba un programa que pida al usuario dos palabras, 
	// y que indique cuál de ellas es la más larga
	// y por cuántas letras lo es.
	Definir palabra1,palabra2 Como Caracter
	Escribir 'ingrese la palabra 1'
	Leer palabra1
	Escribir 'ingrese la palabra 2'
	Leer palabra2
	largo <- Longitud(palabra1)
	largo2 <- Longitud(palabra2)
	Si largo>largo2 Entonces
		Escribir 'la palabra',palabra1,'tiene',' ',largo2,' ','mas que ',palabra2
	SiNo
		Si largo2>largo Entonces
			aux <- largo-largo2
			pos <- aux*(-1)
			Escribir 'la palabra','  ',palabra2,'  ','tiene',' ',pos,' ','mas que ',palabra1
		SiNo
			Si largo=largo2 Entonces
				Escribir 'las dos palabras tienen el mismo largo '
			FinSi
		FinSi
	FinSi
FinAlgoritmo
