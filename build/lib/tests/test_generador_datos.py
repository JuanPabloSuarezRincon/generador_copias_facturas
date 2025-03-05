from generador_copias_facturas.datos.generador_datos_rs import generar_factura

def test_generar_factura():
    """Prueba la función generar_factura()"""

    # Datos de prueba
    num_factura = 1
    num_documento_obligado = "123456789"
    tipo_nota = "NC"
    num_factura_personalizada = "FCT-123"

    # Generar factura
    factura = generar_factura(num_factura, num_documento_obligado, tipo_nota, num_factura_personalizada)

    # Aserciones
    assert isinstance(factura, dict)  # Verifica que la factura sea un diccionario
    assert factura["numFactura"] == num_factura_personalizada  # Verifica el número de factura
    assert factura["numDocumentoIdObligado"] == num_documento_obligado  # Verifica el número de documento del obligado
    assert factura["tipoNota"] == tipo_nota  # Verifica el tipo de nota
    assert factura["numNota"] == f"Fev{num_factura}"  # Verifica el número de nota
    assert isinstance(factura["usuarios"], list)  # Verifica que "usuarios" sea una lista
    assert len(factura["usuarios"]) == 1  # Verifica que haya un usuario en la lista
    assert isinstance(factura["usuarios"][0], dict)  # Verifica que el usuario sea un diccionario
    assert "tipoDocumentoIdentificacion" in factura["usuarios"][0]  # Verifica que el usuario tenga un tipo de documento
    assert "numDocumentoIdentificacion" in factura["usuarios"][0]  # Verifica que el usuario tenga un número de documento
    # Agrega más aserciones para verificar otros campos del usuario y los servicios

    # Prueba con tipo_nota=None
    factura_sin_nota = generar_factura(num_factura, num_documento_obligado, None, num_factura_personalizada)
    assert factura_sin_nota["tipoNota"] is None
    assert factura_sin_nota["numNota"] is None

    # Prueba con num_factura_personalizada=None
    factura_sin_num_factura_personalizada = generar_factura(num_factura, num_documento_obligado, tipo_nota, None)
    assert factura_sin_num_factura_personalizada["numFactura"] == f"FCT-{num_factura}"