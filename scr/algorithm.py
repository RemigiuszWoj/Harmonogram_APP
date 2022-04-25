from collections import deque

class CArc():
    """
    CArc class;
    :param: nd;
    :param: weight; 
    """
    def __init__(self, nd:int = 0, weight:int = 0) -> None:
        self.nd = nd
        self.weight = weight

class CRes():
    """
    CRes class;
    :param: id;
    :param: number; 
    """
    def __init__(self, id:int = 0, number:int = 0) -> None:
        self.id = id
        self.number = number

class CGraph():
    """
    CGraph class;
    :param: n;
    :param: Succ; 
    :param: Pred; 
    :param: Res; 
    """
    def __init__(self, np:int=0) -> None:

        self.n = np 
        self.Succ = list()
        self.Pred = list()
        self.Res = list()
        self.p = list()
        self.job = list() 

        for _ in range(self.n + 1):
            self.Succ.append([])

        for _ in range(self.n + 1):
            self.Pred.append([])

        for _ in range(self.n + 1):
            self.Res.append([])

        for _ in range(self.n + 1):
            self.p.append(0)

        for _ in range(self.n + 1):
            self.job.append(0)

    def TOP_ORDER(self) -> list:
        LP = [None] * (self.n + 1)
        for i in range(1,self.n + 1, 1):
            LP[i] = len(self.Pred[i])

        Q = deque()
        for i in range(1,self.n + 1, 1):
            if LP[i] == 0:
                Q.appendleft(i)

        ORD = []
        ORD.append(0)
        while len(Q) > 0:
            nd = Q.pop()
            ORD.append(nd)
            for arc in self.Succ[nd]:
                LP[arc.nd] = LP[arc.nd] - 1
                if LP[arc.nd]  == 0:
                    Q.appendleft(arc.nd)

        return ORD        

    def Harm(self, ord:list) -> list:

        S = [None] * (self.n + 1 )
        S[0] = 0

        for i in range(1, self.n + 1):
            nd = ord[i]
            sm = 0
            for arc in self.Pred[nd]:
                if (sm < S[arc.nd] + self.p[arc.nd] + arc.weight):
                    sm = S[arc.nd] + self.p[arc.nd] + arc.weight
            S[nd] = sm
        return S
