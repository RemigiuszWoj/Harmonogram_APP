from multiprocessing.dummy import Array
import op as opp
import csv
import easyHeur
from array import array


def GenJob(referencja, szt, lop, jobnr, MACH, DJOB):
    L = []
    OPNR = []
    L.append(referencja)
    while len(L) > 0:
        r = L[0]
        L.pop(0)
        lop += 1
        OPNR.append({"key": r, "value": lop})
        for el in DJOB['row']:
            if el.get("Referencja") == r:
                opdx = el.get("Poprzednik").split(',')
                for ex in opdx:
                    if ex.strip() != "":
                        L.append(ex.strip())
    JOB = []
    L = []
    L.append(referencja)
    while len(L) > 0:
        r = L[0]
        L.pop(0)
        for el in DJOB['row']:
            if el["Referencja"] == r:
                opd = el
        op = opp.Operation()
        op.refer = r
        for el in OPNR:
            if el['key'] == r:
                op.nr = el['value']
        op.p = szt * int(opd["Czas"])
        op.jobnr = jobnr
        sekcje = opd["Maszyny"].split(',')
        mach = []
        for sk in sekcje:
            ky = opd["Sekcja"] + "~" + sk.strip()
            for m in MACH:
                if m['key'] == ky:
                    mach.append(m['maszyny'])

        op.machines = mach
        for el in DJOB['row']:
            if el.get("Referencja") == r:
                opdx = el.get("Poprzednik").split(',')
                for ex in opdx:
                    if ex.strip() != "":
                        L.append(ex.strip())
                        for el in OPNR:
                            if el['key'] == ex.strip():
                                op.pop.append(el['value'])
        JOB.append(op)
    return JOB


def ParseData():
    MACH = []
    pomMach = []
    with open('C:\\Users\\alage\\OneDrive\\Pulpit\\pempera_projekt\\data\\Maszyny.csv', mode='r') as machcsv:
        machDict = csv.DictReader(machcsv, delimiter=';')
        ofs = 0
        for row in machDict:
            key = row['Obszar'] + "~" + row['Typ maszyn']
            lmaszyn = int(row['Liczba maszyn'])
            nmaszyn = []
            for i in range(lmaszyn):
                ofs += 1
                nmaszyn.append(ofs)
            MACH.append({'key': key, 'maszyny': nmaszyn})
    easyHeur.m = ofs


    DJOB = {'key': [], 'row': []}
    with open('C:\\Users\\alage\\OneDrive\\Pulpit\\pempera_projekt\\data\\Technologia.csv', mode='r') as techcsv:
        techDict = csv.DictReader(techcsv,delimiter=';')
        for row in techDict:
            key = row['Referencja']
            DJOB['key'].append(key)
            DJOB['row'].append(row)
    
    OPERATIONS = []
    OPERATIONS.append(None)
    ofs = 0 
    lp = 0

    with open('C:\\Users\\alage\\OneDrive\\Pulpit\\pempera_projekt\\data\\Zamowienia.csv', mode='r') as ordcsv:
        ordDict = csv.DictReader(ordcsv, delimiter=';')
        for row in ordDict:
            lp+=1
            JOB = GenJob(row['Referencja'], int(row['Liczba szt']), ofs, lp, MACH, DJOB)
            
            for op in JOB:
                OPERATIONS.append(op)
            ofs += len(JOB)
  
    easyHeur.OPERATIONS = OPERATIONS
    easyHeur.EasyHeur()
    L = []
    L.append("")
    for i in range(1,len(easyHeur.OPERATIONS)):
        L.append(str(easyHeur.OPERATIONS[i].S)+" "+str(easyHeur.OPERATIONS[i].C))
    print(L)