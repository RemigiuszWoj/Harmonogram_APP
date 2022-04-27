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


# GP = generate_full_graph()
GP = test_graph()

workers_data = parser.PARS_WORKERS()

Algorytm = algorithm.Algorithm(Graph=GP, workers_data=workers_data)

Algorytm.generate_permutation()





# from copy import deepcopy

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
