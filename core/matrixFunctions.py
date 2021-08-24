import numpy as np


class MatrixFunctions:
    def __init__(self):
        pass
        
    #create a square matrix node x node
    def makeMatrix(nodes):
        matrix = [[0]*nodes]*nodes
        return matrix

    #create a vector for currents
    def makeIVector(nodes):
        IVector = [0]*nodes

        return IVector