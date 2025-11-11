Algoritmo MayusculaMinuscula
    Definir caracter Como Caracter
    
    Escribir "Ingrese un carácter: "
    Leer caracter
    
    Si caracter >= 'A' Y caracter <= 'Z' Entonces
        Escribir "El carácter ", caracter, " es MAYÚSCULA"
    Sino
        Si caracter >= 'a' Y caracter <= 'z' Entonces
            Escribir "El carácter ", caracter, " es MINÚSCULA"
        Sino
            Escribir "El carácter ", caracter, " no es una letra"
        FinSi
    FinSi
FinAlgoritmo