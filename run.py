from core import MatrixFunctions,NetlistParser

fileNetlist = NetlistParser.openNetlist('netlist.txt')
print(NetlistParser.checkNumberOfNodes('netlist.txt'))
MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes('netlist.txt'))



def Main():
    MatrixFunctions.makeMatrix(NetlistParser.checkNumberOfNodes('netlist.txt'))
    operationType = int(input('Insira o tipo de operação: \n 1 - Tensões nodais simples\n\
                                2 - Tensões nodais fasores em RP\n'))

    if (operationType==1):
        #inserir 
        pass
    if (operationType==2):
        #inserir
        pass
    
