Algoritmo Escaneo_de_Vulnerabilidades 
	Definir opc, cont, nivel Como Entero
	Dimension host[10], servicio[10], vuln[10]
	cont <- 0
	
	Repetir
		Escribir "1. Registrar"
		Escribir "2. Mostrar"
		Escribir "3. Reporte"
		Escribir "4. Salir"
		Leer opc
		Segun opc Hacer
			1:
				cont <- cont + 1
				Escribir "Host:"
				Leer host[cont]
				Escribir "Servicio:"
				Leer servicio[cont]
				Escribir "Vulnerabilidad: 1.Baja 2.Media 3.Alta"
				Leer nivel
				Segun nivel Hacer
					1: vuln[cont] <- "Baja"
					2: vuln[cont] <- "Media" 
					3: vuln[cont] <- "Alta"
				FinSegun
			2:
				Para i <- 1 Hasta cont Hacer
					Escribir host[i], " - ", servicio[i], " - ", vuln[i]
				FinPara
			3:
				Para i <- 1 Hasta cont Hacer
					Si vuln[i] = "Alta" Entonces
						Escribir "ALERTA: ", host[i], " - RIESGO ALTO"
					FinSi
				FinPara
		FinSegun
	Hasta Que opc = 4
	
FinAlgoritmo
