Algoritmo VerificacionesCompletas
    Definir num Como Real
    Definir esPositivo, esPar, estaEnRango Como Logico
    
    Escribir "Ingrese un número: "
    Leer num
    
    esPositivo <- num > 0
    esPar <- (num MOD 2) = 0
    estaEnRango <- num >= 1 Y num <= 100
    
    Escribir "Análisis del número ", num, ":"
    Escribir "- ¿Es positivo? ", esPositivo
    Escribir "- ¿Es par? ", esPar
    Escribir "- ¿Está entre 1 y 100? ", estaEnRango
FinAlgoritmo