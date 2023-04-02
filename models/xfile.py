'''
descripción:
uso:
explicación:
'''

from pathlib import Path

from messages import msg


class Xfile:
    __path: str = ''
    __file: str = ''
    __full_path: str = ''
    __encoding: str = ''
    __MB_block_size: int = 0
    __ignore__errors_data: bool = True

    __headers_in_file: bool = False
    __custom_headers: list = []
    __types: list = []
    __separator: str = ''
    __headers: list = []

    __pre_load: any = None

    __long_char_separators: list = []

    __data: list = []

    def __init__(self):
        pass

    def config(self, path: str, file: str, encoding: str, ignore_errors_data: bool, MB_block_size: int = 0):
        self.__path = path
        self.__file = file
        self.__full_path = Path(self.__path)/self.__file
        self.__encoding = encoding
        self.__ignore__errors_data = ignore_errors_data
        self.__MB_block_size = MB_block_size

    def read_tabulated(self, separator: str, types: list = [], headers_in_file: bool = True,  custom_headers: list = [], ignore_errors: bool = True) -> dict:
        self.__data.clear()
        self.__separator = separator
        self.__headers_in_file = headers_in_file
        self.__types = types.copy()
        self.__custom_headers = custom_headers.copy()
        self.__ignore__errors_data = ignore_errors

        # abro el archivo de datos
        if not self.file_exists():
            msg.print(
                'error', f'el archivo {self.__file} No se encuentra en la ruta {self.__path}')
            return None
        else:
            msg.print(
                'info', f'leyendo el archivo {self.__file} de la ruta {self.__path}')
            with open(self.__full_path, 'r', encoding=self.__encoding) as file:
                # si el archivo tiene cabeceras y no se han definido cabeceras personalizadas
                if self.__headers_in_file and len(self.__custom_headers) == 0:
                    self.__headers = file.readline().strip().split(self.__separator)
                # si el archivo no tiene cabeceras y se han definido cabeceras personalizadas
                elif not self.__headers_in_file and len(self.__custom_headers) > 0:
                    self.__headers = self.__custom_headers.copy()
                # si el archivo no tiene cabeceras y no se han definido cabeceras personalizadas
                elif not self.__headers_in_file and len(self.__custom_headers) == 0:
                    msg.print(
                        'error', 'no se han definido cabeceras para el archivo')
                    return None
                # si el archivo tiene cabeceras y se han definido cabeceras personalizadas
                elif self.__headers_in_file and len(self.__custom_headers) > 0:
                    self.__headers = self.__custom_headers.copy()

                for line in file:
                    value = line.strip().split(self.__separator)
                    if len(self.__headers) != len(value):
                        msg.print(
                            'error', 'la cantidad de cabeceras no coincide con la cantidad de valores de este registro')
                        if self.__ignore__errors_data:
                            continue
                        else:
                            return None
                    # combino los headers con los valores para formar un diccionario
                    self.__data.append(dict(zip(self.__headers, value)))
                return self.__data

    def read_numchar(self, long_char_separators: list) -> dict:
        self.__long_char_separators = long_char_separators.copy()

    def read_tagged(self, templateHV: str) -> dict:
        pass

    def affect_raw_data(self, list_function: list):
        pass

    def file_exists(self) -> bool:
        return self.__full_path.exists()


mfile = Xfile()
mfile.config('data', 'MOCK_DATA.csv', 'utf-8', True)
# quede implmentando la conversion de tipos de datos
response = mfile.read_tabulated(',',[])
print(response)
