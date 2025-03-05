# generador_datos_rs.py
import random
from faker import Faker
from generador_copias_facturas.utils.utils import generar_consecutivo

fake = Faker('es_ES')

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
    """Genera un consecutivo auto-incrementable por tipo de servicio"""
    consecutivos[tipo] += 1
    return consecutivos[tipo]

def generar_usuario(edad_min=0, edad_max=100):
    usuario = {
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE", "RC"]), # U01, Obligatorio, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # U02, Obligatorio, de 4 a 20 caracteres, tipo C
        "tipoUsuario": random.choice(["01", "02", "03", "04"]), # U03, Obligatorio, 2 caracteres, tipo C
        "fechaNacimiento": fake.date_of_birth(minimum_age=edad_min, maximum_age=edad_max).strftime("%Y-%m-%d"), # U04, Obligatorio, 10 caracteres, tipo C
        "codSexo": random.choice(["F", "M"]), # U05, Obligatorio, 1 caracter, tipo C
        "codPaisResidencia": "170", # U06, Obligatorio, 3 caracteres, tipo C
        "codMunicipioResidencia": fake.numerify("170"), # U07, 5 caracteres, tipo C (aunque en tu lógica es numérico)
        "codZonaTerritorialResidencia": fake.numerify("#"), # U08, 2 caracteres, tipo C
        "incapacidad": random.choice(["SI", "NO"]), # U09, Obligatorio, 2 caracteres, tipo C
        "consecutivo": 1, # U10, Obligatorio, de 1 a 7 caracteres, tipo N (aunque en tu lógica es fijo)
        "codPaisOrigen": "170", # U11, Obligatorio, 3 caracteres, tipo C
        "servicios": generar_servicios() # No especificado en la homologación, pero se mantiene de tu lógica
    }

    return usuario

def generar_servicios():
    return {
        "consultas": [generar_consulta() for _ in range(random.randint(1, 3))],
        "procedimientos": [generar_procedimiento() for _ in range(random.randint(1, 3))],
        "urgencias": [generar_urgencia() for _ in range(random.randint(1, 2))],
        "hospitalizacion": [generar_hospitalizacion() for _ in range(random.randint(1, 2))],
        "recienNacidos": [generar_recien_nacido() for _ in range(random.randint(1, 2))],
        "medicamentos": [generar_medicamento() for _ in range(random.randint(1, 3))],
        "otrosServicios": [generar_otro_servicio() for _ in range(random.randint(1, 3))]
    }

def generar_consulta():
    # Códigos CUPS válidos (ejemplo)
    codigos_cups_validos = ["890302", "890303", "890304", "890305"]

    # Códigos CIE-10 válidos (ejemplo)
    codigos_cie10_validos = ["Z000", "Z001", "Z002", "Z003"]

    return {
        "codPrestador": "110013905701", # C01, 12 caracteres, tipo C
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"), # C02, 16 caracteres, tipo C
        "numAutorizacion": None, # C03, 0-30 caracteres, tipo C, opcional
        "codConsulta": fake.numerify("######"), # C04, 6 caracteres, tipo C
        "modalidadGrupoServicioTecSal": random.choice(["01", "02"]), # C05, 2 caracteres, tipo C
        "grupoServicios": random.choice(["01", "02"]), # C06, 2 caracteres, tipo C
        "codServicio": random.choice(codigos_cups_validos), # C07, 3-4 caracteres, tipo N
        "finalidadTecnologiaSalud": random.choice(["15", "25"]), # C08, 2 caracteres, tipo C
        "causaMotivoAtencion": random.choice(["22", "38"]), # C09, 2 caracteres, tipo C
        "codDiagnosticoPrincipal": random.choice(codigos_cie10_validos), # C10, 4 caracteres, tipo C
        "codDiagnosticoRelacionado1": random.choice(codigos_cie10_validos + [None]), # C11, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionado2": random.choice(codigos_cie10_validos + [None]), # C12, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionado3": random.choice(codigos_cie10_validos + [None]), # C13, 4 caracteres, tipo C, opcional
        "tipoDiagnosticoPrincipal": random.choice(["01", "02"]), # C14, 2 caracteres, tipo C
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # C15, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # C16, 4-20 caracteres, tipo C
        "vrServicio": round(random.uniform(5000, 100000), 2), # C17, 1-10 caracteres, tipo N
        "conceptoRecaudo": "05", # C18, 2 caracteres, tipo C
        "valorPagoModerador": random.randint(0, 10000), # C19, 1-10 caracteres, tipo N
        "numFEVPagoModerador": None, # C20, 1-30 caracteres, tipo C, opcional
        "consecutivo": generar_consecutivo("consulta") # C21, 1-7 caracteres, tipo N
    }

