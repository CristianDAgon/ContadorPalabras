import os
from Archivo import Archivo


class Carpeta:

    def __init__(self, ruta: str, palabraBuscada: str):
        self.ruta = ruta
        self.palabraBuscada = palabraBuscada

    # Validamos de que lo que nos este entrando como ruta sea una ruta correcta de una carpeta
    def buscarCarpetaArchivo(self):
        if not os.path.exists(self.ruta) or not os.path.isdir(self.ruta):
            print(f'La ruta "{self.ruta}" no existe o no es una carpeta.')

        #Listamos todos los archivo que hay en esa ruta
        archivosCarpeta =  os.listdir(self.ruta)
        #Validamos de que la carpeta no este vacia
        if archivosCarpeta == None or len(archivosCarpeta) == 0:
            print("La carpeta se encuentra vacia")
            return

        #A rutaArchivo es igual a la construccion de la ruta, la ruta del archivo se crea mediante
        #el path.join con la ruta principal mas la de cada archivo
        contador = 0
        for archivo in archivosCarpeta:
            rutaArchivo = os.path.join(self.ruta, archivo)
        #validamos de que cada archivo si sea un file y de que termine con las extensiones correspondientes
            if (os.path.isfile(rutaArchivo) and (archivo.endswith(".txt") or archivo.endswith(".xml") or
            archivo.endswith(".json") or archivo.endswith(".csv"))):
                #open , abre el archivo en modo lectura , buscando la palabra que necesitamos
                if self.palabraBuscada in open(rutaArchivo, 'r').read():
                     #este contador va a ser igual , a lo que  retorna el metodo contador palabra
                     #que devuelve las veces que esta la palabra en el archivo
                     contadorPalabra_archivo = Archivo(rutaArchivo, self.palabraBuscada).contadorPalabra()
                     print("La palabra", self.palabraBuscada, "esta", contadorPalabra_archivo, "veces en", archivo)
                     contador += contadorPalabra_archivo
            else:
                    print("No se encontro ningun archivo de texto")


        print("La palabra", self.palabraBuscada, " se repite un total de ", contador, " veces")



