import numpy as np

class Csvtodf():
    #Inicialización de la clase con el path del archivo csv
    def __init__(self, file_path):
        self.file_path = file_path
        self.array = None
    #se lee el csv y se convierte a un df de pandas
    def csv_to_array(self):
        try:
            self.array = np.genfromtxt(self.file_path, delimiter=",", skip_header=0)
            if self.array is not None:
                return self.array #se retornan los valores únicamente
        except Exception as e:
            print(f"No se pudo leer el archivo CSV: {e}")
            return None
