from graph import Graph
import graph 
import op

OPERATIONS = [op.Operation()]
m = 0

def EasyHeur():
    G = graph.Graph(len(OPERATIONS)-1)
    for i in range(1,len(OPERATIONS)):
        op = OPERATIONS[i]
        G.W[op.nr] = op.p
        for pop in op.pop:
            G.AddArc(op.nr,int(pop))
           
    ORD = G.TopOrder()

    Z = []
    Z.append(None)
    for i in range(1,m+1):
        Z.append(0)
    for i in range(1,G.n+1):
        op = ORD[i]
        mach = OPERATIONS[op].machines[0]
        sm = mach[0]
        for k in range(len(mach)):
            if Z[sm] > Z[mach[k]]:
                sm = mach[k]
        OPERATIONS[op].amach = sm
        OPERATIONS[op].S = Z[sm]
        for pop in OPERATIONS[op].pop:
            if OPERATIONS[op].S < OPERATIONS[pop].C:    
                OPERATIONS[op].S = OPERATIONS[pop].C
        OPERATIONS[op].C = OPERATIONS[op].S + OPERATIONS[op].p
        Z[sm] = OPERATIONS[op].C
     
    