from core import MatrixFunctions,NetlistParser,ComponentFunctions,Solver,ComplexFunctions
import numpy as np


def Main():
    print("#"*80)
    print("Trabalho de Circuitos Elétricos 2\nAluno Gabriel Parracho dos Santos Leal\nProfessora Fernanda Duarte Vilela Reis de Oliveira")
    print("#"*80)
    filename=str(input('Insira o nome da netlist a ser analisada (incluindo o .txt): '))
    print("#"*80)

    #opening file
    fileNetlist = NetlistParser.openNetlist(filename)
    #creating empty matrix and vector
    GmMatrix=MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes(filename))
    IVector=MatrixFunctions.makeIVector(NetlistParser.checkNumberOfNodes(filename))
    #checking system type trying to get freq
    freq=ComplexFunctions.getFreq(fileNetlist)
    if freq == None:
        operationType = 1
    else:
        operationType = 2

    if operationType == 1: # no frequency components
        #adding components
        GmMatrix=ComponentFunctions.addResistor(GmMatrix,fileNetlist)
        GmMatrix=ComponentFunctions.addCurrentSourceVcontrolled(GmMatrix,fileNetlist)
        IVector=ComponentFunctions.addCurrentSource(IVector,fileNetlist)
        #fixing ground
        GmMatrix,IVector =MatrixFunctions.fixGround(GmMatrix,IVector)
        #solving the system
        EMatrix= Solver.solveSystem(GmMatrix,IVector)

    elif operationType == 2:
        #adding passive components
        GmMatrix=ComponentFunctions.addResistor(GmMatrix,fileNetlist)
        GmMatrix=ComponentFunctions.addCurrentSourceVcontrolled(GmMatrix,fileNetlist)
        IVector=ComponentFunctions.addCurrentSource(IVector,fileNetlist)
        #adding reactive components
        IVector=ComplexFunctions.addSinCurrentSource(IVector,fileNetlist)
        GmMatrix=ComplexFunctions.addInductor(GmMatrix,fileNetlist,freq)
        GmMatrix=ComplexFunctions.addCapacitor(GmMatrix,fileNetlist,freq)
        GmMatrix=ComplexFunctions.addTransformer(GmMatrix,fileNetlist,freq)
        #fixing ground
        GmMatrix,IVector =MatrixFunctions.fixGround(GmMatrix,IVector)
        #solving the system
        EMatrix= Solver.solveSystem(GmMatrix,IVector)
    #Matrix printing
    print("\nGm Matrix:")
    print(np.array(GmMatrix),"\n")
    print("-"*80)
    # print(GmMatrix)
    print("I Vector: ")
    print(np.array(IVector), "\n")
    print("-"*80)

    print("e Array: ")
    print(np.array(EMatrix), "\n")
    print("-"*80)


Main()