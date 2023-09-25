from zooAnimales.animal import Animal


class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado += self

    @classmethod
    def cantidadMamiferos(cls):
        return cls._listado.len()

    def crearCaballo(self, nombre, edad, genero):
        Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1

    def crearLeon(self, nombre, edad, genero):
        Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas