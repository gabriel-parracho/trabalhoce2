

class NetlistParser:
    def __init__(self):
        pass

    def openNetlist(fileName):
        with open(fileName) as f: # O with já fecha o arquivo após sua finalização (f.close)
            fileNetlist = f.read().splitlines()
        print(fileNetlist)
        
    def checkNumberOfNodes(fileNetlist):
        pass