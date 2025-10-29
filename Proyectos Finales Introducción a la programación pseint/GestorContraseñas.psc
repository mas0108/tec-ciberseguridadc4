Algoritmo GestorContraseñas
	Definir user, pass Como Caracter
	Dimension user[10], pass[10]
	
	Registrar("admin", "Abc123!")
	Registrar("user1", "123456")
	Registrar("ana", "Pass2024$")
FinAlgoritmo

SubProceso Registrar(u, p)
	Escribir "Usuario: ", u
	Si Verificar(p) Entonces
		Escribir "Contraseña: SEGURA"
	Sino
		Escribir "Contraseña: DÉBIL - ALERTA!"
	FinSi
FinSubProceso


Funcion seguro <- Verificar(p)
	seguro <- Verdadero
	Si Longitud(p) < 6 Entonces
		seguro <- Falso
	FinSi
FinFuncion


