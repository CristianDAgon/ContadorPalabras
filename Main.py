
from Archivo import Archivo
from Carpeta import Carpeta

class Main:

    #Instaciamos la clase correspondiente para la ejecucion de las pruebas
    ruta = "incorrecta"
    palabra_busqueda = "ejemplo"


    carpeta = Carpeta(ruta, palabra_busqueda)
    carpeta.buscarCarpetaArchivo()

if __name__ == "__main__":
    main = Main()