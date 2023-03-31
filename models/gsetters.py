'''
descripción:
    clase que se encarga de devolver valores mediante el método get y asignar valores mediante el método set
    a los atributos incluidos en una lista de la clase que la herede
uso:
    class Data(GSetters):
        __name: str = "emilton"
        __altura: float = 1.81
        __last_name: str = "mendoza"
        __anio: int = 1983
        def __init__(self):
            attr_include = ["__name", "__altura"]
            att_exclude = ["__last_name", "__anio"]
            self.create_getters(self,attr_include, att_exclude)
            self.create_setters(self,attr_include, att_exclude)
            ...
    x=Data()
    print(x.get("__name"))
    x.set("__name","Emiltonnnnn")
    print(x.get("__name"))
explicación:
    creo una lista de nombres de atributos a los cuales voy a permitir acceder mediante el método get y set
    y una lista de atributos a los cuales no voy a permitir acceder mediante el método get y set
    al llamar al método get se comprueba si el atributo existe en la lista de atributos incluidos
    si existe se devuelve el valor del atributo
'''



class GSetters:
    __Get_object: object = None
    __included_get_attr: list = []
    __excluded_get_attr: list = []
    __Set_object: object = None
    __included_set_attr: list = []
    __excluded_set_attr: list = []

    def create_getters(self, obj: object, included_attr: list, excluded_attr: list):
        self.__Get_object = obj
        self.__included_get_attr = included_attr.copy()
        self.__excluded_get_attr = excluded_attr.copy()

    def create_setters(self, obj: object, included_attr: list, excluded_attr: list):
        self.__Set_object = obj
        self.__included_set_attr = included_attr.copy()
        self.__excluded_set_attr = excluded_attr.copy()

    def __fix_list_attr_name(self, obj: object, attributes: list):
        tmp_list = []
        for attr in attributes:
            if attr.startswith('__'):
                tmp_list.append('_'+obj.__class__.__name__+attr)
            else:
                tmp_list.append(attr)
        attributes.clear()
        attributes.extend(tmp_list)

    def __fix_attr_name(self, obj: object, attribute: str):
        if attribute.startswith('__'):
            attribute = '_'+obj.__class__.__name__+attribute
        return attribute

    def get(self, attr: str) -> any:
        self.__fix_list_attr_name(self.__Get_object, self.__included_get_attr)
        self.__fix_list_attr_name(self.__Get_object, self.__excluded_get_attr)
        attr = self.__fix_attr_name(self.__Get_object, attr)

        if attr in self.__included_get_attr and attr not in self.__excluded_get_attr:
            return self.__Get_object.__getattribute__(attr)
        else:
            print(
                f'El atributo {attr} en el objeto {self.__Get_object.__class__.__name__} no esta incluido en la lista de atributos')
            return None

    def set(self, attr: str, value: any):
        self.__fix_list_attr_name(self.__Set_object, self.__included_set_attr)
        self.__fix_list_attr_name(self.__Set_object, self.__excluded_set_attr)
        attr = self.__fix_attr_name(self.__Set_object, attr)

        if attr in self.__included_set_attr and attr not in self.__excluded_set_attr:
            self.__Set_object.__setattr__(attr, value)
        else:
            print(
                f'El atributo {attr} en el objeto {self.__Set_object.__class__.__name__} no esta incluido en la lista de atributos')
