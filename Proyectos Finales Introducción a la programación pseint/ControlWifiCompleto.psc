Algoritmo ControlWifiCompleto
    Definir mac, ip Como Cadena
    Definir dispositivos, ips Como Cadena
    Definir conexiones Como Entero
    Dimension dispositivos[100], ips[100]
    conexiones <- 0
    
    Escribir "MAC: "; Leer mac
    Escribir "IP: "; Leer ip
    
    Si ValidarAcceso(mac, ip, dispositivos, ips, conexiones) Entonces
        Escribir "Acceso PERMITIDO"
    Sino
        Escribir "ALERTA: Acceso denegado"
    FinSi
FinAlgoritmo

Funcion resultado <- ValidarAcceso(mac, ip, dispositivos, ips, conexiones Por Referencia)
    Definir i, max Como Entero
    max <- 5
    resultado <- Falso
    
    Si conexiones < max Entonces
        Para i <- 0 Hasta conexiones-1 Hacer
            Si dispositivos[i] = mac Entonces
                resultado <- Verdadero
            FinSi
        FinPara
        Si NO resultado Entonces
            dispositivos[conexiones] <- mac
            ips[conexiones] <- ip
            conexiones <- conexiones + 1
            resultado <- Verdadero
        FinSi
    FinSi
FinFuncion