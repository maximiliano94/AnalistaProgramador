Algoritmo Tiempodeviaje
	// Un viajero desea saber cu�nto tiempo tom� un viaje que realiz�. 
	// �l tiene la duraci�n en minutos de cada uno de los tramos del viaje.
	// Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y 
	// entregue como resultado el tiempo total de viaje en formato horas:minutos.
	// El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
	
	// Duracion tramo: 15
	// Duracion tramo: 30
	// Duracion tramo: 87
	// Duracion tramo: 0
	// Tiempo total de viaje: 2:12 horas
	Definir acumuladorTiempo,tiempo Como Entero
	acumuladorTiempo <- 0
	Repetir
		Escribir 'duracion del tramo '
		Leer tiempo
		acumuladorTiempo <- acumuladorTiempo+tiempo
	Hasta Que tiempo=0
	Escribir 'tiempo total del viaje',' ',trunc(acumuladorTiempo/60),':',' ',acumuladorTiempo MOD 60
FinAlgoritmo
