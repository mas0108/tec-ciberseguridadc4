Algoritmo Sistema_de_Monitoreo_de_Accesos 
	Definir u1,u2,u3,s1,s2,s3 Como Caracter
	Definir cont Como Entero
	
	u1 <- "moises"
	u2 <- "ana" 
	u3 <- "root"
	s1 <- "web"
	s2 <- "db"
	s3 <- "mail"
	cont <- 0
	
	Registrar("moises","web","192.168.1.2","fallido")
	Registrar("moises","web","192.168.1.2","fallido")
	Registrar("moises","web","192.168.1.2","fallido")
	Registrar("ana","db","10.0.0.5","exitoso")
	
	Escribir "Total: ",cont," intentos"
	
FinAlgoritmo

SubProceso Registrar(usuario,servidor,ip,tipo)
	cont <- cont + 1
	Escribir usuario," -> ",servidor," (",tipo,")"
	
	Si tipo = "fallido" Y cont >= 3 Entonces
		Escribir "ALERTA: ",usuario," - 3+ fallos"
	FinSi
FinSubProceso

