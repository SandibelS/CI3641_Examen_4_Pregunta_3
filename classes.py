
class Clase():
    def __init__(self, nombre :str, metodos : dict[str: str]):
        self.nombre = nombre
        self.metodos = metodos

class Simulador():
    def __init__(self):
        self.clases : dict[str, Clase] = {}

    def crear_clase_simple(self, nombre :str, metodos : list[str]) -> None:

        dict_metodos : dict[str: str] = {}

        # Creamos un diccionaro con los metodos asociados a su clase
        # revisamos que no hayan metodos repetidos
        for metodo in metodos:
            if metodo in dict_metodos:
                raise ValueError("No pueden haber multiples metodos con el mismo nombre")
            dict_metodos[metodo] = nombre

        # comprobar que esta clase no ha sido declarada antes
        if nombre in self.clases:
            raise ValueError(f"Ya existe una clase con el nombre: {nombre}")  
        
        # Creamos la clase y la unimos al dicc de clases que llevamos
        nuevaClase = Clase(nombre, dict_metodos)

        self.clases[nombre] = nuevaClase
    
    def crear_clase_con_herencia(self, nombre :str, metodos : list[str], super_clase : str) -> None:

        # ver si hay una clase que ya tiene el nombre pasado
        if nombre in self.clases:
            raise ValueError(f"Ya existe una clase con el nombre: {nombre}")  
        
        # ver si la clase que se desea heredar existe
        if (super_clase in self.clases) == False:
            raise ValueError(f"No existe una clase con el nombre: {super_clase}")

        dict_metodos : dict[str: str] = {}

        # Creamos un diccionaro con los metodos  asociados a su clase
        # revisamos que no hayan metodos repetidos
        for metodo in metodos:
            if metodo in dict_metodos:
                raise ValueError("No pueden haber multiples metodos con el mismo nombre")
            dict_metodos[metodo] = nombre

        # Le agregamos los metodos heredados de la super clase
        # que no se hayan reemplazado
        metodos_super_clase = self.clases[super_clase].metodos
        for metodo in metodos_super_clase.keys():
            if (metodo in dict_metodos) == False:
                dict_metodos[metodo] = metodos_super_clase[metodo]
        
        nuevaClase = Clase(nombre, dict_metodos)
        self.clases[nombre] = nuevaClase

    def describir(self, nombre) -> dict[str: str]:

        if (nombre in self.clases) == False:
            raise ValueError("No existe esa clase")
        
        clase = self.clases[nombre]
        metodos = clase.metodos
       
        return metodos