

class NetlistParser:
    def __init__(self):
        pass

    def openNetlist(fileName):
        #file reading
        with open(fileName) as f:
            fileNetlist = f.read().splitlines()
        print(fileNetlist)
        return fileNetlist
        
    def checkNumberOfNodes(fileName):
        fileNetlist=NetlistParser.openNetlist(fileName)
        nodes=0
        for i in range (len(fileNetlist)):
            if (int((fileNetlist[i][3])) > nodes):
                nodes=int(fileNetlist[i][3])
            if (int((fileNetlist[i][5])) > nodes):
                nodes=int(fileNetlist[i][5])
        return nodes

