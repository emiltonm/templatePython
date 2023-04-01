# PLANTILLA BASE PARA PROYECTOS PYTHON (TITULO)

#  Descripción general de el... (-proyecto-)
resumen del texto que envian de la prueba o descripcion del proyecto

# Tecnologías
- python

# Requerimientos
- python 3.x
- pip
- virtualenv

# Permisos necesarios

# Instalación
- Ubicarse en el directorio donde se desea clonar el repositorio
- Clonar el repositorio 
  ```
  git clone https://github.com/emiltonm/templatePython.git
  ```
- Instale un entorno virtual
  ```
  virtualenv venv
  ```
- activa el entorno virtual
  
    para windows: 
    ```
    .\venv\Scripts\activate
    ```
    para linux: 
    ```
    source venv/bin/activate
    ```
- instale las dependencias
  ```
  pip install -r requirements.txt
  ```

# Configuración
- cree y configure el archivo .env.name_modulo del proyecto 

# Ejecución
- para ejecutar el proyecto ejecute el siguiente comando:
    ```
    python app/app.py
    ```

# Notas
para simplificar la lectura de la descripcion se utilizara la siguiente notacion para los atributos de las clases: ([-,+][-,G][-,S]) <tipo_de_dato> nombre_atributo: funcion de el atributo; donde el primer caracter indica si es publico o privado el segundo si tiene un metodo get para acceder a ella y el tercero si existe un metodo set para modificar su valor ejemplo:

(-GS) < string > file_path: ruta relativa donde se encuentra el archivo de datos a partir de app.py

(+--) < int > size: numero de registros que contiene el archivo de datos

en el primero de los ejemplos indica que el atributo es privado y tiene un metodo get y set, y es de tipo string; en el segundo de los ejemplos indica que el atributo es publico y no tiene metodos get ni set, y es de tipo int

# Descripción general de la solución
Para dar solución a este (-proyecto-) se dividio en N modulos:
- **modulo1**: Descripcion del modulo
- **modulo2**: Descripcion del modulo
- ...

# Modulo environment
Este modulo se encarga de cargar las variables de entorno requeridas por cada modulo del proyecto que lo herede. para simplificar el proceso de configuracion de cada modulo, environment carga automaticamente el archivo .env.x donde x es el nombre del modulo que lo esta heredando este archivo debe estar ubicado en la raiz del proyecto y sus variables deben llamarse igual que los atributos de la clase que lo hereda. ejemplo:
```
# clase (modulo) que hereda de environment
class Data(Enviroment):
    __host: str = "<unknow>"
    __port: int = 0
    database: str = "<unknow>"
    def __init__(self):
        self.load_env(self)
        ...
```
```
# archivo .env.data
HOST=localhost
PORT=8080
DATABASE=mongodb
```
environment buscara el archivo .env.data (porque asi se llama la clase que lo heredo) y cargara las variables de entorno en los atributos del mismo nombre __host=HOST, __port=PORT, database=DATABASE


# Modulo gsetters
Este modulo se encarga de crear los metodos get y set para los atributos de la clase que lo herede, para esto se debe llamar al metodo load_gsetters(self) en el metodo __init__ de la clase que lo herede y crear una lista de los atributos a los cuales se puede acceder y una lista de los cuales no se desea que se acceda ejemplo:
```
class Data(GSetters):
    __host: str = "<unknow>"
    __port: int = 0
    database: str = "<unknow>"
    def __init__(self):
        attr_include = ["__host", "__port"]
        attr_exclude = ["database"]
        self.create_getters(self,attr_include, attr_exclude)
        self.create_setters(self,attr_include, attr_exclude)
        ...
x=Data()
print(x.get("__port"))
x.set("__port",27017)
print(x.get("__port"))
```
# Modulo x
Nota: _configurar el modulo data a traves del archivo .env.x_
Este modulo se encarga de...
## Flujo de ejecución:
- paso 1
  - paso 1.1
  - paso 1.2
- paso 2
  
## Detalles de ejecución:
- **paso 1**: descripcion detallada de el paso 1 si es necesario
- **paso 2**: descipcion detallada de el paso 2 si es necesario

## Atributos de la clase x:

(-GS) < string > **attribute_name**: descripcion...

(-GS) < string > **attribute_name**: descripcion...

(-GS) < string > **attribute_name**: descripcion...

## Metodos de la clase x:
Descripción de metodos relevantes.

**name_method(parametro:tipo,...) -> tipo retorno**: descripcion de el metodo

**name_method(parametro:tipo,...) -> tipo retorno**: descripcion de el metodo

# Futuras implementaciones
## Modulo x
- descripcion de la implementacion
- descripcion de la implementacion

## Modulo y
- descripcion de la implementacion
- descripcion de la implementacion