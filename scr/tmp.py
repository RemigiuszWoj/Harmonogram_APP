def symulowane_wyzazanie(n,pi,JOBS,LBreakdowns):
    t0 = 10000
    tk = 0.1
    lam = 0.95
    t = t0
    cmax_best = Cmax(n,pi,JOBS,LBreakdowns)
    pi_best = []
    pi_best = pi.copy()
    while t > tk:
        l1 = np.random.randint(1,n+1)
        l2 = np.random.randint(1,n+1)
        tmp0 = Cmax(n,pi,JOBS,LBreakdowns)
        pi.insert(l1,pi.pop(l2))
        tmp = Cmax(n,pi,JOBS,LBreakdowns)
        if tmp < cmax_best:
            cmax_best = tmp
            print("pom: ",cmax_best)
            pi_best = pi.copy()
        if tmp > tmp0:
            delta = tmp-tmp0
            P = np.exp(-delta/t)
            Z = np.random.random()
            if Z <= P:
                i = 0
            else:
                pi.insert(l2,pi.pop(l1))
                
        t = lam*t

    pi = pi_best.copy()
    print("end")
    return pi