

class ComponentFunctions:
        def __init__(self):
                pass

        def addResistor(GmMatrix,fileNetlist):
                print(GmMatrix)
                for i in range(len(fileNetlist)):
                        print(fileNetlist[i][0])
                        if (fileNetlist[i][0] == 'R'):
                                parser=(fileNetlist[i].split())
                                print(parser)
                                nodeA= int(parser[1])
                                nodeB= int(parser[2])
                                R= int(parser[3])
                                
                                GmMatrix[nodeA-1][nodeA-1] += (1/R)
                                GmMatrix[nodeB-1][nodeB-1] += (1/R)


                                # if nodeA != 0:
                                #         GmMatrix[nodeA-1][nodeA-1] += 1/R
                                # if nodeB != 0:
                                #         GmMatrix[nodeB-1][nodeB-1] += 1/R
                                # if ((nodeA != 0) and (nodeB != 0)):
                                #         GmMatrix[nodeA-1][nodeB-1] += (1/R)*-1
                                #         GmMatrix[nodeB-1][nodeA-1] += (1/R)*-1
                return GmMatrix

        def currentSource(IVector,fileNetlist):
                print(IVector)
                for i in range (len(fileNetlist)):
                        if (fileNetlist[i][0] == 'I'):
                                parser=(fileNetlist[i].split())
                                nodeA= int(parser[1])
                                nodeB= int(parser[2])
                                value= int(parser[3])
                                if nodeA != 0:
                                        IVector[(nodeA-1)] += -value
                                if nodeB != 0:
                                        IVector[(nodeB-1)] += value
                return IVector