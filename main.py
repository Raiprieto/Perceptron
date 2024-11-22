import numpy as np
from src.data_loader import Csvtodf  
from src.optimization_model import Modelo  
from src.visualizer import ModeloVisual
import sys 

class Programa():
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.csv_path = args[0]
        else:
            raise ValueError("Debes proporcionar la ruta al archivo CSV como argumento.")
        self.verbose = kwargs.get("verbose", True)
        
    def ejecutar(self):
        try:
            # Paso 1: Leer el archivo CSV
            print("Cargando datos desde el archivo CSV...")
            csv_reader = Csvtodf(self.csv_path)
            array = csv_reader.csv_to_array()

            try:
                array = array[1]  #la segunda fila contiene los parámetros
                if self.verbose:
                    print("Datos cargados correctamente:", array)
            except IndexError:
                print("El archivo CSV no contiene suficientes filas.")
                return
            print("Inicializando el modelo...")
            modelo = Modelo(array)
            resultados = modelo.solution()

            # Mostrar resultados
            print("\nResultados del Modelo:")
            print(f"Valores óptimos de las variables: x_A = {resultados.x[0]:.2f}, x_B = {resultados.x[1]:.2f}")
            print(f"Valor óptimo de la función objetivo: Z = {-resultados.fun:.2f}")

            # Paso 3: Generar el gráfico
            print("\nGenerando el gráfico...")
            visual = ModeloVisual(array)
            visual.solution()
            visual.plot_solution()
            print("Gráfico generado exitosamente.")

        except Exception as e:
            print(f"Error durante la ejecución del programa: {e}")

        
if __name__ == "__main__":
    # Leer argumentos desde la línea de comandos
    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_al_csv>")
        sys.exit(1)

    # Crear una instancia del programa con el archivo proporcionado
    programa = Programa(sys.argv[1])
    programa.ejecutar()

