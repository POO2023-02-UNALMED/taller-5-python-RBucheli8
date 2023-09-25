from zooAnimales.animal import Animal


class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero=None, color, venenoso):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorPiel = color
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return cls._listado.len()

    def movimiento(self):
        pass

    def crearRana(self, nombre, edad, genero):
        Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1

    def crearSalamandra(self, nombre, edad, genero):
        Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
