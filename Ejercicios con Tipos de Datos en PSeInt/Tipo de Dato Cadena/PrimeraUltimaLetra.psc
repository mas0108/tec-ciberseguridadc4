Algoritmo PrimeraUltimaLetra
    Definir palabra Como Cadena
    Definir primeraLetra, ultimaLetra Como Caracter
    
    Escribir "Ingrese una palabra: "
    Leer palabra
    
    Si Longitud(palabra) > 0 Entonces
        primeraLetra <- Subcadena(palabra, 0, 1)
        ultimaLetra <- Subcadena(palabra, Longitud(palabra)-1, Longitud(palabra))
        
        Escribir "Palabra: ", palabra
        Escribir "Primera letra: ", primeraLetra
        Escribir "Última letra: ", ultimaLetra
    Sino
        Escribir "Error: No se ingresó ninguna palabra"
    FinSi
FinAlgoritmo