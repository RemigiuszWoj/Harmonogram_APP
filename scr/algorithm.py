#Base algorithm file


from collections import deque
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

        self.n = np

        self.Succ = list()
        
        self.Pred = list()

        self.Res = list()

        self.p = list()

        # for _ in range(1, self.n + 1, 1):
        for _ in range(self.n + 1):
            self.Succ.append([])

        for _ in range(self.n + 1):
        # for _ in range(1, self.n + 1, 1):
            self.Pred.append([])

        for _ in range(self.n + 1):
        # for _ in range(1, self.n + 1, 1):
            self.Res.append([])

        for _ in range(self.n + 1):
        # for _ in range(1, self.n + 1, 1):
            self.p.append(0)

        # print(self.Succ)
        # print(self.Pred)
        # print(self.Res)
        # print(self.p)

    def TOP_ORDER(self) -> list:
        LP = [None] * (self.n + 1)
        for i in range(1,self.n + 1, 1):
            LP[i] = len(self.Pred[i])

        # print(LP)

        Q = deque()
        for i in range(1,self.n + 1, 1):
            if LP[i] == 0:
                Q.appendleft(i)
       
        # print(Q)

        ORD = []
        ORD.append(0)
        while len(Q) > 0:
            nd = Q.pop()
            ORD.append(nd)
            for arc in self.Succ[nd]:
                LP[arc.nd] = LP[arc.nd] - 1
                if LP[arc.nd]  == 0:
                    Q.appendleft(arc.nd)
        # print(ORD)
        return ORD        

    def Harm(self, ord:list) -> list:
        #Czemu n+1?
        S = [None] * (self.n + 1 )
        S[0] = 0

        # print("len S: ", len(S))
        # print("len ord: ", len(ord))


        # for i in range(1,self.n + 1, 1):
        for i in range(1, self.n + 1):
        
            # print(i)

            nd = ord[i]
            sm = 0
            for arc in self.Pred[nd]:
                # print("arc.nd", arc.nd, " ",  S[arc.nd]," ",  self.p[arc.nd]," ", arc.weight)


                if (sm < S[arc.nd] + self.p[arc.nd] + arc.weight):
                    sm = S[arc.nd] + self.p[arc.nd] + arc.weight
            S[nd] = sm
        return S


def PARSOWANIE_DANYCH(path:str ="dryer_50_t.csv"):
    
    file = data_csv.preprocesData(path=path)
    file.preper_file()

    G = CGraph(len(file.file_to_dict["lp"]))
    # print(G.n)
    # print(file.file_to_dict["Czas wykonania"])

    for i in range(G.n):

        # 0 na początku czy na koncu?

        # G.p[i] = int(file.file_to_dict["Czas wykonania"][i])
        G.p[i + 1] = int(file.file_to_dict["Czas wykonania"][i])

    # print(G.p)


    stringSeparators = [" and "]
    for i in range(1, G.n + 1, 1):
        sp = file.file_to_dict["Wymaga zakonczenia"][i - 1].split(*stringSeparators)
        
        # print("sp: ", sp)
        
        for s in sp:
            spx = s.split("(")
            nd = int(spx[0])
            
            # print("nd: ", nd)

            if nd == 0:
                continue
            weight = int(eval(spx[1].replace(")", "")))

            # print("weight: ", weight)

            a = CArc(nd=i, weight=weight)
            # G.Succ[nd] = a
            G.Succ[nd].append(a)

            
            # print(" G.Succ[nd]: ",  G.Succ[nd])

            b = CArc(nd=nd, weight=weight)
            # G.Pred[i] = b
            G.Pred[i].append(b)
            # print("i:" ,i)
            # print("nd: ,", nd, "weight: ", weight)
            # print("G.Pred[i]: ", G.Pred[i])

    # print(" G.Succ: ",  G.Succ)
    # print("G.Pred: ", G.Pred)
#### To do coś ie działa z przedziałami

        sp = file.file_to_dict["Pracownicy"][i - 1].split(" ")

        # print("sp: ", sp)

        for s in sp:
            if s == "":
                continue
            spx = s.split("x")

            # print("spx: ", spx)

            nbr = int(spx[0])
            id = str(spx[1])

            # print("nbr: ", nbr)
            # print("id: ", id)

            r = CRes(id=id, number=nbr)
            
            G.Res[i] = r

    # print(G.Res)

    return G
                

G = PARSOWANIE_DANYCH(path ="dryer_50_t.csv")
# print(G.Succ[5][0].nd)
# print(G.Succ[5][1].nd)
# print(G.Succ[5][2].nd)

ord = G.TOP_ORDER()

H = G.Harm(ord=ord)

print("H: ", H)

# Test = CGraph(np=2)
# print(Test.TOP_ORDER())