import numpy as np


class MatrixFunctions:
    def __init__(self):
        pass
        
    #create a square matrix node x node, including ground, for algorithm purposes
    def makeMatrix(nodes):
        matrix=[]
        for i in range(0,nodes+1,1):
            matrix.append([])
            for j in range(0,nodes+1,1):
                matrix[i].append(0)
        return matrix

    #create a vector for currents
    def makeIVector(nodes):
        IVector = []
        for i in range(0,nodes+1,1):
            IVector.append(0)
        return IVector
    
    #remove the ground nodes from GmMatrix and IVector to make possible system solving
    def fixGround(GmMatrix,IVector):
        GmMatrix.pop(0)
        IVector.pop(0)

        for i in range (len(GmMatrix)):
            GmMatrix[i].pop(0)


        return GmMatrix,IVector

