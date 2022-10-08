Algoritmo Calculadora
	// Escriba un programa que simule una calculadora básica, 
	// este puede realizar operación de suma, resta, multiplicación y división.
	// El programa debe recibir como entrada 2 números reales y 
	// un operador, que puede ser +, -, * o /.
	// La salida del programa debe ser el resultado de la operación.
	Definir operador,_nummero1,_numero2 Como Entero
	Escribir 'BIENVENIDOS A LA CALCULADORA'
	Escribir 'PRESIONE CUALQUIER TECLA PARA CONTINUAR'
	Esperar Tecla
	Borrar Pantalla
	Escribir 'ingrese numero 1'
	Leer _nummero1
	Escribir 'ingrese numero 2'
	Leer _numero2
	Escribir 'ingrese la operacion'
	Escribir 'Suma'
	Escribir 'Resta'
	Escribir 'Multiplicacion'
	Escribir 'Division'
	Leer operador
	Segun operador  Hacer
		1:
			suma <- _nummero1+_numero2
			Escribir 'el  resultado de la operacion es',' ',suma
		2:
			resta <- _nummero1-_numero2
			Escribir 'el resultado de la operacion es',' ',resta
		3:
			multiplicacion <- _nummero1*_numero2
			Escribir 'el resultado de la operacion es ',' ',multiplicacion
		4:
			division <- _nummero1/_numero2
			Escribir 'el resultado  de la operacion es',' ',division
		De Otro Modo:
			Escribir 'Error  no  ha ingresado ningun operador'
	FinSegun
FinAlgoritmo
