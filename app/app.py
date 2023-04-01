from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from models.environment import Environment
from models.gsetters import GSetters
from models.messages import Messages

msg=Messages()

msg.print('info','Iniciando el programa...')

class persona(GSetters):
    __nombre: str = "EmiltonX"
    __apellido: str = "Mendoza"
    height: float = 1.81
    __anio: int = 1983

    def __init__(self):
        attr_include = ["__nombre", "__apellido"]
        att_exclude = ["height", "__anio"]
        self.create_getters(self,attr_include, att_exclude)
        self.create_setters(self,attr_include, att_exclude)


x=persona()
print(x.get("__nombre"))
x.set("__nombre","Emiltonnnnn")
print(x.get("__nombre"))

class animal(Environment):
    __species: str = "dog"
    __name: str = "Firulais"
    __age: int = 3

    def __init__(self) -> None:
        self.load_env(self)
        print(self.__species)
        print(self.__name)
        print(self.__age)

y=animal()
msg.print('info','Terminando el programa...')