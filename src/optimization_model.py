from scipy.optimize import linprog
import numpy as np
#linprog minimiza por defecto
class Modelo():
    def __init__(self, array):
        self.array = array
        #Se comprueba que el array sea válido
        if len(self.array) != 8:
            raise ValueError(f"El array debe tener exactamente 8 elementos, pero tiene {len(self.array)}.")
        
        if not np.issubdtype(self.array.dtype, np.number):
            raise TypeError("El array debe contener únicamente valores numéricos (float o int).")
        
    def solution(self):
        #verificar que es un array de 8 elementos y solo números (float o int)
        
        #como el modelo minimiza, se multiplica por -1
        self.C = self.array[-2:]*-1
        #es de la forma Ax <= b
        self.A = [[self.array[0],self.array[2]],[self.array[1],self.array[3]]]
        self.B = [self.array[4],self.array[5]]
        self.x_bounds = (0, None)  # x >= 0
        self.y_bounds = (0, None)  # y >= 0
        self.results = linprog(
            self.C,
            A_ub=self.A,
            b_ub=self.B,
            bounds=[self.x_bounds, self.y_bounds],
            method='simplex'
        )
        if self.results.success:
            return self.results
        else:
            print("No se pudo encontrar una solución: ", self.results.message)
            return None
       