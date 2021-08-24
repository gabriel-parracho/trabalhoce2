import cmath

class ComplexFunctions:
        def __init__(self):
                pass
        
        #assuming the system has only one freq
        def getFreq(fileNetlist):
                for i in range (len(fileNetlist)):
                        if(fileNetlist[i][0] == 'I'):
                                parser = (fileNetlist[i].split())
                                if (parser[3]) == 'SIN':
                                        return float(parser[5])
                return None

        def addSinCurrentSource(IVector,fileNetlist):
                for i in range (len(fileNetlist)):
                        if (fileNetlist[i][0] == 'I'):
                                parser=(fileNetlist[i].split())
                                if (parser[3]) == 'SIN':
                                        nodeA= int(parser[1])
                                        nodeB= int(parser[2])
                                        A = float(parser[4])
                                        phase = float(parser[6])
                                        value = A*cmath.exp(1j*phase)
                                        IVector[(nodeA)] -= value
                                        IVector[(nodeB)] += value
                return IVector

        def addInductor(GmMatrix,fileNetlist,freq):
                inductors=[]
                for i in range (len(fileNetlist)):
                        if(fileNetlist[i][0] == 'L'):
                                inductors+=(fileNetlist[i].split())
                print (inductors)
                for i in range (int(len(inductors)/4)):
                        nodeA=int((inductors[4*i+1]))
                        nodeB=int((inductors[4*i+2]))
                        G=(1/(1j*freq*(float(inductors[4*i+3]))))
                        
                        GmMatrix[nodeA][nodeA] += G
                        GmMatrix[nodeB][nodeB] += G
                        GmMatrix[nodeA][nodeB] -= G
                        GmMatrix[nodeB][nodeA] -= G
                return GmMatrix

        def addCapacitor(GmMatrix,fileNetlist,freq):
                capacitors=[]
                for i in range (len(fileNetlist)):
                        if(fileNetlist[i][0] == 'C'):
                                capacitors+=(fileNetlist[i].split())
                print (capacitors)
                for i in range (int(len(capacitors)/4)):
                        nodeA=int((capacitors[4*i+1]))
                        nodeB=int((capacitors[4*i+2]))
                        G=((1j*freq*(float(capacitors[4*i+3]))))
                        
                        GmMatrix[nodeA][nodeA] += G
                        GmMatrix[nodeB][nodeB] += G
                        GmMatrix[nodeA][nodeB] -= G
                        GmMatrix[nodeB][nodeA] -= G
                return GmMatrix

        def addTransformer(GmMatrix,fileNetlist,freq):
                transformers=[]
                for i in range (len(fileNetlist)):
                        if(fileNetlist[i][0] == 'K'):
                                transformers+=(fileNetlist[i].split())
                print (transformers)
                for i in range (int(len(transformers)/8)):
                        nodeA=int((transformers[4*i+1]))
                        nodeB=int((transformers[4*i+2]))
                        Inductance1=float((transformers[4*i+3]))
                        nodeC=int((transformers[4*i+4]))
                        nodeD=int((transformers[4*i+5]))
                        Inductance2=float((transformers[4*i+6]))
                        M = float((transformers[4*i+7]))

                        T11 = Inductance2/((Inductance1*Inductance2)-(M**2))
                        T22 = Inductance1/((Inductance1*Inductance2)-(M**2))
                        T12 = -M/((Inductance1*Inductance2)-(M**2))

                        GmMatrix[nodeA][nodeA] += T11/(1j*freq)
                        GmMatrix[nodeA][nodeB] -= T11/(1j*freq)
                        GmMatrix[nodeA][nodeC] += T12/(1j*freq)
                        GmMatrix[nodeA][nodeD] -= T12/(1j*freq)

                        GmMatrix[nodeB][nodeA] -= T11/(1j*freq)
                        GmMatrix[nodeB][nodeB] += T11/(1j*freq)
                        GmMatrix[nodeB][nodeC] -= T12/(1j*freq)
                        GmMatrix[nodeB][nodeD] += T12/(1j*freq)

                        GmMatrix[nodeC][nodeA] += T12/(1j*freq)
                        GmMatrix[nodeC][nodeB] -= T12/(1j*freq)
                        GmMatrix[nodeC][nodeC] += T22/(1j*freq)
                        GmMatrix[nodeC][nodeD] -= T22/(1j*freq)

                        GmMatrix[nodeD][nodeA] -= T12/(1j*freq)
                        GmMatrix[nodeD][nodeB] += T12/(1j*freq)
                        GmMatrix[nodeD][nodeC] -= T22/(1j*freq)
                        GmMatrix[nodeD][nodeD] += T22/(1j*freq)

                return GmMatrix