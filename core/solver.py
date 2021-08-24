import numpy as np 

class Solver:

    def __init__(self):
                pass
    
    def solveSystem(GmMatrix,IVector):
        Gm=np.array(GmMatrix)
        I=np.array(IVector)

        e=np.linalg.solve(Gm,I)

        return e