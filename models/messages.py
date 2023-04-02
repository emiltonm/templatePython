'''
descripcion:
    clase que se encarga de mostrar mensajes en pantalla y en archivos de log
uso:
    msg = Messages()
    msg.print('success', 'mensaje de prueba')
explicacion:
    existen varios tipos de mensajes predefinidos: normal, success, info, warning, error
    se puede agregar mas tipos con la funcion add_type o remover con la funcion remove_type
    se puede activar un archivo log individual para cada tipo de mensaje cambiando el valor de log a True
    con la funcion change_log_type
    se puede activar o desactivar la impresion en pantalla de un tipo de mensaje cambiando el valor de screen a True o False
    con la funcion change_screen_type
    sepuede desactivar el general.log cambiando el valor de general_log a False con la funcion
    deactivate_general_log o reactivar con la funcion activate_general_log
'''
from pathlib import Path
from datetime import datetime

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'
BG_RESET = '\033[49m'


class Messages:
    __log_path: str = 'log'
    __full_path: str = ''
    __file_general_log: str = 'general.log'
    __general_log: bool = True
    message_types = {
        'normal': {'color': WHITE, 'bgcolor': BG_RESET, 'log': False, 'screen': True},
        'success': {'color': GREEN, 'bgcolor': BG_RESET, 'log': False, 'screen': True},
        'info': {'color': BLUE, 'bgcolor': BG_RESET, 'log': False, 'screen': True},
        'warning': {'color': YELLOW, 'bgcolor': BG_RESET, 'log': False, 'screen': True},
        'error': {'color': RED, 'bgcolor': BG_RESET, 'log': False, 'screen': True}
    }

    def __init__(self, log_path: str = ''):
        if log_path != '':
            self.__log_path = log_path
        else:
            self.__log_path = 'log'
        self.__full_path = Path(
            __file__).resolve().parent.parent/self.__log_path
        if not self.__full_path.exists():
            self.__full_path.mkdir(parents=True, exist_ok=True)

    def print(self, type: str, message: str):
        fecha = datetime.now().strftime('%Y-%m-%d.%H:%M:%S')
        if type in self.message_types:
            if self.message_types[type]['screen']:
                print(
                    f'{self.message_types[type]["bgcolor"]}{self.message_types[type]["color"]}{message}{RESET}{BG_RESET}')
            if self.message_types[type]['log']:
                with open(self.__full_path/f'{type}.log', 'a') as f:
                    f.write(f'[{fecha}]{message}\n')
            if self.__general_log:
                with open(self.__full_path/self.__file_general_log, 'a') as f:
                    f.write(f'[{type}][{fecha}]{message}\n')

    def show_messages(self, type: str):
        if type in self.message_types:
            with open(self.__full_path/f'{type}.log', 'r') as f:
                print(f.read())
    
    def add_type(self, type: str, color: str, bgcolor: str, log: bool, screen: bool):
        self.message_types[type] = {
            'color': color, 'bgcolor': bgcolor, 'log': log, 'screen': screen}

    def remove_type(self, type: str):
        if type in self.message_types:
            self.message_types.pop(type)

    def change_log_type(self, type: str, log: bool):
        if type in self.message_types:
            self.message_types[type]['log'] = log

    def change_screen_type(self, type: str, screen: bool):
        if type in self.message_types:
            self.message_types[type]['screen'] = screen

    def activate_general_log(self):
        self.__general_log = True
    
    def deactivate_general_log(self):
        self.__general_log = False

msg = Messages()