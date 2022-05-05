
import parser
import graph
import algorithm

def load_orders() -> list:
    orders = parser.PARS_ORDERS()
    orders = parser.preper_orders(orders)
    return orders

def make_orders_list(orders) -> list:
    orders_list = []
    for i in range(0, len(orders)):
        orders_list.append(orders[i]["MODEL"])
    return orders_list

def generate_full_graph():
    orders = load_orders()
    orders_list = make_orders_list(orders=orders)
    
    GP = graph.CGraph(np=0)
    job = 1
    for model in orders_list:
        G = parser.PARSOWANIE_DANYCH(
            path =model, nr_job = job)
        GP.mergeGraf(G1=G)
        job += 1
    return GP

def test_graph():
    GP = graph.CGraph(np=0)
    G = parser.PARSOWANIE_DANYCH(path ="dryer_35_t.csv", nr_job = 1)
    G1 = parser.PARSOWANIE_DANYCH(path ="dryer_20_t.csv", nr_job = 2)
    GP.mergeGraf(G1=G)
    GP.mergeGraf(G1=G1)
    return GP

def get_job():
    G_list = []
    G = parser.PARSOWANIE_DANYCH(path ="dryer_35_t.csv", nr_job = 1)
    G_list.append(G)
    G1 = parser.PARSOWANIE_DANYCH(path ="dryer_20_t.csv", nr_job = 2)
    G_list.append(G1)
    return G_list


# # GP = generate_full_graph()
# GP = test_graph()

workers_data = parser.PARS_WORKERS()
wokrers_list = parser.preper_woreks(workers_data=workers_data)

# Algorytm = algorithm.Algorithm(Graph=GP, workers_data=workers_data)

# Algorytm.generate_permutation()

def create_G(G_list, sequence, nb):
    GP = graph.CGraph(np=0)
    for i in range(1,nb+1):
        GP.mergeGraf(G1=G_list[sequence[i]-1])
    return GP

sequence =[0, 1, 2]
nb = 2

G_list = get_job()

G = create_G(G_list=G_list, sequence=sequence, nb=nb) 
# print(G.TOP_ORDER())
ord = G.TOP_ORDER()


def easy_asign(workers, Graph):
    a = []
    a.append([])
    for op in range(1,Graph.n+1):
        USE_WORKERS = []
        FUNCTION_ID = []
        for r in Graph.Res[op]:
            r_id = r.id
            r_number = r.number
            ID_WORKERS = []
            for k in range(1,len(workers)):
                if r_id in workers[k - 1]:
                    if k not in USE_WORKERS:
                            ID_WORKERS.append(k)
            for l in range(1, r_number + 1):
                USE_WORKERS.append(ID_WORKERS.pop(0))
                FUNCTION_ID.append(r_id)
        a.append({"USE_WORKERS":USE_WORKERS,
                  "FUNCTION_ID":FUNCTION_ID})
    return a

def c_max(m, workers, Graph, a, pi):
    Z = [ 0 for _ in range(m + 1)]
    C = [ 0 for _ in range(Graph.n + 1)]
    for i in range(1,Graph.n +1):
        op = pi[i]
        z = 0
        for j in a[op]["USE_WORKERS"]:
            z = max([z, Z[j]])
        for arc in Graph.Pred[op]:
            z = max([z, C[arc.nd] + arc.weight])
            
        z = z + Graph.p[op]
        C[op] = z
        for j in a[op]["USE_WORKERS"]:
            Z[j] = z
    return C

def c_max2(m, workers, Graph, a, pi):
    Z = [ 0 for _ in range(m + 1)]
    C = [ 0 for _ in range(Graph.n + 1)]
    for i in range(1,Graph.n +1):
        op = pi[i]
        z = 0
        for j in a[op]["USE_WORKERS"]:
            z = max([z, Z[j]])

        for nx in range(len(a[op]["USE_WORKERS"])):
            # print(a[op]["USE_WORKERS"])
            # print(nx)
            ky = a[op]["USE_WORKERS"][nx]
            fun_w = a[op]["FUNCTION_ID"][nx]
            if z == Z[ky]:
                for k in range(1,m+1):
                    if k in a[op]["USE_WORKERS"]:
                        continue
                    if Z[k] >= z:
                        continue

                    # print("len wrkers",len(workers))
                    # print("k",k)
                    if fun_w in workers[k-1]:
                        a[op]["USE_WORKERS"][nx] = k
                        break
                    continue
        z = 0
        for j in a[op]["USE_WORKERS"]:
            z = max([z, Z[j]])
        for arc in Graph.Pred[op]:
            z = max([z, C[arc.nd] + arc.weight])
            
        z = z + Graph.p[op]
        C[op] = z
        for j in a[op]["USE_WORKERS"]:
            Z[j] = z
    return C, max(C)

