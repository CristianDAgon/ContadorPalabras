import re

class Archivo:
    def __init__(self, archivo, palabraBuscada: str):
        self.archivo = archivo
        self.palabraBuscada = palabraBuscada



    def contadorPalabra(self) -> int:
        contador = 0
        #con el try aseguramos de que si hay alguna excepcion no nos arroje error
        #si no que nos muestre que fue lo que sucedio
        try:
            #abrimos el archivo, almacenamos todo en una variable contenido ya que este
            #se utilizara en contador , donde es una lista con diferentes metodos de so
            #el cual nos permite contar palabras excluyendo caracateres especiales
            with open(self.archivo, 'r') as archivo:
                contenido = archivo.read().lower()
                contador = len(re.findall(r'\b{}\b'.format(re.escape(self.palabraBuscada)),contenido))
        except Exception as e:
            print("Error generado al abrir el archivo", self.archivo)
        return contador