from collections import deque
from array import array

# from pydantic import NoneBytes

class Graph:
    n = 0
    W = []
    Pred = []
    Succ = []

    def __init__(self, n):
        self.n = n
        for i in range(n+1):
            self.Pred.append([])
            self.Succ.append([])
        for i in range(n+1):
            self.W.append(0)
        
    def AddArc(self, snode, dnode): # snode - nr skad prowadzi luk, dnode - dokad prowadzi luk
        self.Succ[snode].append(dnode)
        self.Pred.append([dnode,snode])

    def TopOrder(self):
        LP = []
        LP.append(None)
        for i in range(1,self.n+1):
            LP.append(len(self.Pred[i]))
            # print(LP[i])
        Q = deque()
        for i in range(1,self.n+1):
            if LP[i] == 0:
                Q.append(i)
        ORD = []
        ORD.append(0)
        while len(Q)>0:
            op = Q.popleft()
            ORD.append(op)
            for ns in self.Succ[op]:
                LP[ns] -= 1
                if LP[ns] ==0:
                    Q.append(ns)
        return ORD

        
        

# G = Graph(2)
# G.TopOrder()