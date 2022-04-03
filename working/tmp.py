
import csv
import pandas as pd

def PARSOWANIE_DANYCH(path:str ='dryer_50_t.csv'):
    # wczytanie i podział danych do dogadania#########################
    dict_from_csv = {}

    # with open(path, mode='r') as inp:
    #     reader = csv.reader(inp)
    #     # print(reader)
    #     dict_from_csv = {print(rows) for rows in reader}

    #     # dict_from_csv = {rows[0]:rows[1] for rows in reader}



    dict_from_csv = pd.read_csv(path, header=None, index_col=0, squeeze=True).to_dict()
    print(dict_from_csv)


    # print(dict_from_csv)

PARSOWANIE_DANYCH()