def generar_procedimiento():
    # Códigos CUPS válidos (ejemplo)
    codigos_cups_validos = ["99213", "99214", "99215", "99241"]

    # Códigos CIE-10 válidos (ejemplo)
    codigos_cie10_validos = ["Z000", "Z001", "Z002", "Z003"]

    return {
        "codPrestador": "110013905701", # P01, 12 caracteres, tipo C
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"), # P02, 16 caracteres, tipo C
        "idMIPRES": None, # P03, 0-15 caracteres, tipo C, opcional
        "numAutorizacion": None, # P04, 0-30 caracteres, tipo C, opcional
        "codProcedimiento": random.choice(codigos_cups_validos), # P05, 6 caracteres, tipo C
        "viaIngresoServicioSalud": random.choice(["01", "02", "03"]), # P06, 2 caracteres, tipo C
        "modalidadGrupoServicioTecSal": random.choice(["01", "02"]), # P07, 2 caracteres, tipo C
        "grupoServicios": random.choice(["01", "02"]), # P08, 2 caracteres, tipo C
        "codServicio": fake.numerify("####"), # P09, 3-4 caracteres, tipo N
        "finalidadTecnologiaSalud": random.choice(["15", "25"]), # P10, 2 caracteres, tipo C
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # P11, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # P12, 4-20 caracteres, tipo C
        "codDiagnosticoPrincipal": random.choice(codigos_cie10_validos), # P13, 4 caracteres, tipo C
        "codDiagnosticoRelacionado": random.choice(codigos_cie10_validos + [None]), # P14, 4 caracteres, tipo C, opcional
        "codComplicacion": None, # P15, 4 caracteres, tipo C, opcional
        "vrServicio": round(random.uniform(5000, 100000), 2), # P16, 1-15 caracteres, tipo N
        "conceptoRecaudo": "05", # P17, 2 caracteres, tipo C
        "valorPagoModerador": random.randint(0, 10000), # P18, 1-10 caracteres, tipo N
        "numFEVPagoModerador": None, # P19, 1-30 caracteres, tipo C, opcional
        "consecutivo": generar_consecutivo("procedimiento") # P20, 1-7 caracteres, tipo N
    }

def generar_urgencia():
    # Códigos CIE-10 válidos (ejemplo)
    codigos_cie10_validos = ["R100", "R101", "R102", "R103"]

    return {
        "codPrestador": "110013905701", # U01, 12 caracteres, tipo C
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"), # U03, 16 caracteres, tipo C
        "causaMotivoAtencion": random.choice(["22", "38"]), # U05, 2 caracteres, tipo C
        "codDiagnosticoPrincipal": random.choice(codigos_cie10_validos), # U06, 4 caracteres, tipo C
        "codDiagnosticoPrincipalE": random.choice(codigos_cie10_validos), # U07, 4 caracteres, tipo C
        "codDiagnosticoRelacionadoE1": random.choice(codigos_cie10_validos + [None]), # U08, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionadoE2": random.choice(codigos_cie10_validos + [None]), # U09, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionadoE3": random.choice(codigos_cie10_validos + [None]), # U10, 4 caracteres, tipo C, opcional
        "condicionDestinoUsuarioEgreso": random.choice(["01", "02", "03"]), # U11, 2 caracteres, tipo C
        "codDiagnosticoCausaMuerte": None, # U12, 0-4 caracteres, tipo C, opcional
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"), # U13, 16 caracteres, tipo C
        "consecutivo": generar_consecutivo("urgencia") # U14, 1-7 caracteres, tipo N
    }

