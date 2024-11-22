from src.visualizer import ModeloVisual
from src.data_loader import Csvtodf
from src.optimization_model import Modelo
import unittest
import numpy as np


class TestModeloVisual(unittest.TestCase):
    def test_plot_solution(self):
        self.test_array = np.array([1.5, 2.0, 1.0, 1.5, 8.0, 10.0, 100, 80])
    
        self.modelo = ModeloVisual(self.test_array)
        # Resolver el modelo para garantizar que hay resultados
        self.modelo.solution()
        # Intentar generar el gráfico
        try:
            self.modelo.plot_solution()
        except Exception as e:
            self.fail(f"El método plot_solution lanzó una excepción: {e}")