
import preproces_data
import parser
import badania
import algorithm
import matplotlib.pyplot as plt

RUNS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# NB = [1, 2, 3, 4, 5, 6, 7, 8]
NB = [1,2]
COLORS = ["red", "green", "blue", "orange", "green", "black", "pink", "grey", "yellow", "brown"]

run = RUNS[:3]

sequence =[0, 1, 2, 3, 4, 5, 6, 7, 8]

dyer_number = 1
debug = True

def przeprowadz_badania(NB, run, sequence, debug):

    for nb in NB:

        # workers_data = parser.PARS_WORKERS()
        # wokrers_list = parser.preper_woreks(workers_data=workers_data)
        # # G_list = preproces_data.get_job()
        # G_list = preproces_data.generate_full_graph_list()
        # G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 
        
        # ord = G.TOP_ORDER()
        # badania.badania_ds(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        workers_data = parser.PARS_WORKERS()
        wokrers_list = parser.preper_woreks(workers_data=workers_data)
        # G_list = preproces_data.get_job()
        G_list = preproces_data.generate_full_graph_list()
        G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 

        ord = G.TOP_ORDER()
        # print(ord)
        # print(algorithm.IS_TOP(ord,G))

        # i =14
        # j = 15
        # algorithm.move_elem(l=ord,oldindex=i,newindex=j)
        # print(ord)
        # print(algorithm.IS_TOP(ord,G))
        # algorithm.move_elem(l=ord,oldindex=28,newindex=1)
        # print(ord)
        # print(algorithm.IS_TOP(ord,G))
        

        badania.badania_rnd(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        # workers_data = parser.PARS_WORKERS()
        # wokrers_list = parser.preper_woreks(workers_data=workers_data)
        # # G_list = preproces_data.get_job()
        # G_list = preproces_data.generate_full_graph_list()
        # G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 

        # ord = G.TOP_ORDER()
        # badania.badania_sw(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        if debug == True:
                print("nd: " + str(nb))



def make_harmonogram(sequence, NB, dyer_number):

    workers_data = parser.PARS_WORKERS()
    wokrers_list = parser.preper_woreks(workers_data=workers_data)

    G_list = preproces_data.generate_full_graph_list()

    G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=NB[dyer_number]) 

    print(G.job)

    ord = G.TOP_ORDER()
    # print(ord)
    # C_best_sw, best_Cmax_sw, best_ord_sw ,G = algorithm.symulowane_wyzazanie(pi=ord,Graph=G,workers_list=wokrers_list)
    C_best_sw, best_Cmax_sw, best_ord_sw = algorithm.ds(ord=ord,Graph=G,workers_list=wokrers_list)

    return  C_best_sw, best_Cmax_sw, best_ord_sw, G

def print_harmonogram(sequence, NB, dyer_number, COLORS):

    workers_data = parser.PARS_WORKERS()
    wokrers_list = parser.preper_woreks(workers_data=workers_data)

    C_best_sw, best_Cmax_sw, best_ord_sw, Graph= make_harmonogram(sequence=sequence, NB=NB, dyer_number=dyer_number)


    m=len(wokrers_list)
    a0 = algorithm.easy_asign(Graph=Graph, workers=wokrers_list)
    C0_best, Cmax_best =  algorithm.c_max2(m=m, workers=wokrers_list, Graph=Graph, a=a0, pi=best_ord_sw)
  
    Zakonczenia = C0_best
    Czas_trwania = Graph.p
    Rozpoczecie =[ Zakonczenia[i] - Czas_trwania[i] for i in range(len(Zakonczenia))]

    print("Kolejnosc: ", best_ord_sw)
    print("Rozpoczecie: ",Rozpoczecie)
    print("Czas_trwania: ",Czas_trwania)
    print("Zakonczenia ",Zakonczenia)
    
    Pracownicy = [a0[i]["USE_WORKERS"] for i in range(1,len(a0))]
    Pracownicy.insert(0,[])
    print("Prazownicy: ",Pracownicy)
    
    fig, ax = plt.subplots() 

    for i in range(1,len(Rozpoczecie)-1):
        for j in Pracownicy[i]:
            ax.hlines(j,Rozpoczecie[i],Zakonczenia[i], colors=COLORS[Graph.job[i]])
    ax.set_title("Harmonogram Czasu Pracy")
    ax.set_ylabel("Pracownik")
    ax.set_xlabel("Czas [h]")
    plt.show()


# C_best_sw, best_Cmax_sw, best_ord_sw, Graph= make_harmonogram(sequence=sequence, NB=NB, dyer_number=dyer_number)


przeprowadz_badania(NB=NB, run=run, sequence=sequence, debug=debug)




# print("wyzazanie: ", best_Cmax_sw)
# print("wyzazanie: ", C_best_sw)
# print("wyzazanie: ", best_ord_sw)

# print_harmonogram(G=Graph, C=C_best_sw)


# G_list = preproces_data.get_job()
# badania.badania_sw(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=NB[0])


# C_best_ds, b
# est_Cmax_ds, best_ord_ds = algorithm.ds(ord=ord,Graph=G,workers_list=wokrers_list)
# print("ds: ", best_Cmax_ds)

# C_best_rnd, best_Cmax_rnd, best_ord_rnd = algorithm.random_serge(ord=ord,Graph=G,workers_list=wokrers_list)
# print("random: ", best_Cmax_rnd)

