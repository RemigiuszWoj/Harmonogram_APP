import tkinter
import csv
import preproces_data
import main

ADD_DRYER = "dryer_20_t"
SYMBOL_LIST= ["C","E","K","U","S","W","-"]
NB = [1, 2, 3, 4, 5, 6, 7, 8]
sequence =[0, 1, 2, 3, 4, 5, 6, 7, 8]
dyer_number = 1


def add_20_t():
    ADD_DRYER = "dryer_20_t"
    print(ADD_DRYER)

def add_35_t():
    ADD_DRYER = "dryer_35_t"
    print(ADD_DRYER)

def add_50_t():
    ADD_DRYER = "dryer_50_t"
    print(ADD_DRYER)

def wyswietl_zamowienia():
    output.delete(0.0,tkinter.END)
    with open("orders.csv", "r") as f:
        data = f.read()
        output.insert("1.0", data)
    print("Wyświetlono")

def dodaj_element_zamowienia():
    orders = preproces_data.load_orders()
    last_LP = orders[-1]["LP"]
    if  nazwa_firmy.get() != "":
        company_name = nazwa_firmy.get()
    else:
        company_name = "Blad"

    order = f"{last_LP + 1};{company_name};{ADD_DRYER};"
    print (order)
    with open("orders.csv", 'a') as f:
        f.write("\n")
        f.write(order)
    wyswietl_zamowienia()
    print("Dodano")

