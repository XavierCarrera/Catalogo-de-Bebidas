class underline:
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Bebidas:

    def __init__(self, nombre, precio, grado_alcohol):
        self.nombre = nombre
        self.precio = precio
        self.grado_alcohol = grado_alcohol

    def __str__(self):

        return "\n{} \n PRECIO: {} \n GRADO ALCOHOL: {}".format(self.nombre, self.precio, self.grado_alcohol)

class Cerveza(Bebidas):

    def __init__(self, nombre, precio, grado_alcohol, tipo_cerveza):
        super().__init__(nombre, precio, grado_alcohol)
        self.tipo_cerveza = tipo_cerveza

    def __str__(self):

        return super().__str__() + "\n TIPO DE CERVEZA: {}".format(self.tipo_cerveza)

class  Oscura(Cerveza):

    def __init__(self, nombre, precio, grado_alcohol, tipo_cerveza, pais):
        super().__init__(nombre, precio, grado_alcohol, tipo_cerveza)
        self.pais = pais
        self._marca = None

    def __str__(self):

        return super().__str__() + "\n PAIS: {}".format(self.pais)

class  Clara(Cerveza):

    def __init__(self, nombre, precio, grado_alcohol, tipo_cerveza, pais):
        super().__init__(nombre, precio, grado_alcohol, tipo_cerveza)
        self.pais = pais

    def __str__(self):

        return super().__str__() + "\n PAIS: {}".format(self.pais)

class Vino(Bebidas):

    def __init__(self, nombre, precio, grado_alcohol, tipo_vino):
        super().__init__(nombre, precio, grado_alcohol)
        self.tipo_vino = tipo_vino

    def __str__(self):

        return super().__str__() + "\n TIPO DE VINO: {}".format(self.tipo_vino)

class Tinto(Vino):

    def __init__(self, nombre, precio, grado_alcohol, tipo_vino, pais):
        super().__init__(nombre, precio, grado_alcohol, tipo_vino)
        self.pais = pais

    def __str__(self):

        return super().__str__() + "\n AÑO DE CULTIVO: {}".format(self.pais)

class Blanco(Vino):

    def __init__(self, nombre, precio, grado_alcohol, tipo_vino, pais):
        super().__init__(nombre, precio, grado_alcohol, tipo_vino)
        self.pais = pais

    def __str__(self):

        return super().__str__() + "\n AÑO DE CULTIVO: {}".format(self.pais)

def run():

    
    lager = Oscura(underline.UNDERLINE  + "LAGER" + underline.END , "$2.40", "4.5 %", "Lager", "Alemania")
    pale_lager = Clara(underline.UNDERLINE  + "PALE LAGER" + underline.END, "$3.20", "3.1 %", "Lager", "Estados Unidos") 
    weissbier = Clara(underline.UNDERLINE  + "WEISSBIER" + underline.END, "$2.90", "5.0 %", "Dark lager", "Austria")
    irish_dry = Oscura(underline.UNDERLINE  + "IRSH DRY" + underline.END, "$4.80", "6.5 %", "Stout", "Irlanda")
    baltic_porter = Oscura(underline.UNDERLINE  + "BALTIC PORTER" + underline.END, "$3.50", "8.3 %", "Stout", "Rusia")
    sauvignon = Blanco(underline.UNDERLINE + "SAUVIGNON" + underline.END , "$5.60", "9.0 %", "Blanco", "Francia")
    muscat = Blanco(underline.UNDERLINE + "MUSCAT" + underline.END, "$6.70", "11.3 %", "Blanco", "Italia")
    malbec = Tinto(underline.UNDERLINE + "MALBEC" + underline.END, "$13.75", "12.4 %", "Tinto", "Argentina")
    pinot_noir = Tinto(underline.UNDERLINE + "PINOT NOIR" + underline.END, "$15.80", "14.8 %", "Tinto", "Francia")
    merlot = Tinto(underline.UNDERLINE + "MERLOT" + underline.END, "$13.30", "12.4 %", "Tinto", "Francia")

    print(lager.__str__())
    print(pale_lager.__str__())
    print(weissbier.__str__())
    print(irish_dry.__str__())
    print(baltic_porter.__str__())
    print(sauvignon.__str__())
    print(muscat.__str__())
    print(malbec.__str__())
    print(pinot_noir.__str__())
    print(merlot.__str__())

if __name__ == "__main__":
    run()