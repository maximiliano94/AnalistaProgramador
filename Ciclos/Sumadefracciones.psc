Algoritmo Sumadefracciones
//Desarrolle un programa que permita trabajar 
//con las potencias fraccionales de dos, es decir:
//12,14,18,116,132,164,?
//en forma decimal:
//0.5,0.25,0.125,0.0625,0.03125,0.015625,?
//El programa debe mostrar tres columnas 
//que contengan la siguiente información:
	
//	Potencia  Fraccion  Suma
//1         0.5       0.5
//2         0.25      0.75
//3         0.125     0.875
//4         0.0625    0.9375
//...       ...       ...
	
	Definir decimal Como real

	Definir  acumuladorPotencia Como Entero
	Definir  espacio Como Caracter
	contadorPotencia=1
	acumdecimal=acumdecimal+decimal
	Repetir
		Escribir "ingrese  la potencia ", contadorPotencia
		Leer  decimal
		contadorPotencia=contadorPotencia+1
		
	Hasta Que decimal<=0.000001
	

	 Para i=1 Hasta  contadorPotencia Con Paso 1 Hacer
		 escribir  "potencia"  ,"     ","fraccion"  ,"     "
		 Escribir  i,"               ", acumdecimal
	 FinPara
	 
	
        

FinAlgoritmo
