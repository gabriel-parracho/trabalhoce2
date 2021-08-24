from core import MatrixFunctions,NetlistParser,ComponentFunctions,Solver,ComplexFunctions


def Main():
    #opening file
    fileNetlist = NetlistParser.openNetlist('netlist.txt')
    #creating empty matrix and vector
    GmMatrix=MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes('netlist.txt'))
    IVector=MatrixFunctions.makeIVector(NetlistParser.checkNumberOfNodes('netlist.txt'))
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
        print(GmMatrix)
        print(IVector)
        print("e: ",EMatrix)

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
        print(GmMatrix)
        print(IVector)
        print("e: ",EMatrix)

    # #adding components
    # GmMatrix=ComponentFunctions.addResistor(GmMatrix,fileNetlist)
    # GmMatrix=ComponentFunctions.addCurrentSourceVcontrolled(GmMatrix,fileNetlist)
    # IVector=ComponentFunctions.addCurrentSource(IVector,fileNetlist)
    # #fixing ground
    # GmMatrix,IVector =MatrixFunctions.fixGround(GmMatrix,IVector)
    # EMatrix= Solver.solveSystem(GmMatrix,IVector)


    # print(GmMatrix)
    # print(IVector)
    # print("e: ",EMatrix)
    # # print("abaixo é a fixed")
    # # MatrixFunctions.fixGround(GmMatrix,IVector)
    # # fileNetlist = NetlistParser.openNetlist('netlist.txt')
    # # operationType = int(input('Insira o tipo de operação: \n 1 - Tensões nodais simples\n\
    # #                             2 - Tensões nodais fasores em RP\n'))

    # # if (operationType==1):
    # #     #inserir 
    # #     pass
    # # if (operationType==2):
    # #     #inserir
    # #     pass

Main()