import json

class Producto:
    def __init__(self, nombre, precio, cantidad, esLiquido, marca, calificacion):
        self._nombre       = nombre
        self._precio       = precio
        self._cantidad     = cantidad
        self._esLiquido    = esLiquido
        self._marca        = marca
        self._calificacion = calificacion

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

        
    def toString(self):
        return self._nombre + self._marca