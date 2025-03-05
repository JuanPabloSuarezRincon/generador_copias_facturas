# interfaz_principal.py
import tkinter as tk
from tkinter import ttk

# Importar todos los módulos
from generador_copias_facturas.facturas import generador_facturas_fev
from generador_copias_facturas.facturas import generador_facturas_ncp
from generador_copias_facturas.facturas import generador_facturas_ri
from generador_copias_facturas.facturas import generador_facturas_ci
from generador_copias_facturas.facturas import generador_facturas_cf
from generador_copias_facturas.facturas import generador_facturas_ncv
from generador_copias_facturas.facturas import generador_facturas_nct
from generador_copias_facturas.facturas import generador_facturas_naj
from generador_copias_facturas.facturas import generador_facturas_cp
from generador_copias_facturas.facturas import generador_facturas_rs
def crear_interfaz_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Generador-copias-Facturas")

    # Estilo ttk
    style = ttk.Style()
    style.configure("TButton", padding=5, font=("Arial", 10))
    style.configure("TLabel", padding=5, font=("Arial", 10))

    # Encabezado
    encabezado_label = ttk.Label(ventana_principal, text="Generador de Facturas por servicio para pruebas del aplicativo Apidocker", font=("Arial", 12, "bold"))
    encabezado_label.pack(pady=10)

    # Información del usuario
    frame_usuario = ttk.Frame(ventana_principal)
    frame_usuario.pack(pady=10)

    nombre_label = ttk.Label(frame_usuario, text="Angel Peña", font=("Arial", 10, "bold"))
    nombre_label.pack(side=tk.LEFT, padx=10)

    identificacion_label = ttk.Label(frame_usuario, text="Nit/No. Identificación: 1024482086")
    identificacion_label.pack(side=tk.LEFT, padx=10)

    # Tabla de opciones
    frame_tabla = ttk.Frame(ventana_principal)
    frame_tabla.pack(pady=20)

    opciones = [
        ("Factura Electrónica de Venta", "Esta opción permite la factura Electrónica con su Recibo individual de Prestación de Servicios - RIPS (sin factura)", generador_facturas_fev.main),
        ("Nota Crédito Parcial", "Esta opción permite seleccionar, validar y armar Una Nota Crédito de Capital", generador_facturas_ncp.main),
        ("Recibo Inicial", "Esta opción permite la factura Electrónica con su Recibo inicial de Prestación de Servicios - RIPS (sin factura)", generador_facturas_ri.main),
        ("Capital Inicial", "Seleccionar, validar y armar Un Capital Inicial", generador_facturas_ci.main),
        ("Capital Final", "Seleccionar, validar y armar Un Capital Final", generador_facturas_cf.main),
        ("NC Acuerdo de Voluntades", "Seleccionar, validar y armar Una Nota Crédito de Acuerdo de Voluntades", generador_facturas_ncv.main),
        ("Nota Crédito Total", "Esta opción permite seleccionar, validar y armar Una Nota Crédito de Capital", generador_facturas_nct.main),
        ("Nota de Ajuste", "Esta opción permite seleccionar, validar y armar Una Nota de Ajuste", generador_facturas_naj.main),
        ("Capital por Periodo", "Esta opción permite la factura Electrónica con su Recibo de Capital por Periodo - RIPS (sin factura)", generador_facturas_cp.main),
        ("Rips Sin Factura", "Seleccionar, validar y armar Un Rips Sin Factura", generador_facturas_rs.main)
    ]

    for i, (titulo, descripcion, funcion) in enumerate(opciones):
        frame_opcion = ttk.Frame(frame_tabla, borderwidth=1, relief="solid")
        frame_opcion.grid(row=i // 5, column=i % 5, padx=10, pady=10)

        titulo_label = ttk.Label(frame_opcion, text=titulo, font=("Arial", 10, "bold"))
        titulo_label.pack(pady=5)

        descripcion_label = ttk.Label(frame_opcion, text=descripcion, wraplength=150)
        descripcion_label.pack(pady=5)

        def ejecutar_funcion(f=funcion):
            print(f"Ejecutando función: {f.__name__}")
            try:
                f()
                print(f"Función {f.__name__} ejecutada")
            except Exception as e:
                print(f"Error al ejecutar la función {f.__name__}: {e}")

        boton_opcion = ttk.Button(frame_opcion, text="Abrir", command=ejecutar_funcion)
        boton_opcion.pack(pady=5)

    # Pie de página
    pie_pagina_label = ttk.Label(ventana_principal, text="TEMA DE VALIDACION Y ENVIO DE FEV RIPS (Versión 1.0.0) Ambiente de capacitación y pruebas", font=("Arial", 8))
    pie_pagina_label.pack(pady=10)

    ventana_principal.mainloop()