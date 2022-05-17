from statistics import mean
import data_csv
import os

DIRECTORY = ["badania"]
SUB_DIRECTORY = ["1", "2", "3", "4", "5", "6", "7", "8"]
SUB_DIRECTORY = SUB_DIRECTORY[0]

ALGORYTMY = ["ds", "rnd", "sw"]
ALGORYTMY = ["ds"]
EXTENTION = [".csv"]

def create_path_set(DIRECTORY, SUB_DIRECTORY, ALGORYTMY, EXTENTION):
    PATH_SET = []
    for directory in DIRECTORY:
        for sub_directory in SUB_DIRECTORY:
            for algorytm in ALGORYTMY:
                for extension in EXTENTION:
                    PATH_SET.append(directory + os.sep + sub_directory + os.sep + algorytm + extension)
    return PATH_SET

PATH_SET = create_path_set(DIRECTORY, SUB_DIRECTORY, ALGORYTMY, EXTENTION)
print(PATH_SET)

def txt_to_csv(path:str):
    path.replace(".txt", ".csv")

def create_csv_set(patch_list:list) -> list:
    # PATH_LIST = []
    # for path in patch_list:
    #     PATH_LIST.append(txt_to_csv(path=path))
    # return PATH_LIST
    for path in patch_list:
        txt_to_csv(path=path)

# create_csv_set(patch_list=PATH_SET)

# PATH_LIST = create_csv_set(patch_list=PATH_SET)

# print(PATH_LIST)

my_csv_file = data_csv.preprocesData(PATH_SET[0])
my_csv_file.preper_file()
print(my_csv_file.file_to_dict)

C_max = my_csv_file.file_to_dict["best_Cmax_ds"]
best_C_max = min(C_max)
mean_C_max = mean(C_max)