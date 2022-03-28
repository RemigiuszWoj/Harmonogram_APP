#Base algorithm file

from urllib.request import CacheFTPHandler


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

        self.n:int = np
        
        self.pomSucc = CArc()
        self.Succ = list()
        for i in range(1,self.n + 1, 1):
            self.Succ.append(self.pomSucc)

        self.pomPred = CArc()
        self.Pred = list()
        for j in range(1,self.n + 1, 1):
            self.Pred.append(self.pomPred)

        self.pomRes = CRes()
        self.Res = list()
        for k in range(1,self.n + 1, 1):
            self.Res.append(self.pomRes)
        
        self.p:list[int] = list()
        for l in range(1,self.n + 1, 1):
            self.p.append(0)

a =CGraph(3)
print(a.n)
print(a.Succ[0].nd)
print(a.Pred)
print(a.Res)
print(a.p)

