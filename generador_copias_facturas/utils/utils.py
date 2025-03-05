# utils.py

# Diccionario para llevar la cuenta de los consecutivos por tipo de servicio
consecutivos = {
    "consulta": 0,
    "procedimiento": 0,
    "urgencia": 0,
    "hospitalizacion": 0,
    "recien_nacido": 0,
    "medicamento": 0,
    "otro_servicio": 0
}

def generar_consecutivo(tipo):
    """Genera un consecutivo auto-incrementable por tipo de servicio."""
    consecutivos[tipo] += 1
    return consecutivos[tipo]