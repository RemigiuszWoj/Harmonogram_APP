import preproces_data
import parser
import badania
import algorithm

RUNS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NB = [1, 2, 3, 4, 5, 6, 7, 8]

run = RUNS[:8]

sequence =[0, 1, 2, 3, 4, 5, 6, 7, 8]
# nb = 3
# NB = [4]
debug = True

def przeprowadz_badania(NB, run, sequence, debug):

    for nb in NB:

        workers_data = parser.PARS_WORKERS()
        wokrers_list = parser.preper_woreks(workers_data=workers_data)
        # G_list = preproces_data.get_job()
        G_list = preproces_data.generate_full_graph_list()
        G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=nb) 
        
        ord = G.TOP_ORDER()
        badania.badania_ds(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        ord = G.TOP_ORDER()
        badania.badania_rnd(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        ord = G.TOP_ORDER()
        badania.badania_sw(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=nb)

        if debug == True:
                print("nd: " + str(nb))


# przeprowadz_badania(NB=NB, run=run, sequence=sequence, debug=debug)


workers_data = parser.PARS_WORKERS()
wokrers_list = parser.preper_woreks(workers_data=workers_data)

G_list = preproces_data.generate_full_graph_list()

G = preproces_data.create_G(G_list=G_list, sequence=sequence, nb=NB[1]) 




ord = G.TOP_ORDER()
print(ord)

C_best_sw, best_Cmax_sw, best_ord_sw = algorithm.symulowane_wyzazanie(ord=ord,Graph=G,workers_list=wokrers_list)
print("wyzazanie: ", best_Cmax_sw)
print("wyzazanie: ", C_best_sw)
print("wyzazanie: ", best_ord_sw)

# przykład z harmonogramen  
#  harmonogra narysowac + tabele  


# G_list = preproces_data.get_job()
# badania.badania_sw(ord=ord, Graph=G, workers_list=wokrers_list, run=run, debug=debug, nb=NB[0])


# C_best_ds, b
# est_Cmax_ds, best_ord_ds = algorithm.ds(ord=ord,Graph=G,workers_list=wokrers_list)
# print("ds: ", best_Cmax_ds)

# C_best_rnd, best_Cmax_rnd, best_ord_rnd = algorithm.random_serge(ord=ord,Graph=G,workers_list=wokrers_list)
# print("random: ", best_Cmax_rnd)