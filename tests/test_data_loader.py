from src.data_loader import Csvtodf
import unittest
import numpy as np

#Test para ver si se cargó correctamente el archivo a un nparray
class TestCsvtoArray(unittest.TestCase):

    def test_csv_to_df(self):
        csv_path = "optimization_problem_data.csv"
        csv_reader = Csvtodf(csv_path)
        array = csv_reader.csv_to_array()

        # Verificar que se cargó correctamente comparando con la carga directa
        expected_array = np.genfromtxt(csv_path, delimiter=",", skip_header=0)
        np.testing.assert_array_equal(array, expected_array)

    # def test_incorrect_path(self):
    #     csv_path = "optimation_problem_datacsv"
    #     csv_reader = Csvtodf(csv_path)
    #     with self.assertRaises(Exception):
    #         csv_reader.csv_to_array()
