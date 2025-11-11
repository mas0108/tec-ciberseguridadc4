Algoritmo ValorAbsoluto
    Definir numero, absoluto Como Real
    
    Escribir "Ingrese un número real: "
    Leer numero
    
    Si numero >= 0 Entonces
        absoluto <- numero
    Sino
        absoluto <- numero * (-1)
    FinSi
    
    Escribir "El valor absoluto de ", numero, " es: ", absoluto
FinAlgoritmo