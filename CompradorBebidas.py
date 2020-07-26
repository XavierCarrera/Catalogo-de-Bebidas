class EntradaTiendasBebidas:

    def __init__(self, menor):
        self.menor = menor
        self._edad = False

    @property
    def edad (self):
        return self._edad 

    @edad.setter
    def set_edad(self, mayor):
        if mayor is True:
            self._edad = True
        else:
            raise ValueError("Para comprar en la tienda se necesita tener 18 años y el comprador es menor")


cliente = EntradaTiendasBebidas(False)
print(cliente.edad)
cliente.set_edad = True
print(cliente.set_edad)