#def IS_TOP(pi, Graph)
#insertowanie na wszystkie pozycje , liczenie cmax, zmiana i dalej 


a = easy_asign(Graph=G, workers=wokrers_list)

C0, max_C0 = c_max2(m=len(wokrers_list),
 workers=wokrers_list,Graph=G, a=a, pi=ord)

print(max_C0)

def move_elem(l, oldindex, newindex):
    l.insert(newindex, l.pop(oldindex))

move_elem(ord,45,43)

a1 = easy_asign(Graph=G, workers=wokrers_list)

C1, max_C1 = c_max2(m=len(wokrers_list),
 workers=wokrers_list,Graph=G, a=a1, pi=ord)

print(max_C1)

move_elem(ord,27,34)

a2 = easy_asign(Graph=G, workers=wokrers_list)
print(a)
C2, max_C2 = c_max2(m=len(wokrers_list),
 workers=wokrers_list,Graph=G, a=a2, pi=ord)
print(C2)
print(max_C2)








# print(wokrers_list)

# # from copy import deepcopy

# ord = G.TOP_ORDER()

# H = G.Harm(ord=ord)

# G1 = parser.PARSOWANIE_DANYCH(path ="dryer_20_t.csv", nr_job = 2)

# def mergeGraf(G, G1):
#     for i in range(1,len(G1.p)):
#         G.p.append(G1.p[i])
#         G.job.append(G1.job[i])
#         G.Res.append(G1.Res[i])

#     for i in range(1,len(G1.Succ)):
#         pom =[]
#         pom = deepcopy(G1.Succ[i])
#         for j in range(0,len(pom)):
#             pom[j].nd = pom[j].nd + G.n 
#         G.Succ.append(pom)
        
#     for i in range(1,len(G1.Pred)):
#         pom =[]
#         pom = deepcopy(G1.Pred[i])
#         for j in range(0,len(pom)):
#             pom[j].nd = pom[j].nd + G.n 
#         G.Pred.append(pom)
       
#     G.n += G1.n
    
#     return G



# mergeGraf(G,G1)


# orders = parser.PARS_ORDERS()

# orders = parser.preper_orders(orders)

# # print(orders)

# orders_list = []
# for i in range(0, len(orders)):
#     orders_list.append(orders[i]["MODEL"])

# # print(orders_list)


# # print(workers_data)

# wokrers_list = []
# for i in range(0, len(workers_data)):
#     tmp =[]
#     if workers_data[i]["UMIEJETNOSC_1"] != 99:
#         tmp.append(workers_data[i]["UMIEJETNOSC_1"])
#     if workers_data[i]["UMIEJETNOSC_2"] != 99:
#         tmp.append(workers_data[i]["UMIEJETNOSC_2"])
#     if workers_data[i]["UMIEJETNOSC_3"] != 99:
#         tmp.append(workers_data[i]["UMIEJETNOSC_3"])
#     wokrers_list.append(tmp)


# # e = order[1]
# # print(order)
# # e = 5
# iteracje = 1
# for e in order:
#     if e == 0:
#         continue
    
#     USE_WORKERS = []
#     ID_WORKERS = []
#     # print(USE_WORKERS, iteracje, "uw")
#     # print(ID_WORKERS, iteracje,"id")
#     for i in GP.Res[e]:

#         for k in range(1,wn + 1):
#             # print(k)
#             if i.id in wokrers_list[k - 1]:

#                 if k not in USE_WORKERS:
#                     ID_WORKERS.append(k)
#         # print(ID_WORKERS)

#         for l in range(1,i.number+1):
#             USE_WORKERS.append(ID_WORKERS.pop(0))
#         # print(USE_WORKERS)
#     iteracje += 1
#     # if iteracje == 4:
#     #     break
        

#     # print(ID_WORKERS)
#     # print(USE_WORKERS)

#     for m in USE_WORKERS:
#         permutation[m].append(e)
# print(permutation)
