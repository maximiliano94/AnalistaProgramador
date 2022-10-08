Algoritmo sin_titulo
	Definir n,p,signo,suma,i,resultado Como Real
	suma <- 0
	signo <- -1
	Escribir 'ingrese la cantidad de términos que utilizará la suma'
	Leer n
	Para i<-3 Hasta (2*n)+1 Con Paso 2 Hacer
		resultado <- signo*(1/i) // 1/3  1/5   1/7
		Si suma==0 Entonces
			suma <- 1+resultado // 1 - 1/3 
		SiNo
			suma <- suma+resultado
		FinSi
		signo <- signo*(-1)
	FinPara
	p <- 4*(suma)
	Escribir 'n : ',n
	Escribir p
FinAlgoritmo
