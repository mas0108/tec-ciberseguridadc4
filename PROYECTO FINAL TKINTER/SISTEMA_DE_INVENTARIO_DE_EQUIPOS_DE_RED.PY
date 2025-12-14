import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# ======================================
# CLASE BASE DE DATOS
# ======================================
class BaseDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="monitoreo_accesos"
        )
        self.cursor = self.conexion.cursor()

    def insertar_intento(self, intento):
        sql = """INSERT INTO intentos 
                 (usuario, servidor, ip, tipo, hora)
                 VALUES (%s,%s,%s,%s,%s)"""
        valores = (intento.usuario, intento.servidor,
                   intento.ip, intento.tipo, intento.hora)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def obtener_intentos(self):
        self.cursor.execute("SELECT usuario, servidor, ip, tipo, hora FROM intentos")
        return self.cursor.fetchall()

# ======================================
# CLASE BASE (HERENCIA)
# ======================================
class IntentoAcceso:
    def __init__(self, usuario, servidor, ip, tipo):
        self.usuario = usuario
        self.servidor = servidor
        self.ip = ip
        self.tipo = tipo
        self.hora = datetime.now()

# ======================================
# CLASE HIJA (HERENCIA)
# ======================================
class AlertaAcceso(IntentoAcceso):
    def generar_alerta(self):
        if self.tipo == "Fallido":
            messagebox.showerror(
                "⚠ ALERTA DE SEGURIDAD",
                f"Acceso FALLIDO detectado\nUsuario: {self.usuario}\nIP: {self.ip}"
            )

# ======================================
# CLASE SISTEMA
# ======================================
class SistemaMonitoreo:
    def __init__(self):
        self.bd = BaseDatos()
        self.usuarios = []     # Vector
        self.servidores = []   # Vector
        self.intentos = []     # Matriz

    def registrar_intento(self, intento):
        self.usuarios.append(intento.usuario)
        self.servidores.append(intento.servidor)

        self.intentos.append([
            intento.usuario,
            intento.servidor,
            intento.ip,
            intento.tipo,
            intento.hora
        ])

        self.bd.insertar_intento(intento)
        intento.generar_alerta()

    def obtener_reporte(self):
        return self.bd.obtener_intentos()

# ======================================
# CLASE INTERFAZ GRÁFICA
# ======================================
class InterfazGrafica:
    def __init__(self):
        self.sistema = SistemaMonitoreo()
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Monitoreo de Accesos (POO)")
        self.ventana.geometry("780x520")

        self.crear_componentes()
        self.mostrar_reporte()

        self.ventana.mainloop()

    def crear_componentes(self):
        tk.Label(self.ventana, text="Usuario").grid(row=0, column=0)
        self.usuario_entry = tk.Entry(self.ventana)
        self.usuario_entry.grid(row=0, column=1)

        tk.Label(self.ventana, text="Servidor").grid(row=1, column=0)
        self.servidor_entry = tk.Entry(self.ventana)
        self.servidor_entry.grid(row=1, column=1)

        tk.Label(self.ventana, text="IP").grid(row=2, column=0)
        self.ip_entry = tk.Entry(self.ventana)
        self.ip_entry.grid(row=2, column=1)

        tk.Label(self.ventana, text="Tipo").grid(row=3, column=0)
        self.tipo_var = tk.StringVar(value="Exitoso")
        tk.Radiobutton(self.ventana, text="Exitoso", variable=self.tipo_var,
                       value="Exitoso").grid(row=3, column=1)
        tk.Radiobutton(self.ventana, text="Fallido", variable=self.tipo_var,
                       value="Fallido").grid(row=3, column=2)

        tk.Button(self.ventana, text="Registrar Intento",
                  command=self.registrar).grid(row=4, column=1, pady=10)

        tk.Label(self.ventana, text="Reporte de Accesos").grid(row=5, column=0, pady=10)
        self.texto = tk.Text(self.ventana, width=90, height=15)
        self.texto.grid(row=6, column=0, columnspan=4)

    def registrar(self):
        usuario = self.usuario_entry.get()
        servidor = self.servidor_entry.get()
        ip = self.ip_entry.get()
        tipo = self.tipo_var.get()

        if not usuario or not servidor or not ip:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        intento = AlertaAcceso(usuario, servidor, ip, tipo)
        self.sistema.registrar_intento(intento)

        self.usuario_entry.delete(0, tk.END)
        self.servidor_entry.delete(0, tk.END)
        self.ip_entry.delete(0, tk.END)

        self.mostrar_reporte()

    def mostrar_reporte(self):
        self.texto.delete(1.0, tk.END)
        for r in self.sistema.obtener_reporte():
            self.texto.insert(
                tk.END,
                f"Usuario: {r[0]} | Servidor: {r[1]} | IP: {r[2]} | "
                f"Tipo: {r[3]} | Hora: {r[4]}\n"
            )

# ======================================
# EJECUCIÓN
# ======================================
if __name__ == "__main__":
    InterfazGrafica()
