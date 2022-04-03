
public class CArc {
            public int nd;
            public int weight;
       }
       public class CRes
       {
           public int id;
           public int number;
       }
      
        
        public class CGraph
        {
            public int n;
            public List<CArc>[] Succ = null;
            public List<CArc>[] Pred = null;
            public List<CRes>[] Res = null;
            
            public int[] p = null;
            public void init(int np) {
                n = np;
                Succ = new List<CArc>[n + 1];
                for (int i = 1; i <= n; i++) Succ[i] = new List<CArc>();
                Pred = new List<CArc>[n + 1];
                for (int i = 1; i <= n; i++) Pred[i] = new List<CArc>();
                Res = new List<CRes>[n + 1];
                for (int i = 1; i <= n; i++) Res[i] = new List<CRes>();
              
 
                p = new int[n + 1]; for (int i = 0; i <= n; i++) p[i] = 0;
            }

            public int [] TOP_ORDER()
            {
               int []LP = new int[n + 1];
               for (int i = 1; i <= n; i++) LP[i] = Pred[i].Count;
               Queue<int> Q = new Queue<int>();
               for (int i = 1; i <= n; i++) if (LP[i] == 0) Q.Enqueue(i);
               List<int> ORD = new List<int>(); ORD.Add(0);
               while (Q.Count > 0)
               {
                   var nd = Q.Dequeue(); ORD.Add(nd);
                   foreach (var arc in Succ[nd]) if (--LP[arc.nd] == 0) Q.Enqueue(arc.nd);
               }
               return ORD.ToArray();

            }

            public int[] Harm(int []ord)
            {
                int[] S = new int[n + 1]; S[0] = 0;
                for (int i = 1; i <= n; i++)
                {
                    var nd = ord[i]; int sm = 0;
                    foreach (var arc in Pred[nd])
                        if (sm < S[arc.nd] + p[arc.nd] + arc.weight)
                            sm = S[arc.nd] + p[arc.nd] + arc.weight;
                    S[nd] = sm;
                }
                
                return S;
            }
        }

        CGraph G = null;
        int[] H = null;


//PARSOWANIE DANYCH


    D = MI.CSV2Dicts("c:\\Wojewodzki\\Dane\\dryer_50_t.csv");
            G = new CGraph();  G.init(D.Length);

            for(int i=1; i<=G.n; i++)
                G.p[i]=int.Parse(D[i-1]["Czas wykonania"]);

            string[] stringSeparators = new string[] { "and" };
            for (int i = 1; i <= G.n; i++)
            {
                string[] sp = D[i - 1]["Wymaga zakończenia"].Split(stringSeparators, StringSplitOptions.None);
                foreach (var s in sp)
                {
                    string[] spx = s.Split('(');
                    int nd = int.Parse(spx[0]); if (nd == 0) continue;
                    int weight = int.Parse(spx[1].Replace(')', ' '));        
                    CArc a = new CArc(); a.nd = i; a.weight = weight;
                    G.Succ[nd].Add(a);
                    CArc b = new CArc(); b.nd = nd;  b.weight = weight;
                    G.Pred[i].Add(b);
                }

                sp = D[i - 1]["Pracownicy"].Split(' ');
                foreach (var s in sp)
                {
                    if (s == "") continue;
                    string[] spx = s.Split('x');
                    int nbr = int.Parse(spx[0]); 
                    int id = Symbols[spx[1]];
                    CRes r = new CRes(); r.id = id; r.number = nbr;
                    G.Res[i].Add(r);
                   
                }
            }



//WYWOŁANIE ALGORYTMU

    var ord =  G.TOP_ORDER();

          H = G.Harm(ord);





Wynik

		[1]	0	int
		[2]	42	int
		[3]	62	int
		[4]	82	int
		[5]	95	int
		[6]	108	int
		[7]	108	int
		[8]	108	int
		[9]	123	int
		[10]	139	int
		[11]	195	int
		[12]	195	int
		[13]	195	int
		[14]	195	int
		[15]	200	int
		[16]	200	int
		[17]	200	int
		[18]	200	int
		[19]	203	int
		[20]	205	int
		[21]	209	int
		[22]	217	int
		[23]	217	int
		[24]	225	int
		[25]	232	int
		[26]	244	int
		[27]	251	int
		[28]	265	int












        






