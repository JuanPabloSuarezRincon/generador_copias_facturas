# login.py
import tkinter as tk
from tkinter import ttk, messagebox
from generador_copias_facturas.facturas import interfaz_principal

def verificar_credenciales():
    identificacion = identificacion_entry.get()
    contrasena = contrasena_entry.get()

    if not identificacion or not contrasena:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    usuarios = {"1010568794": "Procesos1"}

    if identificacion in usuarios and usuarios[identificacion] == contrasena:
        ventana_login.destroy()  # Cierra la ventana de inicio de sesión
        import interfaz_principal  # Abre la ventana principal
    else:
        messagebox.showerror("Error", "Credenciales incorrectas.")

ventana_login = tk.Tk()
ventana_login.title("Iniciar Sesión")

# Estilo ttk
style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 10))
style.configure("TLabel", padding=5, font=("Arial", 10))
style.configure("TEntry", padding=5, font=("Arial", 10))

# Campos de entrada
ttk.Label(ventana_login, text="Tipo:").grid(row=0, column=0, padx=10, pady=10)
tipo_documento = ttk.Combobox(ventana_login, values=["Cédula de Ciudadanía"])
tipo_documento.grid(row=0, column=1, padx=10, pady=10)
tipo_documento.current(0)  # Establece el valor predeterminado

ttk.Label(ventana_login, text="No. Identificación:").grid(row=1, column=0, padx=10, pady=10)
identificacion_entry = ttk.Entry(ventana_login)
identificacion_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(ventana_login, text="Contraseña:").grid(row=2, column=0, padx=10, pady=10)
contrasena_entry = ttk.Entry(ventana_login, show="*")  # Oculta la contraseña
contrasena_entry.grid(row=2, column=1, padx=10, pady=10)

# Botones
ttk.Button(ventana_login, text="Ingresar", command=verificar_credenciales).grid(row=3, column=0, columnspan=2, pady=20)
ttk.Button(ventana_login, text="Cerrar", command=ventana_login.destroy).grid(row=4, column=0, columnspan=2, pady=10)

ventana_login.mainloop()