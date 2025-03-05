import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from generador_copias_facturas.datos  import generador_datos_nct  # Importación corregida

def seleccionar_ruta(ruta_entry):
    ruta = filedialog.askdirectory()
    ruta_entry.delete(0, tk.END)
    ruta_entry.insert(0, ruta)

def generar_facturas(num_documento_obligado_entry, tipo_nota_entry, num_factura_personalizada_entry, num_facturas_inicio_entry, num_facturas_fin_entry, ruta_entry, edad_min_entry, edad_max_entry, barra_progreso, ventana):
    try:
        num_documento_obligado = num_documento_obligado_entry.get()
        tipo_nota = tipo_nota_entry.get()
        num_factura_personalizada = num_factura_personalizada_entry.get()
        num_facturas_inicio = int(num_facturas_inicio_entry.get())
        num_facturas_fin = int(num_facturas_fin_entry.get())
        ruta = ruta_entry.get()
        edad_min_str = edad_min_entry.get()
        edad_max_str = edad_max_entry.get()

        if edad_min_str and edad_max_str:
            edad_min = int(edad_min_str)
            edad_max = int(edad_max_str)
        else:
            edad_min = 0
            edad_max = 100

        if not os.path.exists(ruta):
            os.makedirs(ruta)

        for i in range(num_facturas_inicio, num_facturas_fin + 1):
            factura = generador_datos_nct.generar_factura(i, num_documento_obligado, tipo_nota, num_factura_personalizada, edad_min, edad_max)  # Llamada corregida
            with open(f"{ruta}/factura_{i}.json", "w", encoding="utf-8") as f:
                json.dump(factura, f, indent=4, ensure_ascii=False)
            barra_progreso['value'] = (i - num_facturas_inicio + 1) / (num_facturas_fin - num_facturas_inicio + 1) * 100
            ventana.update_idletasks()
        messagebox.showinfo("Proceso Completado", f"{num_facturas_fin - num_facturas_inicio + 1} facturas generadas en {ruta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números enteros válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def main():
    ventana = tk.Tk()
    ventana.title("Generador de Facturas por servicio para pruebas del aplicativo Apidocker")

    # Encabezado
    encabezado_label = ttk.Label(ventana, text="Rips sin Factura (RS)", font=("Arial", 12, "bold"))
    encabezado_label.pack(pady=10)

    # Información del usuario
    frame_usuario = ttk.Frame(ventana)
    frame_usuario.pack(pady=10)
    
    # Campos adicionales
    frame_obligado = ttk.LabelFrame(ventana, text="Obligado")
    frame_obligado.pack(padx=10, pady=10, fill="x")

    num_documento_obligado_label = ttk.Label(frame_obligado, text="Número de documento del obligado:")
    num_documento_obligado_label.pack(side=tk.LEFT, padx=5, pady=5)

    num_documento_obligado_entry = ttk.Entry(frame_obligado)
    num_documento_obligado_entry.pack(side=tk.LEFT, padx=5, pady=5)

    frame_tipo_nota = ttk.LabelFrame(ventana, text="Tipo de Nota")
    frame_tipo_nota.pack(padx=10, pady=10, fill="x")

    tipo_nota_label = ttk.Label(frame_tipo_nota, text="Tipo de nota:")
    tipo_nota_label.pack(side=tk.LEFT, padx=5, pady=5)

    tipo_nota_entry = ttk.Entry(frame_tipo_nota)
    tipo_nota_entry.pack(side=tk.LEFT, padx=5, pady=5)

    frame_num_factura_personalizada = ttk.LabelFrame(ventana, text="Número de Factura Personalizada")
    frame_num_factura_personalizada.pack(padx=10, pady=10, fill="x")

    num_factura_personalizada_label = ttk.Label(frame_num_factura_personalizada, text="Número de factura personalizada:")
    num_factura_personalizada_label.pack(side=tk.LEFT, padx=5, pady=5)

    num_factura_personalizada_entry = ttk.Entry(frame_num_factura_personalizada)
    num_factura_personalizada_entry.pack(side=tk.LEFT, padx=5, pady=5)

    # Rango de facturas
    frame_num_facturas = ttk.LabelFrame(ventana, text="Rango de Facturas")
    frame_num_facturas.pack(padx=10, pady=10, fill="x")

    num_facturas_inicio_label = ttk.Label(frame_num_facturas, text="Número de factura inicial:")
    num_facturas_inicio_label.pack(side=tk.LEFT, padx=5, pady=5)

    num_facturas_inicio_entry = ttk.Entry(frame_num_facturas)
    num_facturas_inicio_entry.pack(side=tk.LEFT, padx=5, pady=5)

    num_facturas_fin_label = ttk.Label(frame_num_facturas, text="Número de factura final:")
    num_facturas_fin_label.pack(side=tk.LEFT, padx=5, pady=5)

    num_facturas_fin_entry = ttk.Entry(frame_num_facturas)
    num_facturas_fin_entry.pack(side=tk.LEFT, padx=5, pady=5)

    # Ruta de guardado
    frame_ruta = ttk.LabelFrame(ventana, text="Ruta de Guardado")
    frame_ruta.pack(padx=10, pady=10, fill="x")

    ruta_label = ttk.Label(frame_ruta, text="Ruta para guardar las facturas:")
    ruta_label.pack(side=tk.LEFT, padx=5, pady=5)

    ruta_entry = ttk.Entry(frame_ruta)
    ruta_entry.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

    ruta_button = ttk.Button(frame_ruta, text="Seleccionar Ruta", command=lambda: seleccionar_ruta(ruta_entry))
    ruta_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Rango de edades
    frame_edades = ttk.LabelFrame(ventana, text="Rango de Edades")
    frame_edades.pack(padx=10, pady=10, fill="x")

    edad_min_label = ttk.Label(frame_edades, text="Edad mínima:")
    edad_min_label.pack(side=tk.LEFT, padx=5, pady=5)

    edad_min_entry = ttk.Entry(frame_edades)
    edad_min_entry.pack(side=tk.LEFT, padx=5, pady=5)

    edad_max_label = ttk.Label(frame_edades, text="Edad máxima:")
    edad_max_label.pack(side=tk.LEFT, padx=5, pady=5)

    edad_max_entry = ttk.Entry(frame_edades)
    edad_max_entry.pack(side=tk.LEFT, padx=5, pady=5)

    # Botón de generar y barra de progreso
    generar_button = ttk.Button(ventana, text="Generar Facturas", command=lambda: generar_facturas(num_documento_obligado_entry, tipo_nota_entry, num_factura_personalizada_entry, num_facturas_inicio_entry, num_facturas_fin_entry, ruta_entry, edad_min_entry, edad_max_entry, barra_progreso, ventana))
    generar_button.pack(pady=10)

    barra_progreso = ttk.Progressbar(ventana, orient=tk.HORIZONTAL, length=200, mode='determinate')
    barra_progreso.pack(pady=10)

    # Pie de página
    pie_pagina_label = ttk.Label(ventana, text="TEMA DE VALIDACION Y ENVIO DE FEV RIPS (Versión 1.0.0) Ambiente de capacitación y pruebas", font=("Arial", 8))
    pie_pagina_label.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()