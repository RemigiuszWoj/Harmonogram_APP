
import preproces_data
import parser
import badania
import algorithm
import matplotlib.pyplot as plt

RUNS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NB = [1, 2, 3, 4, 5, 6, 7, 8]
# NB = [1]
COLORS = ["red", "green", "blue", "orange", "green", "black", "pink", "grey", "yellow", "brown"]

run = RUNS[:3]

sequence =[0, 1, 2, 3, 4, 5, 6, 7, 8]

dyer_number = 0
debug = True

def przeprowadz_badania(NB, run, sequence, debug):

    for nb in NB:
        ds = False
        rnd = True
        sw =False

        if ds:
            workers_data = parser.PARS_WORKERS()
            wokrers_list = parser.preper_woreks(workers_data=workers_data)
            # G_list = preproces_data.get_job()
            G_list = preproces_data.generate_full_graph_list()
            G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 
            
            ord = G.TOP_ORDER()
            badania.badania_ds(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        if rnd:
            workers_data = parser.PARS_WORKERS()
            wokrers_list = parser.preper_woreks(workers_data=workers_data)
            # G_list = preproces_data.get_job()
            G_list = preproces_data.generate_full_graph_list()
            G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 
            
            ord = G.TOP_ORDER()
            badania.badania_rnd(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        if sw:
            workers_data = parser.PARS_WORKERS()
            wokrers_list = parser.preper_woreks(workers_data=workers_data)
            # G_list = preproces_data.get_job()
            G_list = preproces_data.generate_full_graph_list()
            G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 

            ord = G.TOP_ORDER()
            badania.badania_sw(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        if debug == True:
                print("nd: " + str(nb))



def make_harmonogram(sequence, NB, dyer_number):

    workers_data = parser.PARS_WORKERS()
    wokrers_list = parser.preper_woreks(workers_data=workers_data)

    G_list = preproces_data.generate_full_graph_list()

    G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=NB[dyer_number]) 

    ord = G.TOP_ORDER()
    # print(ord)
    # C_best_sw, best_Cmax_sw, best_ord_sw ,G = algorithm.symulowane_wyzazanie(pi=ord,Graph=G,workers_list=wokrers_list)
    C_best_sw, best_Cmax_sw, best_ord_sw = algorithm.ds(ord=ord,Graph=G,workers_list=wokrers_list)

    return  C_best_sw, best_Cmax_sw, best_ord_sw, G

def save_to_table(Kolejnosc,Rozpoczecie,Zakonczenie,Czas_trwania,Pracownicy,path="harmonogra_tabela.csv"):
    my_data_file = open(path, "+w")
    my_data_file.write("LP;Operacja;Rozpocecie;Zakonczenie,Pracownicy;" + "\n")
    for i in range(1,len(Kolejnosc)):
        Workers = str(Pracownicy[i]).replace("[","").replace("]","")
        # print(f"{i};{Kolejnosc[i]};{Rozpoczecie[i]};{Zakonczenie[i]};{Workers};")
        my_data_file.write(f"{i};{Kolejnosc[i]};{Rozpoczecie[i]};{Zakonczenie[i]};{Workers};\n")
    my_data_file.close()


def print_harmonogram(sequence, NB, dyer_number, COLORS):
    save = True

    workers_data = parser.PARS_WORKERS()
    wokrers_list = parser.preper_woreks(workers_data=workers_data)

    C_best_sw, best_Cmax_sw, best_ord_sw, Graph= make_harmonogram(sequence=sequence, NB=NB, dyer_number=dyer_number)

    m=len(wokrers_list)
    a0 = algorithm.easy_asign(Graph=Graph, workers=wokrers_list)
    C0_best, Cmax_best =  algorithm.c_max2(m=m, workers=wokrers_list, Graph=Graph, a=a0, pi=best_ord_sw)
  
    Zakonczenia = C0_best
    Czas_trwania = Graph.p
    Rozpoczecie =[ Zakonczenia[i] - Czas_trwania[i] for i in range(len(Zakonczenia))]
    Pracownicy = [a0[i]["USE_WORKERS"] for i in range(1,len(a0))]
    Pracownicy.insert(0,[])

    # print("Kolejnosc: ", best_ord_sw)
    # print("Rozpoczecie: ",Rozpoczecie)
    # print("Czas_trwania: ",Czas_trwania)
    # print("Zakonczenia ",Zakonczenia)
    # print("Prazownicy: ",Pracownicy)

    if save: 
        save_to_table(best_ord_sw,Rozpoczecie,Zakonczenia,Czas_trwania,Pracownicy)
    
    fig, ax = plt.subplots() 

    for i in range(1,len(Rozpoczecie)-1):
        for j in Pracownicy[i]:
            ax.hlines(j,Rozpoczecie[i],Zakonczenia[i], colors=COLORS[Graph.job[i]])
    ax.set_title("Harmonogram Czasu Pracy")
    ax.set_ylabel("Pracownik")
    ax.set_xlabel("Czas [h]")
    plt.show()


# przeprowadz_badania(NB=NB, run=run, sequence=sequence, debug=debug)

print_harmonogram(sequence=sequence, NB=NB, dyer_number=dyer_number, COLORS=COLORS)
