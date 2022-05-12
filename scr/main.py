
import parser
import graph
import algorithm
import copy
import random
# import numpy as np
import math

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
    G2 = parser.PARSOWANIE_DANYCH(path ="dryer_20_t.csv", nr_job = 3)
    G_list.append(G2)
    return G_list

def create_G(G_list, sequence, nb):
    GP = graph.CGraph(np=0)
    for i in range(1,nb+1):
        GP.mergeGraf(G1=G_list[sequence[i]-1])
    return GP

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

def move_elem(l, oldindex, newindex):
    l.insert(newindex, l.pop(oldindex))

def IS_TOP(pi, Graph):
    ps = [0 for _ in range(Graph.n + 1)]
    for i in range(1, G.n):
        ps[pi[i]] = i
    for nd in range(1, Graph.n + 1):
        for a in G.Succ[nd]:
            if ps[nd] > ps[a.nd]:
                return False
        return True

def insert_nbr(Graph, workers_list, ord):
    best_C, best_max_C = 0, 0
    a0 = easy_asign(Graph=Graph, workers=workers_list)

    C0, max_C0 = c_max2(m=len(workers_list),
    workers=workers_list,Graph=Graph, a=a0, pi=ord)

    best_C = C0
    best_max_C = max_C0
    best_ord = copy.deepcopy(ord)

    for i in range(1,len(ord)):
        for j in range(i+1,len(ord)):
            move_elem(l=ord,oldindex=i,newindex=j)
            if IS_TOP(pi=ord,Graph=Graph) == False:
                move_elem(l=ord,oldindex=j,newindex=i)
                break
            else:
                a1 = 0
                C1, max_C1 = 0, 0

                a1 = easy_asign(Graph=G, workers=workers_list)

                C1, max_C1 = c_max2(m=len(workers_list),
                workers=workers_list,Graph=Graph, a=a1, pi=ord)

                if best_max_C > max_C1:
                    best_max_C = max_C1
                    best_C = C1
                    best_ord = copy.deepcopy(ord)

                move_elem(l=ord,oldindex=j,newindex=i)
        for j in range(i-1,1,-1):
            move_elem(l=ord,oldindex=i,newindex=j)
            if IS_TOP(pi=ord,Graph=Graph) == False:
                move_elem(l=ord,oldindex=j,newindex=i)
                break
            else:
                a1 = 0
                C1, max_C1 = 0, 0

                a1 = easy_asign(Graph=G, workers=workers_list)

                C1, max_C1 = c_max2(m=len(workers_list),
                workers=workers_list,Graph=Graph, a=a1, pi=ord)

                if best_max_C > max_C1:
                    best_max_C = max_C1
                    best_C = C1
                    best_ord = copy.deepcopy(ord)

                move_elem(l=ord,oldindex=j,newindex=i)
    return best_C, best_max_C, best_ord




def insert_rand(Graph, workers_list, ord):
    best_C, best_max_C = 0, 0
    a0 = easy_asign(Graph=Graph, workers=workers_list)

    C0, max_C0 = c_max2(m=len(workers_list),
    workers=workers_list,Graph=Graph, a=a0, pi=ord)

    best_C = C0
    best_max_C = 1000_000
    best_ord = copy.deepcopy(ord)
    i = random.randint(1,len(ord)-1)
    # print(i)
    # print(len(ord))
    for j in range(i+1,len(ord)):
        move_elem(l=ord,oldindex=i,newindex=j)
        if IS_TOP(pi=ord,Graph=Graph) == False:
            move_elem(l=ord,oldindex=j,newindex=i)
            break
        else:
            a1 = 0
            C1, max_C1 = 0, 0

            a1 = easy_asign(Graph=G, workers=workers_list)

            C1, max_C1 = c_max2(m=len(workers_list),
            workers=workers_list,Graph=Graph, a=a1, pi=ord)

            if best_max_C > max_C1:
                best_max_C = max_C1
                best_C = C1
                best_ord = copy.deepcopy(ord)

            move_elem(l=ord,oldindex=j,newindex=i)
    for j in range(i-1,1,-1):
        move_elem(l=ord,oldindex=i,newindex=j)
        if IS_TOP(pi=ord,Graph=Graph) == False:
            move_elem(l=ord,oldindex=j,newindex=i)
            break
        else:
            a1 = 0
            C1, max_C1 = 0, 0

            a1 = easy_asign(Graph=G, workers=workers_list)

            C1, max_C1 = c_max2(m=len(workers_list),
            workers=workers_list,Graph=Graph, a=a1, pi=ord)

            if best_max_C > max_C1:
                best_max_C = max_C1
                best_C = C1
                best_ord = copy.deepcopy(ord)

            move_elem(l=ord,oldindex=j,newindex=i)
    return best_C, best_max_C, best_ord

