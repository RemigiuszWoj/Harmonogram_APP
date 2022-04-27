import parser

class Algorithm():
    """
    Base algorithm class
    """

    def __init__(self, Graph, workers_data:dict) -> None:
        self.Graph = Graph
        self.workers_data = workers_data
        self.wokrers_list = parser.preper_woreks(workers_data=workers_data)
        self.wn = len(workers_data)
        self.order = self.Graph.TOP_ORDER()
        self.preproces()
    
    def preproces(self):
        self.permutation = []
        for _ in range(self.wn + 1):
            self.permutation.append([])

        self.Z = []
        for _ in range(self.wn + 1):
            self.Z.append(0)

    def generate_permutation(self):

        # e = order[1]
        # print(order)
        # e = 5
        iteracje = 1
        for e in self.order:
            if e == 0:
                continue
            
            USE_WORKERS = []
            ID_WORKERS = []
            # print(USE_WORKERS, iteracje, "uw")
            # print(ID_WORKERS, iteracje,"id")
            for i in self.Graph.Res[e]:

                for k in range(1,self.wn + 1):
                    # print(k)
                    if i.id in self.wokrers_list[k - 1]:

                        if k not in USE_WORKERS:
                            ID_WORKERS.append(k)
                # print(ID_WORKERS)

                for l in range(1,i.number+1):
                    USE_WORKERS.append(ID_WORKERS.pop(0))
                # print(USE_WORKERS)
            iteracje += 1
            # if iteracje == 4:
            #     break
                

            # print(ID_WORKERS)
            # print(USE_WORKERS)

            for m in USE_WORKERS:
                self.permutation[m].append(e)
        print(self.permutation)

