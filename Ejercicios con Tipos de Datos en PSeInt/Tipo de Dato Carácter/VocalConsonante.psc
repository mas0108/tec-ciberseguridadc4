Algoritmo VocalConsonante
    Definir letra Como Caracter
    
    Escribir "Ingrese una letra: "
    Leer letra
    
    letra <- Minusculas(letra)  // Convertir a minúscula para simplificar
    
    Si letra = 'a' O letra = 'e' O letra = 'i' O letra = 'o' O letra = 'u' Entonces
        Escribir "La letra ", letra, " es una VOCAL"
    Sino
        Escribir "La letra ", letra, " es una CONSONANTE"
    FinSi
FinAlgoritmo