def usun_element_hrmonogram():
    fd=open("orders.csv","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("orders.csv","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
    wyswietl_zamowienia()
    print("usunieto")

def wyswietl_pracownicy():
    output.delete(0.0,tkinter.END)
    with open("workers.csv", "r") as f:
        data = f.read()
        output.insert("1.0", data)
    print("Wyswietlono")

def dodaj_pracownicy():
    workers = preproces_data.load_orders()
    last_LP = workers[-1]["LP"]

    if  pole_imie.get() != "":
        workers_name = pole_imie.get()
    else:
        workers_name = "Blad"

    if  pole_nazwisko.get() != "":
        workers_last_name = pole_nazwisko.get()
    else:
        workers_last_name = "Blad"

    if  pole_U1.get() in SYMBOL_LIST:
        utility_U1 = pole_U1.get()
    else:
        utility_U1 = "-"

    if  pole_U2.get() in SYMBOL_LIST:
        utility_U2 = pole_U2.get()
    else:
        utility_U2 = "-"

    if  pole_U3.get() in SYMBOL_LIST:
        utility_U3 = pole_U3.get()
    else:
        utility_U3 = "-"

    worker = f"{last_LP + 1};{workers_name};{workers_last_name};{utility_U1};{utility_U2};{utility_U3};"
    print (worker)
    with open("workers.csv", 'a') as f:
        f.write("\n")
        f.write(worker)
    wyswietl_pracownicy()
    print("dodano")

def usun_pracownicy():
    fd=open("workers.csv","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("workers.csv","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
    wyswietl_pracownicy()
    print("usunieto")

def harmonogramuj_harmonogram():
    C_best_sw, best_Cmax_sw, best_ord_sw = main.make_harmonogram(sequence=sequence, NB=NB,dyer_number=dyer_number)
    print("wyzazanie: ", best_Cmax_sw)
    print("wyzazanie: ", C_best_sw)
    print("wyzazanie: ", best_ord_sw)

    data = f"best_Cmax_sw: {best_Cmax_sw}\n C_best_sw: {C_best_sw}\n best_ord_sw: {best_ord_sw}"

    output.delete(0.0,tkinter.END)
    output.insert("1.0", data)
    print("Harmonagramuje")

def wyswietl_harmonogram():
    print("Wyswietlam")

#Okinko
window =tkinter.Tk()
window.title("Metoda pełazajacej magisterki")

#Zamówienia
ramka_zamowienia = tkinter.LabelFrame(window, text="Zamówienia")
ramka_zamowienia.grid(row=0, column=1, columnspan=8, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

tkinter.Label (ramka_zamowienia, text="Podaj nazwę firmy").grid(row=1,column=0,sticky='W')

nazwa_firmy = tkinter.Entry(ramka_zamowienia, width = 30)
nazwa_firmy.grid(row=1, column=3, columnspan=8, sticky="WE", pady=5, padx = 5)

tkinter.Button(ramka_zamowienia,text="dryer_20_t",
             command=add_20_t, width = 9, height = 1
             ).grid(row=3,column=0, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="dryer_35_t",
             command=add_35_t, width = 9, height = 1
             ).grid(row=3,column=4, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="dryer_50_t",
             command=add_50_t, width = 9, height = 1
             ).grid(row=3,column=6, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="Wyświetl",
             command=wyswietl_zamowienia, width = 9, height = 1
             ).grid(row=5,column=0, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="Dodaj",
             command=dodaj_element_zamowienia, width = 9, height = 1
             ).grid(row=5,column=4, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="Usun",
             command=usun_element_hrmonogram, width = 9, height = 1
             ).grid(row=5,column=6, rowspan=1, sticky='E',pady=2, padx = 5)


#Pracownicy
ramka_zamowienia = tkinter.LabelFrame(window, text="Pracownicy")
ramka_zamowienia.grid(row=2, column=1, columnspan=8, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

tkinter.Button(ramka_zamowienia,text="Wyświetl",
             command=wyswietl_pracownicy, width = 9, height = 1
             ).grid(row=3,column=0, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="Dodaj",
             command=dodaj_pracownicy, width = 9, height = 1
             ).grid(row=3,column=4, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_zamowienia,text="Usun",
             command=usun_pracownicy, width = 9, height = 1
             ).grid(row=3,column=6, rowspan=1, sticky='E',pady=2, padx = 5)

#ramka imie
ramka_imie = tkinter.LabelFrame(ramka_zamowienia, text="Imie")
ramka_imie.grid(row=6, column=0, columnspan=5, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

pole_imie = tkinter.Entry(ramka_imie, width=10)
pole_imie.grid(row=1, column=1, columnspan=1, sticky="WE", pady=10, padx = 5)

#ramka nazwisko
ramka_nazwisko = tkinter.LabelFrame(ramka_zamowienia, text="Nazwisko")
ramka_nazwisko.grid(row=6, column=5, columnspan=5, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

pole_nazwisko = tkinter.Entry(ramka_nazwisko, width=10)
pole_nazwisko.grid(row=1, column=1, columnspan=1, sticky="WE", pady=10, padx = 5)


#Umiejetnosc 1
ramka_U1 = tkinter.LabelFrame(ramka_zamowienia, text="Umiejetnosc 1")
ramka_U1.grid(row=9, column=0, columnspan=5, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

pole_U1 = tkinter.Entry(ramka_U1, width=10)
pole_U1.grid(row=1, column=1, columnspan=1, sticky="WE", pady=10, padx = 5)

#Umiejetnosc 2
ramka_U2 = tkinter.LabelFrame(ramka_zamowienia, text="Umiejetnosc 2")
ramka_U2.grid(row=9, column=5, columnspan=5, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

pole_U2 = tkinter.Entry(ramka_U2, width=10)
pole_U2.grid(row=1, column=1, columnspan=1, sticky="WE", pady=10, padx = 5)

#Umiejetnosc 3
ramka_U3 = tkinter.LabelFrame(ramka_zamowienia, text="Umiejetnosc 3")
ramka_U3.grid(row=9, column=11, columnspan=5, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

pole_U3 = tkinter.Entry(ramka_U3, width=10)
pole_U3.grid(row=1, column=1, columnspan=1, sticky="WE", pady=10, padx = 5)

#Harmonogram
ramka_harmonogram = tkinter.LabelFrame(window, text="Harmonogram")
ramka_harmonogram.grid(row=3, column=1, columnspan=8, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

tkinter.Button(ramka_harmonogram,text="Harmonogramuj",
             command=harmonogramuj_harmonogram, width = 15, height = 1
             ).grid(row=3,column=0, rowspan=1, sticky='E',pady=2, padx = 5)

tkinter.Button(ramka_harmonogram,text="Wyswietl",
             command=wyswietl_harmonogram, width = 15, height = 1
             ).grid(row=3,column=4, rowspan=1, sticky='E',pady=2, padx = 5)


#ramka_komunikacji
ramka_komunikacji = tkinter.LabelFrame(window, text="Stan")
ramka_komunikacji.grid(row=4, column=0, columnspan=8, rowspan=2, sticky='NS', padx=5, pady=5, ipadx=5, ipady=5)

output = tkinter.Text(ramka_komunikacji,width = 56, height = 10,wrap = tkinter.WORD)
output.grid(row = 1, column = 1, columnspan = 7, pady=10, padx = 5)

window.mainloop()
