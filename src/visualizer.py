import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from src.optimization_model import Modelo

class ModeloVisual(Modelo): 
    def __init__(self, array):
        super().__init__(array)  # Inicializa la clase padre

    def plot_solution(self):
        
        # Definir las restricciones
        x = np.linspace(0, 15, 400)  # Valores para x
        y1 = (self.B[0] - self.A[0][0] * x) / self.A[0][1]  # Restricción 1
        y2 = (self.B[1] - self.A[1][0] * x) / self.A[1][1]  # Restricción 2

        # Región factible
        y = np.minimum(y1, y2)
        y[y < 0] = 0 

        # Gráfico
        plt.figure(figsize=(8, 6))

        # Dibujar restricciones
        plt.plot(x, y1, label="Restricción 1", color="blue")
        plt.plot(x, y2, label="Restricción 2", color="green")

        # Dibujar región factible
        plt.fill_between(x, 0, y, where=(y >= 0), color="gray", alpha=0.3, label="Región factible")

        # Dibujar solución óptima
        if self.results.success:
            plt.scatter(self.results.x[0], self.results.x[1], color="red", label="Solución óptima")
            plt.text(self.results.x[0], self.results.x[1],
                     f"({self.results.x[0]:.2f}, {self.results.x[1]:.2f})",
                     fontsize=10, ha='right')

        # Etiquetas y leyenda
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Visualización del Modelo de Optimización")
        plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
        plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
        plt.legend()
        plt.grid()
        plt.show()

    def print_initial_data(self):
        
        print("Datos Iniciales del Modelo:")
        print(f"C (Función objetivo): {self.C}")
        print(f"A (Restricciones): {self.A}")
        print(f"B (Lado derecho de las restricciones): {self.B}")
        print(f"Bounds: x >= {self.x_bounds[0]}, y >= {self.y_bounds[0]}")