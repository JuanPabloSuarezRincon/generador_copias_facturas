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

def generar_usuario(edad_min=0, edad_max=100): # Valores predeterminados aquí
    return {
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE", "RC"]),
        "numDocumentoIdentificacion": fake.numerify("##########"),
        "tipoUsuario": random.choice(["01", "02", "03", "04"]),
        "fechaNacimiento": fake.date_of_birth(minimum_age=edad_min, maximum_age=edad_max).strftime("%Y-%m-%d"),
        "codSexo": random.choice(["F", "M"]),
        "codPaisResidencia": "170",
        "codMunicipioResidencia": fake.numerify("170"),
        "codZonaTerritorialResidencia": fake.numerify("#"),
        "incapacidad": random.choice(["SI", "NO"]),
        "codPaisOrigen": "170",
        "consecutivo": 1,
        "servicios": generar_servicios()
    }

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
    return {
        "codPrestador": "110013905701",
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "numAutorizacion": "",
        "codConsulta": fake.numerify("######"),
        "modalidadGrupoServicioTecSal": random.choice(["01", "02"]),
        "grupoServicios": random.choice(["01", "02"]),
        "codServicio": random.randint(100, 500),
        "finalidadTecnologiaSalud": random.choice(["15", "25"]),
        "causaMotivoAtencion": random.choice(["22", "38"]),
        "codDiagnosticoPrincipal": fake.numerify("S###"),
        "tipoDiagnosticoPrincipal": random.choice(["01", "02"]),
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]),
        "numDocumentoIdentificacion": fake.numerify("##########"),
        "vrServicio": round(random.uniform(5000, 100000), 2),
        "conceptoRecaudo": random.choice(["02", "05"]),
        "valorPagoModerador": round(random.uniform(1000, 10000), 2),
        "consecutivo": generar_consecutivo("consulta")
    }

def generar_procedimiento():
    return {
        "codPrestador": "110013905701",
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "idMIPRES": "",
        "numAutorizacion": "",
        "codProcedimiento": fake.numerify("######"),
        "viaIngresoServicioSalud": random.choice(["01", "02", "03"]),
        "modalidadGrupoServicioTecSal": random.choice(["01", "02"]),
        "grupoServicios": random.choice(["01", "02", "03"]),
        "codServicio": random.randint(100, 500),
        "finalidadTecnologiaSalud": random.choice(["15", "29"]),
        "tipoDocumentoIdentificacion": random.choice(["CC", "CE"]),
        "numDocumentoIdentificacion": fake.numerify("##########"),
        "codDiagnosticoPrincipal": fake.numerify("S###"),
        "vrServicio": round(random.uniform(5000, 100000), 2),
        "conceptoRecaudo": random.choice(["02", "05"]),
        "valorPagoModerador": round(random.uniform(1000, 10000), 2),
        "consecutivo": generar_consecutivo("procedimiento")
    }

def generar_urgencia():
    return {
        "codPrestador": "110013905701",
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "causaMotivoAtencion": random.choice(["22", "38"]),
        "codDiagnosticoPrincipal": fake.numerify("S###"),
        "condicionDestinoUsuarioEgreso": random.choice(["01", "03"]),
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "consecutivo": generar_consecutivo("urgencia")
    }

def generar_hospitalizacion():
    return {
        "codPrestador": "110013905701",
        "fechaInicioAtencion": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "numAutorizacion": fake.numerify("######"),
        "causaMotivoAtencion": random.choice(["22", "38"]),
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "consecutivo": generar_consecutivo("hospitalizacion")
    }

def generar_recien_nacido():
    return {
        "codPrestador": "110013905701",
        "tipoDocumentoIdentificacion": "RC",
        "numDocumentoIdentificacion": fake.numerify("############"),
        "fechaNacimiento": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "peso": random.randint(1000, 4000),
        "codDiagnosticoPrincipal": fake.numerify("A###"),
        "fechaEgreso": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "consecutivo": generar_consecutivo("recien_nacido")
    }

def generar_medicamento():
    return {
        "codPrestador": "110013905701",
        "numAutorizacion": fake.numerify("######"),
        "idMIPRES": fake.numerify("######"),
        "fechaDispensAdmon": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "codTecnologiaSalud": fake.numerify("#####"),
        "nomTecnologiaSalud": fake.word(),
        "consecutivo": generar_consecutivo("medicamento")
    }

def generar_otro_servicio():
    return {
        "codPrestador": "110013905701",
        "numAutorizacion": fake.numerify("######"),
        "fechaSuministroTecnologia": fake.date_time().strftime("%Y-%m-%d %H:%M"),
        "tipoOS": random.choice(["01", "02"]),
        "codTecnologiaSalud": fake.numerify("#####"),
        "nomTecnologiaSalud": fake.word(),
        "consecutivo": generar_consecutivo("otro_servicio")
    }

def generar_factura(num_factura, num_documento_obligado, tipo_nota, num_factura_personalizada, edad_min=0, edad_max=100):
    num_nota = f"Fev{num_factura}" if tipo_nota and tipo_nota in ["NC", "ND", "NA", "RS"] else None
    num_factura_final = num_factura_personalizada if num_factura_personalizada else f"FCT-{num_factura}"

    return {
        "numDocumentoIdObligado": num_documento_obligado,
        "numFactura": num_factura_final,
        "tipoNota": tipo_nota if tipo_nota else None,
        "numNota": num_nota,
        "usuarios": [generar_usuario(edad_min, edad_max)]
    }
