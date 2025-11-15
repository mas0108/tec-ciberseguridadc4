"""
Sistema de Monitoreo de Accesos

Objetivo: Simular un sistema que registre y analice los intentos de acceso de múltiples 
usuarios a distintos servidores, detectando posibles amenazas y generando reportes.

Bibliotecas utilizadas:
- random: Para generar datos aleatorios en simulaciones
- datetime: Para manejo de fechas y horas
- collections.defaultdict: Para estructuras de datos eficientes
- csv: Para exportar datos a CSV
- json: Para exportar datos a JSON

Autor: [Tu nombre]
Fecha: [Fecha]
"""

import random
import datetime
from collections import defaultdict
import csv
import json

class SistemaMonitoreoAccesos:
    """
    Clase principal que representa el sistema de monitoreo de accesos.
    
    Esta clase gestiona usuarios, servidores, registra intentos de acceso,
    genera alertas y reportes sobre posibles amenazas de seguridad.
    """
    
    def __init__(self):
        """Inicializa el sistema con datos de ejemplo."""
        # Vectores de usuarios y servidores
        self.usuarios = ["admin", "usuario1", "usuario2", "invitado", "root", "test_user"]
        self.servidores = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "10.0.0.5", "servidor_bd"]
        
        # Usando defaultdict para estructuras más eficientes
        self.registros_accesos = defaultdict(list)
        
        # Configuración de alertas
        self.umbral_intentos_fallidos = 3
        self.horas_sospechosas = [0, 1, 2, 3, 4, 5]  # Madrugada
        self.ips_sospechosas = ["192.168.1.200", "10.0.0.100", "unknown_source"]
    
    def registrar_intento(self, usuario, servidor, ip, tipo_acceso, hora=None):
        """
        Registra un intento de acceso en el sistema.
        
        Args:
            usuario (str): Nombre del usuario
            servidor (str): Servidor objetivo
            ip (str): Dirección IP de origen
            tipo_acceso (int): 0=fallido, 1=exitoso
            hora (datetime): Hora del acceso (opcional)
            
        Returns:
            bool: True si se registró correctamente
        """
        if hora is None:
            hora = datetime.datetime.now()
        
        # Validar que usuario existe
        if usuario not in self.usuarios:
            print(f"⚠️ Advertencia: Usuario '{usuario}' no está en la lista de usuarios válidos")
            # Podemos agregarlo o continuar según la política
            self.usuarios.append(usuario)
        
        # Validar que servidor existe
        if servidor not in self.servidores:
            print(f"⚠️ Advertencia: Servidor '{servidor}' no está en la lista de servidores válidos")
            self.servidores.append(servidor)
        
        # Crear registro de acceso
        registro = {
            'usuario': usuario,
            'servidor': servidor,
            'ip': ip,
            'tipo_acceso': tipo_acceso,
            'hora': hora,
            'timestamp': hora.timestamp()
        }
        
        # Almacenar registro
        clave = f"{usuario}_{servidor}"
        self.registros_accesos[clave].append(registro)
        
        print(f"📝 Intento registrado: {usuario} -> {servidor} | IP: {ip} | "
              f"Estado: {'✅ ÉXITO' if tipo_acceso else '❌ FALLIDO'} | "
              f"Hora: {hora.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return True
    
    def generar_alertas(self):
        """
        Genera alertas de seguridad basadas en patrones sospechosos.
        
        Returns:
            list: Lista de mensajes de alerta
        """
        alertas = []
        
        # Análisis por usuario
        for usuario in self.usuarios:
            intentos_usuario = self._obtener_intentos_usuario(usuario)
            
            if not intentos_usuario:
                continue
            
            # Alertas por múltiples intentos fallidos
            intentos_fallidos = sum(1 for intento in intentos_usuario if intento['tipo_acceso'] == 0)
            if intentos_fallidos >= self.umbral_intentos_fallidos:
                alertas.append(f"🚨 ALERTA: Usuario '{usuario}' tiene {intentos_fallidos} intentos fallidos")
            
            # Alertas por horas sospechosas
            accesos_nocturnos = sum(1 for intento in intentos_usuario 
                                  if intento['hora'].hour in self.horas_sospechosas)
            if accesos_nocturnos > 0:
                alertas.append(f"🌙 ALERTA: Usuario '{usuario}' tiene {accesos_nocturnos} accesos en horas sospechosas")
            
            # Alertas por IPs sospechosas
            ips_usuario = set(intento['ip'] for intento in intentos_usuario)
            ips_sospechosas_detectadas = ips_usuario.intersection(set(self.ips_sospechosas))
            if ips_sospechosas_detectadas:
                alertas.append(f"🔍 ALERTA: Usuario '{usuario}' accedió desde IPs sospechosas: {', '.join(ips_sospechosas_detectadas)}")
        
        return alertas
    
    def _obtener_intentos_usuario(self, usuario):
        """Obtiene todos los intentos de un usuario específico."""
        intentos = []
        for clave, registros in self.registros_accesos.items():
            if clave.startswith(usuario + "_"):
                intentos.extend(registros)
        return intentos
    
    def mostrar_reporte(self, usuario=None):
        """
        Muestra un reporte detallado de los accesos.
        
        Args:
            usuario (str, optional): Usuario específico para filtrar
        """
        print("=" * 70)
        print("📊 REPORTE DE ACCESOS - SISTEMA DE MONITOREO")
        print("=" * 70)
        
        if usuario:
            print(f"Filtrando por usuario: {usuario}")
            intentos = self._obtener_intentos_usuario(usuario)
        else:
            # Todos los intentos
            intentos = []
            for registros in self.registros_accesos.values():
                intentos.extend(registros)
        
        if not intentos:
            print("No hay intentos de acceso registrados.")
            return
        
        # Estadísticas generales
        total_intentos = len(intentos)
        exitosos = sum(1 for i in intentos if i['tipo_acceso'] == 1)
        fallidos = total_intentos - exitosos
        usuarios_unicos = set(i['usuario'] for i in intentos)
        servidores_unicos = set(i['servidor'] for i in intentos)
        ips_unicas = set(i['ip'] for i in intentos)
        
        # Calcular porcentajes evitando división por cero
        porcentaje_exitosos = (exitosos / total_intentos * 100) if total_intentos > 0 else 0
        porcentaje_fallidos = (fallidos / total_intentos * 100) if total_intentos > 0 else 0
        
        print(f"\n📈 ESTADÍSTICAS GENERALES:")
        print(f"   • Total intentos: {total_intentos}")
        print(f"   • Accesos exitosos: {exitosos} ({porcentaje_exitosos:.1f}%)")
        print(f"   • Accesos fallidos: {fallidos} ({porcentaje_fallidos:.1f}%)")
        print(f"   • Usuarios activos: {len(usuarios_unicos)}")
        print(f"   • Servidores accedidos: {len(servidores_unicos)}")
        print(f"   • IPs únicas detectadas: {len(ips_unicas)}")
        
        # Reporte por usuario
        print(f"\n👤 ACTIVIDAD POR USUARIO:")
        for usuario_actual in usuarios_unicos:
            intentos_usuario = [i for i in intentos if i['usuario'] == usuario_actual]
            exitosos_usuario = sum(1 for i in intentos_usuario if i['tipo_acceso'] == 1)
            servidores_usuario = set(i['servidor'] for i in intentos_usuario)
            
            print(f"   • {usuario_actual}: {len(intentos_usuario)} intentos "
                  f"({exitosos_usuario} exitosos) en {len(servidores_usuario)} servidores")
    
    def exportar_reportes(self, formato='csv'):
        """
        Exporta los reportes a diferentes formatos.
        
        Args:
            formato (str): 'csv' o 'json'
        """
        if formato == 'csv':
            self._exportar_csv()
        elif formato == 'json':
            self._exportar_json()
        else:
            print(f"Formato {formato} no soportado")
    
    def _exportar_csv(self):
        """Exporta los registros a CSV."""
        filename = f"reporte_accesos_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['usuario', 'servidor', 'ip', 'tipo_acceso', 'hora']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for registros in self.registros_accesos.values():
                    for registro in registros:
                        writer.writerow({
                            'usuario': registro['usuario'],
                            'servidor': registro['servidor'],
                            'ip': registro['ip'],
                            'tipo_acceso': 'Exitoso' if registro['tipo_acceso'] else 'Fallido',
                            'hora': registro['hora'].strftime('%Y-%m-%d %H:%M:%S')
                        })
            
            print(f"✅ Reporte exportado como: {filename}")
        
        except Exception as e:
            print(f"❌ Error al exportar CSV: {e}")
    
    def _exportar_json(self):
        """Exporta los registros a JSON."""
        filename = f"reporte_accesos_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            datos_exportar = []
            for registros in self.registros_accesos.values():
                for registro in registros:
                    datos_exportar.append({
                        'usuario': registro['usuario'],
                        'servidor': registro['servidor'],
                        'ip': registro['ip'],
                        'tipo_acceso': 'Exitoso' if registro['tipo_acceso'] else 'Fallido',
                        'hora': registro['hora'].strftime('%Y-%m-%d %H:%M:%S'),
                        'timestamp': registro['timestamp']
                    })
            
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(datos_exportar, jsonfile, indent=2, ensure_ascii=False)
            
            print(f"✅ Reporte exportado como: {filename}")
        
        except Exception as e:
            print(f"❌ Error al exportar JSON: {e}")
    
    def simular_accesos(self, num_intentos=25):
        """
        Simula intentos de acceso para pruebas.
        
        Args:
            num_intentos (int): Número de intentos a simular
        """
        print(f"🎮 Simulando {num_intentos} intentos de acceso...")
        
        ips_ejemplo = [
            "192.168.1.100", "192.168.1.101", "192.168.1.102",
            "10.0.0.50", "10.0.0.51", "172.16.0.10",
            "192.168.1.200", "10.0.0.100"  # IPs sospechosas
        ]
        
        for i in range(num_intentos):
            usuario = random.choice(self.usuarios)
            servidor = random.choice(self.servidores)
            ip = random.choice(ips_ejemplo)
            
            # Probabilidades: 25% fallidos, 75% exitosos
            tipo_acceso = random.choices([0, 1], weights=[0.25, 0.75])[0]
            
            # Hora aleatoria en los últimos 30 días
            dias_aleatorios = random.randint(0, 30)
            horas_aleatorias = random.randint(0, 23)
            minutos_aleatorios = random.randint(0, 59)
            
            hora_acceso = datetime.datetime.now() - datetime.timedelta(
                days=dias_aleatorios,
                hours=horas_aleatorias,
                minutes=minutos_aleatorios
            )
            
            self.registrar_intento(usuario, servidor, ip, tipo_acceso, hora_acceso)


def main():
    """Función principal para demostrar el sistema."""
    # Crear sistema
    sistema = SistemaMonitoreoAccesos()
    
    # Simular accesos
    sistema.simular_accesos(15)  # Reducido para mejor visualización
    
    # Generar reportes
    sistema.mostrar_reporte()
    
    # Generar alertas
    print("\n" + "=" * 70)
    print("🚨 SISTEMA DE ALERTAS")
    print("=" * 70)
    alertas = sistema.generar_alertas()
    
    if alertas:
        for i, alerta in enumerate(alertas, 1):
            print(f"{i}. {alerta}")
    else:
        print("✅ No se generaron alertas de seguridad.")
    
    # Exportar reportes
    print("\n" + "=" * 70)
    print("💾 EXPORTANDO REPORTES")
    print("=" * 70)
    sistema.exportar_reportes('csv')
    sistema.exportar_reportes('json')
    
    # Reporte específico
    print("\n" + "=" * 70)
    print("👤 REPORTE ESPECÍFICO - USUARIO 'admin'")
    print("=" * 70)
    sistema.mostrar_reporte(usuario='admin')


if __name__ == "__main__":
    main()