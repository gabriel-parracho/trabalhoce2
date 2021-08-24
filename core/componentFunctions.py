

class ComponentFunctions:
        def __init__(self):
                pass

        def addResistor(GmMatrix,fileNetlist):
                resistors=[]
                for i in range (len(fileNetlist)):
                        if(fileNetlist[i][0] == 'R'):
                                resistors+=(fileNetlist[i].split())
                print (resistors)
                for i in range (int(len(resistors)/4)):
                        nodeA=int((resistors[4*i+1]))
                        nodeB=int((resistors[4*i+2]))
                        G=(1/float((resistors[4*i+3])))
                        
                        GmMatrix[nodeA][nodeA] += G
                        GmMatrix[nodeB][nodeB] += G
                        GmMatrix[nodeA][nodeB] -= G
                        GmMatrix[nodeB][nodeA] -= G
                return GmMatrix


        def addCurrentSource(IVector,fileNetlist):
                for i in range (len(fileNetlist)):
                        if (fileNetlist[i][0] == 'I'):
                                parser=(fileNetlist[i].split())
                                if (parser[3]) == 'DC':
                                        nodeA= int(parser[1])
                                        nodeB= int(parser[2])
                                        value= int(parser[4])
                                        IVector[(nodeA)] += -value
                                        IVector[(nodeB)] += value
                return IVector

        def addCurrentSourceVcontrolled(GmMatrix,fileNetlist):
                for i in range (len(fileNetlist)):
                        if (fileNetlist[i][0] == 'G'):
                                parser=(fileNetlist[i].split())
                                nodeA= int(parser[1])
                                nodeB= int(parser[2])
                                Vc= int(parser[3])
                                Vd= int(parser[4])
                                Transconductance = float(parser[5])
                                GmMatrix[nodeA][Vc] += Transconductance
                                GmMatrix[nodeA][Vd] -= Transconductance
                                GmMatrix[nodeB][Vc] -= Transconductance
                                GmMatrix[nodeB][Vd] += Transconductance
                return GmMatrix
