class CArc(object):
    def __init__(self):
        self.nd = None
        self.weight = None
class CRes(object):
    def __init__(self):
        self.id = None
        self.number = None
class CGraph(object):
    def __init__(self):
        self.n = None
        self.Succ = None
        self.Pred = None
        self.Res = None
        self.p = None
        self.p = None
    def init(self, np):
        n = np
        Succ = []
        i = 1
        while (i <= n):
            Succ[i] = List[CArc]()
            i += 1
        Pred = []
        i = 1
        while (i <= n):
            Pred[i] = List[CArc]()
            i += 1
        Res = []
        i = 1
        while (i <= n):
            Res[i] = List[CRes]()
            i += 1
        p = []
        i = 0
        while (i <= n):
            p[i] = 0
            i += 1
    def TOP_ORDER(self):
        LP = []
        i = 1
        while (i <= n):
            LP[i] = Pred[i].Count
            i += 1
        Q = Queue[int]()
        i = 1
        while (i <= n):
            if (LP[i] == 0):
                Q.Enqueue(i)
            i += 1
        ORD = List[int]()
        ORD.Add(0)
        while (Q.Count > 0):
            nd = Q.Dequeue()
            ORD.Add(nd)