def generar_hospitalizacion():
    # Códigos CIE-10 válidos (ejemplo)
    codigos_cie10_validos = ["J00", "J01", "J02", "J03"]

    return {
        "codPrestador": "110013905701", # H01, 12 caracteres, tipo C
        "viaIngresoServicioSalud": random.choice(["01", "02", "03"]), # H02, 2 caracteres, tipo C
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"), # H03, 16 caracteres, tipo C
        "causaMotivoAtencion": random.choice(["22", "38"]), # H04, 2 caracteres, tipo C
        "codDiagnosticoPrincipal": random.choice(codigos_cie10_validos), # H05, 4 caracteres, tipo C
        "codDiagnosticoPrincipalE": random.choice(codigos_cie10_validos), # H06, 4 caracteres, tipo C
        "codDiagnosticoRelacionadoE1": random.choice(codigos_cie10_validos + [None]), # H07, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionadoE2": random.choice(codigos_cie10_validos + [None]), # H08, 4 caracteres, tipo C, opcional
        "codDiagnosticoRelacionadoE3": random.choice(codigos_cie10_validos + [None]), # H09, 4 caracteres, tipo C, opcional
        "condicionDestinoUsuarioEgreso": random.choice(["01", "02", "03"]), # H10, 2 caracteres, tipo C
        "codDiagnosticoCausaMuerte": None, # H11, 0-4 caracteres, tipo C, opcional
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"), # H12, 16 caracteres, tipo C
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # H13, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # H14, 4-20 caracteres, tipo C
        "consecutivo": generar_consecutivo("hospitalizacion") # H15, 1-7 caracteres, tipo N
    }

def generar_recien_nacido():
    # Códigos CIE-10 válidos (ejemplo)
    codigos_cie10_validos = ["P000", "P001", "P002", "P003"]

    return {
        "codPrestador": "110013905701", # RN01, 12 caracteres, tipo C
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # RN02, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # RN03, 4-20 caracteres, tipo C
        "fechaNacimiento": fake.date_time().strftime("%Y-%m-%d %H:%M"), # RN04, 16 caracteres, tipo C
        "edadGestacional": random.randint(20, 40), # RN05, 2 caracteres, tipo N
        "numConsultasCPrenatal": random.randint(1, 9), # RN06, 1-2 caracteres, tipo N
        "codSexoBiologico": random.choice(["M", "F"]), # RN07, 1 caracter, tipo C
        "peso": random.randint(1000, 4000), # RN08, 3-4 caracteres, tipo N
        "codDiagnosticoPrincipal": random.choice(codigos_cie10_validos), # RN09, 4 caracteres, tipo C
        "condicionDestinoUsuarioEgreso": random.choice(["01", "02", "03"]), # RN10, 2 caracteres, tipo C
        "codDiagnosticoCausaMuerte": None, # RN11, 0-4 caracteres, tipo C, opcional
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"), # RN12, 16 caracteres, tipo C
        "consecutivo": generar_consecutivo("recien_nacido") # RN13, 1-7 caracteres, tipo N
    }

