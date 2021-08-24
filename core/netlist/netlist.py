

class NetlistParser:
    def __init__(self):
        pass

    def openNetlist(fileName):
        #file reading
        with open(fileName) as f:
            fileNetlist = f.read().splitlines()
        return fileNetlist
        
    def checkNumberOfNodes(fileName):
        fileNetlist=NetlistParser.openNetlist(fileName)
        nodes=0
        for i in range (len(fileNetlist)):
            parser=fileNetlist[i].split()
            print(parser)
            try:
                if (int(parser[1]) > nodes):
                    nodes=int(parser[1])
                if (int(parser[2]) > nodes):
                    nodes=int(parser[2])
            except:
                pass
        return nodes

