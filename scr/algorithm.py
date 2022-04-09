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
                if LP[arc.nd] - 1 == 0:
                    Q.appendleft(arc.nd)
        return ORD        

    def Harm(self, ord:list) -> list:
        #Czemu n+1?
        S = [None] * (self.n + 1 )
        S[0] = 0

        for i in range(1,self.n + 1, 1):
            nd = ord[i]
            sm = 0
            for arc in self.Pred[nd]:
                if (sm < S[arc.nd] + self.p[arc.nd] + arc.weight):
                    sm = S[arc.nd] + self.p[arc.nd] + arc.weight
            S[nd] = sm
        return S


def PARSOWANIE_DANYCH(path:str ="dryer_50_t.csv"):
    
    file = data_csv.preprocesData(path=path)
    file.preper_file()

    G = CGraph(len(file.file_to_dict["lp"]))

    # print(file.file_to_dict["Czas wykonania"])

    for i in range(G.n):

        # 0 na początku czy na koncu?

        # G.p[i] = int(file.file_to_dict["Czas wykonania"][i])
        G.p[i + 1] = int(file.file_to_dict["Czas wykonania"][i])

    # print(G.p)


    stringSeparators = [" and "]
    for i in range(1, G.n + 1):
    # for i in range(1, G.n + 1, 1):
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


            # print("G.Pred[i]: ", G.Pred[i])

    print(" G.Succ: ",  G.Succ)
    print("G.Pred: ", G.Pred)

#### To do coś ie działa z przedziałami


    # stringSeparators = [" and "]
    # for i in range(G.n):
    # # for i in range(1,G.n + 1, 1):
    #     sp = file.file_to_dict["Wymaga zakonczenia"][i].split(*stringSeparators)
    #     for s in sp:
    #         spx = s.split("(")
    #         nd = int(spx[0])
    #         if nd == 0:
    #             continue
    #         weight = int(eval(spx[1].replace(")", "")))
    #         a = CArc(nd=i, weight=weight)
    #         G.Succ[nd] = a
    #         b = CArc(nd=nd, weight=weight)
    #         G.Pred[i] = b
    #     sp = file.file_to_dict["Pracownicy"][i].split(" ")
    #     for s in sp:
    #         if s == "":
    #             continue
    #         spx = s.split("x")
    #         nbr = int(spx[0])
    #         id = str(spx[1])
    #         r = CRes(id=id, number=nbr)
    #         G.Res[i] = r
    # return G
        

# class CGraph():
#     """
#     CGraph class;
#     :param: n;
#     :param: Succ; 
#     :param: Pred; 
#     :param: Res; 
#     """
#     def __init__(self, np:int=0) -> None:

        # self.pomSucc = CArc()
        # self.Succ = list()

        # self.pomPred = CArc()
        # self.Pred = list()

        # self.pomRes = CRes()
        # self.Res = list()

        # self.p:list[int] = list()

        # for _ in range(self.n):
            #moe być od 0 do n ?#########################################
        # for _ in range(1,self.n + 1, 1):
        #     self.Succ.append(self.pomSucc)
        #     self.Pred.append(self.pomPred)
        #     self.Res.append(self.pomRes)
        #     self.p.append(0)


    # def TOP_ORDER(self) -> list:
    #     LP = [None] * (self.n + 1)
    #     # LP = [None] * (self.n)
    #     for i in range(self.n):
    #     # for i in range(1,self.n + 1, 1):
    #         #co tu sie ma dziać?######################################            
    #         # LP[i] = self.Pred[i]
    #         # LP[i] = len(self.Pred[i])
    #         LP[i] = 1
    #         # print(LP[i])
    #     Q = deque()
    #     for i in range(self.n):
    #     # for i in range(1,self.n + 1, 1):
    #         if LP[i] == 0:
    #             Q.appendleft(i)
    #     ORD = []
    #     ORD.append(0)
    #     while len(Q) > 0:
    #         nd = Q.pop()
    #         ORD.append(nd)
    #         for arc in self.Succ[nd]:
    #             if LP[arc.nd] - 1 == 0:
    #                 Q.appendleft(arc.nd)
    #     # Czemu zwracamy kopie? ##############
    #     return deepcopy(ORD)
    #     # return ORD


    # def Harm(self, ord:list) -> list:
    #     #Czemu n+1?
    #     S = [None] * (self.n + 1 )
    #     S[0] = 0
    #     for i in range(self.n):
    #     # for i in range(1,self.n + 1, 1):
    #         nd = ord[i]
    #         sm = 0
    #         for arc in self.Pred[nd]:
    #             if (sm < S[arc.nd] + self.p[arc.nd] + arc.weight):
    #                 sm = S[arc.nd] + self.p[arc.nd] + arc.weight
    #         S[nd] = sm
    #     return S




###########Dopisac dodawanie ; na koncu wiersza ######################

# def PARSOWANIE_DANYCH(path:str ="dryer_50_t.csv"):
#     # wczytanie i podział danych do dogadania#########################
#     file = data_csv.preprocesData(path=path)
#     file.preper_file()
#     # for i in range(1,G.n + 1, 1):
#     for i in range(G.n):

#         G.p[i] = file.file_to_dict["Czas wykonania"][i]
#     stringSeparators = [" and "]
#     for i in range(G.n):
#     # for i in range(1,G.n + 1, 1):
#         sp = file.file_to_dict["Wymaga zakonczenia"][i].split(*stringSeparators)
#         for s in sp:
#             spx = s.split("(")
#             nd = int(spx[0])
#             if nd == 0:
#                 continue
#             weight = int(eval(spx[1].replace(")", "")))
#             a = CArc(nd=i, weight=weight)
#             G.Succ[nd] = a
#             b = CArc(nd=nd, weight=weight)
#             G.Pred[i] = b
#         sp = file.file_to_dict["Pracownicy"][i].split(" ")
#         for s in sp:
#             if s == "":
#                 continue
#             spx = s.split("x")
#             nbr = int(spx[0])
#             id = str(spx[1])
#             r = CRes(id=id, number=nbr)
#             G.Res[i] = r
#     return G



            

G = PARSOWANIE_DANYCH()

# ord = G.TOP_ORDER()

# H = G.Harm(ord=ord)

# print(H)

# Test = CGraph(np=2)
# print(Test.TOP_ORDER())