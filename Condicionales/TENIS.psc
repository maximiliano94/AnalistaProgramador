Algoritmo settenis
	// El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular,
	// no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.
	// Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe 
	// haber ganado por lo menos dos juegos
	// más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que 
	// llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último 
	// juego, en cuyo caso el resultado final es 7-6.
	// Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:
	// si A ganó el set, o
	// si B ganó el set, o
	// si el set todavía no termina, o
	// si el resultado es inválido (por ejemplo, 8-6 o 7-3).
	// Desarrolle un programa que solucione el problema de Solarrabietas
	Definir jugadorA,jugadorB Como Entero
	Definir Mensaje1,Mensaje2,Mensaje3,Mensaje4 Como Caracter
	Definir contadorSet Como Entero
	Mensaje1 <- 'El set no termina'
	Mensaje2 <- 'Gano  B  el set'
	Mensaje3 <- 'Gane A el set'
	Mensaje4 <- 'el resultado  del patido es invalido '
	contadorSet <- 1
	Repetir
		Escribir 'juegos ganados por A',' ','set',' ',contadorSet
		Leer jugadorA
		Escribir 'juegos ganados por B',' ','set',' ',contadorSet
		Leer jugadorB
		contadorSet <- contadorSet+1
		Si jugadorA<=0 O jugadorB<0 Entonces
			Escribir ' el valor no puede ser negativo'
		FinSi
		Si ((jugadorA<6) Y (jugadorB<6)) Entonces
			Escribir Mensaje1
		SiNo
			Si ((jugadorA>7) O (jugadorB>7)) Entonces
				Escribir Mensaje4
			SiNo
				Si (((jugadorA>=7) Y (jugadorB>=7)) O ((jugadorB>=7) Y (jugadorA<5)) O ((jugadorA>=7) Y (jugadorB<5))) Entonces
					Escribir Mensaje4
				SiNo
					Si ((jugadorB>jugadorA) Y ((jugadorB-jugadorA)>=2)) Entonces
						Escribir Mensaje3
					SiNo
						Si ((jugadorA>jugadorB) Y ((jugadorA-jugadorB)>=2)) Entonces
							Escribir Mensaje2
						SiNo
							Escribir Mensaje1
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	Hasta Que contadorSet=6
FinAlgoritmo
