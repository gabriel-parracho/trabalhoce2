from core import MatrixFunctions,NetlistParser,ComponentFunctions

# print(NetlistParser.checkNumberOfNodes('netlist.txt'))
# MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes('netlist.txt'))



def Main():
    fileNetlist = NetlistParser.openNetlist('netlist.txt')
    GmMatrix=MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes('netlist.txt'))
    IVector=MatrixFunctions.makeIVector(NetlistParser.checkNumberOfNodes('netlist.txt'))
    GmMatrix=ComponentFunctions.addResistor(GmMatrix,fileNetlist)
    IVector=ComponentFunctions.currentSource(IVector,fileNetlist)
    print(GmMatrix)
    print(IVector)
    # fileNetlist = NetlistParser.openNetlist('netlist.txt')
    # operationType = int(input('Insira o tipo de operação: \n 1 - Tensões nodais simples\n\
    #                             2 - Tensões nodais fasores em RP\n'))

    # if (operationType==1):
    #     #inserir 
    #     pass
    # if (operationType==2):
    #     #inserir
    #     pass

Main()