from src.optimization_model import Modelo
import unittest
import numpy as np

class TestOptiModel(unittest.TestCase):
    
    def test_valid_input(self):
        array = [1.5,2.0,1.0,1.5,8.0,10.0,100,80]
        array = np.array(array)
        modelo = Modelo(array)
        np.testing.assert_array_equal(modelo.array, array)

    def test_invalid_number_of_parameters(self):
        array = [12,13,14]
        array = np.array(array)
        with self.assertRaises(ValueError):
            Modelo(array)

    def test_invalid_type(self):
        array = ["hola",13,14,12,11,1,1,23]
        array = np.array(array)
        with self.assertRaises(TypeError):
            Modelo(array)

    def test_invalid_type_and_number(self):
        array = ["hola",13,14]
        array = np.array(array)
        with self.assertRaises(ValueError):
            Modelo(array)

    def test_solution_infeasible(self):     
        array = [0, 0, 0, 0, -12, -12,-12, -12]
        array = np.array(array)
        modelo = Modelo(array)
        resultado = modelo.solution()
        # Verificar que no hay solución
        self.assertIsNone(resultado)