workers_data = parser.PARS_WORKERS()
wokrers_list = parser.preper_woreks(workers_data=workers_data)

sequence =[0, 1, 2, 3]
nb = 2

G_list = get_job()

G = create_G(G_list=G_list, sequence=sequence, nb=nb) 
ord = G.TOP_ORDER()
# print(ord)


def ds(ord, Graph, workers_list):
    best_ord = copy.deepcopy(ord)
    NX = 1000_000
    while True:
        best_C, best_max_C, best_ord = insert_nbr(Graph=Graph, workers_list=workers_list, ord=best_ord)
        if best_max_C < NX:
            NX = best_max_C
        else:
            break
        print("best_max_C: ", best_max_C)

    return best_C, best_max_C, best_ord

# best_C, best_max_C, best_ord=ds(ord=ord, Graph=G, workers_list=wokrers_list)
def random_serge(ord, Graph, workers_list):
    best_ord = copy.deepcopy(ord)
    NX = 1000_000
    for i in range(1000):
        best_C, best_max_C, best_ord = insert_rand(Graph=Graph, workers_list=workers_list, ord=best_ord)
        if best_max_C < NX:
            NX = best_max_C
            print("best_max_C: ", best_max_C)
    return best_C, best_max_C, best_ord


def symulowane_wyzazanie(ord,Graph,workers_list):
    t0 = 10000
    tk = 0.1
    lam = 0.95
    t = t0
    n=Graph.n
    m = len(workers_list)
    a0 = easy_asign(Graph=Graph, workers=workers_list)

    C0_best, Cmax_best = c_max2(m=m, workers=workers_list, Graph=Graph, a=a0, pi=ord)

    ord_best = []
    ord_best = copy.deepcopy(ord)
    while t > tk:
        l1 = random.randint(1,n)
        l2 = random.randint(1,n)
        C_tmp0, max_tmp0 = c_max2(m=m, workers=workers_list, Graph=Graph, a=a0, pi=ord)
        move_elem(l=ord, oldindex=l1, newindex=l2)
        if IS_TOP(pi=ord,Graph=Graph) == False:
            move_elem(l=ord,oldindex=l2,newindex=l1)
            continue
        else:
            C_tmp, max_tmp= c_max2(m=m, workers=workers_list, Graph=Graph, a=a0, pi=ord)
            if max_tmp < Cmax_best:
                Cmax_best = max_tmp
                print("pom: ",Cmax_best)
                ord_best = copy.deepcopy(ord)
            if max_tmp > max_tmp0:
                delta = max_tmp-max_tmp0
                P = math.exp(-delta/t)
                Z = random.random()
                if Z <= P:
                    i = 0
                else:
                    move_elem(l=ord, oldindex=l2, newindex=l1)
                
        t = lam*t

    pi = copy.deepcopy(ord_best)
    print("end")
    return pi, Cmax_best

best_ord, best_Cmax = symulowane_wyzazanie(ord=ord,Graph=G,workers_list=wokrers_list)
print(best_Cmax)
