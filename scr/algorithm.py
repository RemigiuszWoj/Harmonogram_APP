#Base algorithm file


from collections import deque
from copy import deepcopy
import data_csv

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

        self.pomPred = CArc()
        self.Pred = list()

        self.pomRes = CRes()
        self.Res = list()

        self.p:list[int] = list()

        for _ in range(self.n):
            #moe być od 0 do n #########################################
        # for _ in range(1,self.n + 1, 1):
            self.Succ.append(self.pomSucc)
            self.Pred.append(self.pomPred)
            self.Res.append(self.pomRes)
            self.p.append(0)


    def TOP_ORDER(self) -> list:
        # LP = [None] * (self.n + 1)
        LP = [None] * (self.n)
        # print("LP",len(LP))
        # print(LP[0])
        # print(self.Pred[1])
        # for i in range(self.n + 1):
        for i in range(self.n):
            # print("i",i)
            #co tu sie ma dziać?#######################################
            # LP[i] = self.Pred[i]
            LP[i] = 1
            # print(LP[i])
        Q = deque()
        for i in range(self.n):
            if LP[i] == 0:
                Q.appendleft(i)
        
        ORD = []
        ORD.append(0)
        while len(Q) > 0:
            nd = Q.pop()
            ORD.append(nd)
            for arc in self.Succ[nd]:
                if LP[arc.nd] - 1 == 0:
                    Q.appendleft(arc.nd)
        return deepcopy(ORD)


    def Harm(self, ord:list) -> list:
        S = [None] * (self.n)
        S[0] = 0
        for i in range(self.n):
            nd = ord[i]
            sm = 0
            for arc in self.Pred[nd]:
                if (sm < S[arc.nd] + self.p[arc.nd] + arc.weight):
                    sm = S[arc.nd] + self.p[arc.nd] + arc.weight
            S[nd] = sm
        return S




# G = CGraph()
# H = list(None)

###########Dopisac dodawanie ; na koncu wiersza ######################

def PARSOWANIE_DANYCH(path:str ="dryer_50_t.csv"):
    # wczytanie i podział danych do dogadania#########################
    file = data_csv.preprocesData(path=path)
    file.preper_file()
    # print(file.header)
    # print(file.file_to_dict)
    G = CGraph(len(file.file_to_dict["lp"]))
    # print(G.n)
    for i in range(G.n):
        G.p[i] = file.file_to_dict["Czas wykonania"][i]
        # print(G.p[i])
    stringSeparators = [" and "]
    for i in range(G.n):
        sp = file.file_to_dict["Wymaga zakonczenia"][i].split(*stringSeparators)
        # print(sp)
        for s in sp:
            # print(i)
            # print(s)
            spx = s.split("(")
            # print(spx)
            nd = int(spx[0])
            # print("nd: ", nd)
            if nd == 0:
                continue
            weight = int(eval(spx[1].replace(")", "")))
            # print("weight: ", weight)

            a = CArc(nd=i, weight=weight)
            G.Succ[nd] = a
            # print( G.Succ[nd])
            b = CArc(nd=nd, weight=weight)
            G.Pred[i] = b
            # print(G.Pred[i])
        sp = file.file_to_dict["Pracownicy"][i].split(" ")
        for s in sp:
            if s == "":
                continue
            spx = s.split("x")
            nbr = int(spx[0])
            # print("nbr: ", nbr)
            id = str(spx[1])
            # print("id: ", id)
            r = CRes(id=id, number=nbr)
            G.Res[i] = r
    return G



            

G = PARSOWANIE_DANYCH()

ord = G.TOP_ORDER()

# H = G.Harm(ord=ord)










# a =CGraph(3)
# print("Succ",len(a.Succ))
# print("Pred",len(a.Pred))
# print("Res",len(a.Res))

# a.TOP_ORDER()
