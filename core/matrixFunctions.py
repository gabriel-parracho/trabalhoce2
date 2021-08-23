import numpy as np


class MatrixFunctions:
    def __init__(self):
        pass
        
    #create a square matrix node x node
    def makeMatrix(nodes):
        matrix = []
        for i in range(nodes):
            for j in range(nodes):
                matrix.append([0])
        print(matrix)