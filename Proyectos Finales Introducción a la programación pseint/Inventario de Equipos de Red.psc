Algoritmo inventario
	Definir eq, ip, ub Como Caracter
	Definir opc, cont Como Entero
	Dimension eq[10], ip[10], ub[10]
	cont <- 0
	
	Repetir
		Escribir "1. Registrar equipo"
		Escribir "2. Mostrar inventario" 
		Escribir "3. Salir"
		Leer opc
		Segun opc Hacer
			1:
				cont <- cont + 1
				Escribir "Nombre:"
				Leer eq[cont]
				Escribir "IP:"
				Leer ip[cont]
				Escribir "Ubicacion:"
				Leer ub[cont]
			2:
				Para i <- 1 Hasta cont Hacer
					Escribir eq[i], " - ", ip[i], " - ", ub[i]
				FinPara
		FinSegun
	Hasta Que opc = 3
FinAlgoritmo
