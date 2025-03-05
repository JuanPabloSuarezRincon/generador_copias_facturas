from setuptools import setup, find_packages

setup(
    name='generador_copias_facturas',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'faker',
    ],
    entry_points={
        'console_scripts': [
            'generador-facturas=generador_copias_facturas.main:main', # Ruta actualizada
        ],
    },
    author='Tu Nombre',
    author_email='tu_correo@example.com',
    description='Aplicación para generar copias de facturas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='URL_DEL_REPOSITORIO',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)

#Explicación del contenido:
    #name: El nombre de tu paquete (debe ser el mismo que el nombre del directorio principal de tu proyecto).
    #version: La versión inicial de tu aplicación.
    #packages: Una lista de todos los paquetes que se incluirán en la distribución. find_packages() encuentra automáticamente todos los paquetes en tu proyecto.
    #install_requires: Una lista de las dependencias externas de tu proyecto (las mismas que en requirements.txt).
    #entry_points: Define los puntos de entrada para tu aplicación. En este caso, crea un script de consola llamado generador-facturas que ejecuta la función main() del módulo main.py.
    #author y author_email: Tu nombre y dirección de correo electrónico.
    #description: Una breve descripción de tu aplicación.
    #long_description: Una descripción más detallada de tu aplicación (se lee del archivo README.md).
    #long_description_content_type: El tipo de contenido de long_description (en este caso, Markdown).
    #url: La URL del repositorio de tu proyecto en GitHub.
    #classifiers: Metadatos adicionales sobre tu aplicación (estado de desarrollo, audiencia, licencia, etc.).
    #python_requires: La versión mínima de Python requerida para ejecutar tu aplicación.

#Instalar la aplicación (desistalarla) , (Reinstalar)
    #Si quieres instalar tu aplicación localmente, puedes ejecutar el siguiente comando en tu terminal:
            #pip install .
    #Esto instalará tu aplicación en tu entorno virtual (si estás usando uno) y creará el script de consola generador-facturas.
    #puedes desinstalarla cuando quieras usando pip uninstall. Aquí te explico cómo:
        #Abre una terminal o símbolo del sistema.
        #Navega hasta el directorio raíz de tu proyecto (el mismo nivel que generador_copias_facturas).
        #Ejecuta el siguiente comando:
            #pip uninstall generador_copias_facturas
    #Esto desinstalará la aplicación y todas sus dependencias.
    #Si estás usando un entorno virtual, asegúrate de que esté activado antes de ejecutar el comando.
    #Reinstala la aplicación:
        #Abre una terminal y navega hasta el directorio raíz de tu proyecto.
        #Ejecuta el siguiente comando para reinstalar la aplicación:
            #pip install --upgrade .


#Crear un paquete distribuible (opcional)
    #Si quieres crear un paquete distribuible para tu aplicación (por ejemplo, un archivo wheel), puedes ejecutar el siguiente comando:
        #python setup.py sdist bdist_wheel
    #Esto creará un directorio dist/ que contiene los paquetes distribuibles.

#setup.py:
    #Se ha creado el archivo setup.py con la configuración de la distribución de la aplicación.
