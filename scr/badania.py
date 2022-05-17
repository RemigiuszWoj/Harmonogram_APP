import algorithm
import time
import os



def badania_ds(ord, Graph, workers_list, run, nb, debug =True):
    path = "badania" + os.sep + str(nb) + os.sep + "ds" + ".txt"
    my_data_file = open(path, "+w")
    my_data_file.write("run;best_Cmax_ds;work_time;" + "\n")
    for i in run:
        t_start = time.time()
        C_best_ds, best_Cmax_ds, best_ord_ds = algorithm.ds(ord=ord,Graph=Graph,workers_list=workers_list)
        t_end = time.time()
        work_time = t_end - t_start      
        my_data_file.write(str(i) + ";" + str(best_Cmax_ds) + ";" + str(work_time) +";" + "\n")
        if debug == True:
            print("ds: " + str(i))
    my_data_file.close()

def badania_rnd(ord, Graph, workers_list, run, nb, debug =True):
    path = "badania" + os.sep + str(nb) + os.sep + "rnd" + ".txt"
    my_data_file = open(path, "+w")
    my_data_file.write("run;best_Cmax_rnd;work_time;" + "\n")
    for i in run:
        t_start = time.time()
        C_best_rnd, best_Cmax_rnd, best_ord_rnd = algorithm.random_serge(ord=ord,Graph=Graph,workers_list=workers_list)
        t_end = time.time()
        work_time = t_end - t_start      
        my_data_file.write(str(i) + ";" + str(best_Cmax_rnd) + ";" + str(work_time) +";" + "\n")
        if debug == True:
            print("rnd: " +  str(i))
    my_data_file.close()

def badania_sw(ord, Graph, workers_list, run, nb, debug =True):
    path = "badania" + os.sep + str(nb) + os.sep + "sw" + ".txt"
    my_data_file = open(path, "+w")
    my_data_file.write("run;best_Cmax_rnd;work_time;" + "\n")
    for i in run:
        t_start = time.time()
        C_best_sw, best_Cmax_sw, best_ord_sw = algorithm.symulowane_wyzazanie(ord=ord,Graph=Graph,workers_list=workers_list)
        t_end = time.time()
        work_time = t_end - t_start      
        my_data_file.write(str(i) + ";" + str(best_Cmax_sw) + ";" + str(work_time) +";" + "\n")
        if debug == True:
            print("sw: " + str(i))
    my_data_file.close()

