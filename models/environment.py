'''
descripción:
    clase que se encarga de leer el archivo .env indicado y asigna a las variables de la clase con el mismo nombre
uso:
    class Data(Enviroment):
        __name: str = "emilton"
        __altura: float = 1.81
        def __init__(self):
            self.load_env(self)
            ...
explicación:
    Al llamar al método load_env este busca en la raiz del proyecto un archivo .env.nombre_clase
    si lo encuentra intenta cargar las variables de entorno que coincidan con los atributos de la clase
    ejemplo:
        para el atributo __name se busca la variable de entorno NAME
        la conversion de datos se hace de manera automatica para los datos str, int, float, bool y list
'''
from decouple import Config, RepositoryEnv
from pathlib import Path


class Environment:
    __config_file: str = ''

    def load_env(self, obj: object):
        # cargar el archivo .env.name_class
        file_name = '.env.'+obj.__class__.__name__.lower()
        self.__config_file = Path(__file__).resolve().parent.parent/file_name
        if not self.__file_exists(self.__config_file, f'No existe el archivo {file_name} en la raiz del proyecto'):
            return None
        else:
            # cargar el archivo .env
            config = Config(RepositoryEnv(self.__config_file))
            for atributo in obj.__class__.__annotations__:
                # dependiendo si el atributo es publico o privado
                # se le asigna el nombre de la variable de entorno
                if atributo.startswith('_'+obj.__class__.__name__+'__'):
                    env_var = atributo.split('__')[1].upper()
                else:
                    env_var=atributo.upper()

                try:
                    # comprueba si existe la variable de entorno en el archivo .env
                    config(env_var)
                except:
                    print(
                        f'No existe la variable de entorno {env_var} en el archivo {file_name}')
                    continue
                # si atributo es tipo str
                if obj.__class__.__annotations__[atributo] == str:
                    obj.__setattr__(atributo, config(env_var))
                    continue
                # si atributo es tipo int
                if obj.__class__.__annotations__[atributo] == int:
                    obj.__setattr__(atributo, int(config(env_var)))
                    continue
                # si atributo es tipo float
                if obj.__class__.__annotations__[atributo] == float:
                    obj.__setattr__(atributo, float(config(env_var)))
                    continue
                # si atributo es tipo bool
                if obj.__class__.__annotations__[atributo] == bool:
                    var_bool = config(env_var).upper()
                    if var_bool == 'TRUE':
                        obj.__setattr__(atributo, True)
                    else:
                        obj.__setattr__(atributo, False)
                    continue
                # si atributo es tipo list
                if obj.__class__.__annotations__[atributo] == list:
                    obj.__setattr__(atributo, config(env_var).split(','))
                    continue

    def __file_exists(self, path: str, error_message: str = '', out_screen: bool = True) -> bool:
        if path.is_file():
            return True
        else:
            if out_screen:
                print(error_message)
            return False