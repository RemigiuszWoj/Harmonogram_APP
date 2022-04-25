import parser

from copy import deepcopy

import algorithm

G = parser.PARSOWANIE_DANYCH(path ="dryer_35_t.csv", nr_job = 1)

ord = G.TOP_ORDER()

H = G.Harm(ord=ord)

# print("H: ", H)

G1 = parser.PARSOWANIE_DANYCH(path ="dryer_20_t.csv", nr_job = 2)

# print(G.Succ[1][0].nd)
# print(G1.Succ[1][0].nd)

def mergeGraf(G, G1):
    for i in range(1,len(G1.p)):
        G.p.append(G1.p[i])
        G.job.append(G1.job[i])
        G.Res.append(G1.Res[i])

    for i in range(1,len(G1.Succ)):
        pom =[]
        pom = deepcopy(G1.Succ[i])
        for j in range(0,len(pom)):
            pom[j].nd = pom[j].nd + G.n 
        G.Succ.append(pom)
        

    for i in range(1,len(G1.Pred)):
        pom =[]
        pom = deepcopy(G1.Pred[i])
        for j in range(0,len(pom)):
            pom[j].nd = pom[j].nd + G.n 
        G.Pred.append(pom)
       
    G.n += G1.n
    

    # for i in range(1,len(G.Succ)):
    #     if len(G.Succ[i]) != 0:
    #         print(G.Succ[i][0].nd)
    
    # for i in range(1,len(G.Pred)):
    #     if len(G.Pred[i]) != 0:
    #         print(G.Pred[i][0].nd)

    return G



# mergeGraf(G,G1)

def emptyGraph():
    GP = algorithm.CGraph(np = 0)

    return GP

GP = emptyGraph()

# print(GP.p, GP.Res, GP.Pred, GP.job)

GP = mergeGraf(GP,G)

GP = mergeGraf(GP, G1)

order = GP.TOP_ORDER()



workers_data = parser.PARS_WORKERS()

# print(workers_data)

wokrers_list = []
for i in range(0, len(workers_data)):
    tmp =[]
    if workers_data[i]["UMIEJETNOSC_1"] != 99:
        tmp.append(workers_data[i]["UMIEJETNOSC_1"])
    if workers_data[i]["UMIEJETNOSC_2"] != 99:
        tmp.append(workers_data[i]["UMIEJETNOSC_2"])
    if workers_data[i]["UMIEJETNOSC_3"] != 99:
        tmp.append(workers_data[i]["UMIEJETNOSC_3"])
    wokrers_list.append(tmp)

# print(wokrers_list)


wn = len(workers_data)



permutation = []
for _ in range(wn + 1):
    permutation.append([])


Z = []
for _ in range(wn + 1):
    Z.append(0)

# e = order[1]
# print(order)
# e = 5
iteracje = 1
for e in order:
    if e == 0:
        continue
    
    USE_WORKERS = []
    ID_WORKERS = []
    # print(USE_WORKERS, iteracje, "uw")
    # print(ID_WORKERS, iteracje,"id")
    for i in GP.Res[e]:

        for k in range(1,wn + 1):
            # print(k)
            if i.id in wokrers_list[k - 1]:

                if k not in USE_WORKERS:
                    ID_WORKERS.append(k)
        # print(ID_WORKERS)

        for l in range(1,i.number+1):
            USE_WORKERS.append(ID_WORKERS.pop(0))
        # print(USE_WORKERS)
    iteracje += 1
    # if iteracje == 4:
    #     break
        

    # print(ID_WORKERS)
    # print(USE_WORKERS)

    for m in USE_WORKERS:
        permutation[m].append(e)
print(permutation)
























# orders = parser.PARS_ORDERS()

# orders = parser.preper_orders(orders)

# # print(orders)

# orders_list = []
# for i in range(0, len(orders)):
#     orders_list.append(orders[i]["MODEL"])

# # print(orders_list)