import numpy as np
from numba import float32
from numba.experimental import jitclass

spec=[
      ('x_range', float32[:]),
      ('y_range', float32[:]),
      ('minima', float32),
      ('location', float32[:,:]),
]

@jitclass(spec)
class Ackley:
    def __init__(self):
        self.x_range = np.array([-5,5], dtype=np.float32)
        self.y_range = np.array([-5,5], dtype=np.float32)
        self.minima = 0,0
        self.location = np.array([0,0], dtype=np.float32).reshape(1,2)
        
def Query(self, x, y):
    z= -20*np.exp(-0.2*np.sqrt(0.5*(x**2 + y**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.exp(1) + 20
    
    return z