def generar_medicamento():
    # Códigos de medicamentos válidos (ejemplo)
    codigos_medicamentos_validos = ["J01AA02", "J01AA03", "J01AA04", "J01AA05"]

    return {
        "codPrestador": "110013905701", # M01, 12 caracteres, tipo C
        "numAutorizacion": None, # M02, 0-30 caracteres, tipo C, opcional
        "idMIPRES": None, # M03, 0-15 caracteres, tipo C, opcional
        "fechaDispensAdmon": fake.date_time().strftime("%Y-%m-%d %H:%M"), # M04, 16 caracteres, tipo C
        "codDiagnosticoPrincipal": fake.numerify("S###"), # M05, 4 caracteres, tipo C
        "codDiagnosticoRelacionado": None, # M06, 4 caracteres, tipo C, opcional
        "tipoMedicamento": random.choice(["01", "02", "03"]), # M07, 2 caracteres, tipo C
        "codTecnologiaSalud": fake.numerify("1M1008891000101"), # M08, 0-20 caracteres, tipo C
        "nomTecnologiaSalud": fake.sentence()[:30], # M09, 0-30 caracteres, tipo C
        "concentracionMedicamento": random.randint(0, 100), # M10, 0-3 caracteres, tipo N
        "unidadMedida": random.randint(0, 10), # M11, 0-4 caracteres, tipo N
        "formaFarmaceutica": None, # M12, 6 u 8 caracteres, tipo C, opcional
        "unidadMinDispensa": random.randint(1, 2), # M13, 1-2 caracteres, tipo N
        "cantidadMedicamento": random.randint(1, 10), # M14, 1-10 caracteres, tipo N
        "diasTratamiento": random.randint(1, 3), # M15, 1-3 caracteres, tipo N
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # M16, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # M17, 4-20 caracteres, tipo C
        "vrUnitMedicamento": round(random.uniform(100, 1000), 2), # M18, 1-15 caracteres, tipo N
        "vrServicio": round(random.uniform(100, 1000), 2), # M19, 1-15 caracteres, tipo N
        "conceptoRecaudo": "05", # M20, 2 caracteres, tipo C
        "valorPagoModerador": 0, # M21, 1-10 caracteres, tipo N
        "numFEVPagoModerador": None, # M22, 1-30 caracteres, tipo C, opcional
        "consecutivo": generar_consecutivo("medicamento") # M23, 1-7 caracteres, tipo N
    }

def generar_otro_servicio():
    return {
        "codPrestador": "110013905701", # OS01, Obligatorio, 12 caracteres, tipo C
        "numAutorizacion": None, # OS02, Opcional (NULL), de 0 a 30 caracteres, tipo C
        "idMIPRES": None, # OS03, Opcional (NULL), de 0 a 15 caracteres, tipo C
        "fechaSuministroTecnologia": fake.date_time().strftime("%Y-%m-%d %H:%M"), # OS04, Obligatorio, 16 caracteres, tipo C
        "tipoOS": random.choice(["01", "02"]), # OS05, Obligatorio, 2 caracteres, tipo C
        "codTecnologiaSalud": fake.numerify("20C05"), # OS06, Opcional (NULL), de 0 a 30 caracteres, tipo C
        "nomTecnologiaSalud": fake.sentence()[:60], # OS07, Opcional (NULL), de 0 a 60 caracteres, tipo C
        "cantidadOS": random.randint(1, 5), # OS08, Obligatorio, de 1 a 5 caracteres, tipo N
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]), # OS09, Obligatorio, 2 caracteres, tipo C
        "numDocumentoIdentificacion": fake.numerify("##########"), # OS10, Obligatorio, de 4 a 20 caracteres, tipo C
        "vrUnitOS": round(random.uniform(100, 1000), 2), # OS11, Obligatorio, de 1 a 15 caracteres, tipo N
        "vrServicio": round(random.uniform(100, 1000), 2), # OS12, Obligatorio, de 1 a 15 caracteres, tipo N
        "conceptoRecaudo": "05", # OS13, Obligatorio, 2 caracteres, tipo C
        "valorPagoModerador": 0, # OS14, Obligatorio, de 1 a 10 caracteres, tipo N
        "numFEVPagoModerador": None, # OS15, Opcional (NULL), de 1 a 30 caracteres, tipo C
        "consecutivo": generar_consecutivo("otro_servicio") # OS16, Obligatorio, de 1 a 7 caracteres, tipo N
    }

def generar_factura(num_factura, num_documento_obligado, num_factura_personalizada, edad_min=0, edad_max=100):
    factura = {
        "numDocumentoIdObligado": num_documento_obligado,
        "numFactura": num_factura_personalizada,
        "tipoNota": "RS",
        "numNota": f"FEV{num_factura}",
        "usuarios": [generar_usuario(edad_min, edad_max)]
    }

    # Aplicar valores predeterminados a los campos específicos
    for usuario in factura["usuarios"]:
        for servicio in usuario["servicios"].values():
            if isinstance(servicio, list):
                for item in servicio:
                    if "vrServicio" in item:
                        item["vrServicio"] = 0
                    if "valorPagoModerador" in item:
                        item["valorPagoModerador"] = 0
                    if "conceptoRecaudo" in item:
                        item["conceptoRecaudo"] = "05"

    return factura