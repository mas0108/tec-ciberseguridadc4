Algoritmo sin_titulo
	
	Definir ip Como Cadena
	Definir puerto Como Entero
	
	Escribir "FIREWALL SIMPLE (escriba SALIR para terminar)"
	
	Mientras Verdadero Hacer
		Escribir "IP origen:"
		Leer ip
		
		Si ip = "SALIR" Entonces
			
		FinSi
			
			Escribir "Puerto destino:"
			Leer puerto
			
			Si ip = "192.168.1.100" Entonces
				Escribir "BLOQUEADO: IP en lista negra"
			Sino
				Si puerto = 80 O puerto = 443 O puerto = 22 Entonces
					Escribir "PERMITIDO"
				Sino
					Escribir "BLOQUEADO: puerto no permitido"
				FinSi
			FinSi
			Escribir "----------------------------"
			
	FinMientras
		
FinAlgoritmo
