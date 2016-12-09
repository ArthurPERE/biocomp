''' inputs 
TabPosition : Position de la Polymerase. Taille N
TabDirection : Direction de traduction. Taille N
ActiveGen : Gens en traduction par la polymerase. Taille N
TabGen : data sur les gens . Taille 2*n (Fille --> Gen id. Colonne --> [0] Promoteur position, [1] Longeur Gen.)
CantBases : Quantite de bases
vel : velocité d'elongation

Outputs
Vecteur: sigma'''

'''Taille N --> Cant. de polymerases
Taille n --> Cant de Genes '''

def eqsygma(TabPosition, TabDirection, TabGen, CantBases, vel):

    sygmavec = [0]*CantBases
    t = [0] * N
    # J0 = [0]*N
    Jp = [0] * N
    derJp = [0] * N

    N = len(TabPosition)
    l = 10
    D = 10**5
    # J = 2.55*D


    for i in range(N):

        a = ActiveGen[i]
        LongGen = TabGen[a][1]
        Promot = TabGen[a][0]
        s = TabDirection[i]
        Pos = TabPosition[i]

       # J0[i] = J/(1+LongGen/(2*l))
        t[i] = (TabPosition[i] - Promot)/vel
       # Jp[i]=s*(J0[i]+J0[i]*vel*t[i]/l)

       # J0 = 2*l*vel
        J0 = vel/((1/LongGen)+1/(2*l))
        Jp[i] = s*(J0+J0*vel*t[i]/l)

        '''Plusiers questions: (voir paper Brackley)
        Valeur J0? Dependant du Lambda (LongGen?), variable ou pas?
        Delta x = l0, represents quoi? '''

    for h in range(1,N-1):
        derJp[h] = (Jp[h+1]-Jp[h-1])/(2*l)

    # Cette equation calcule la derivee dans un point. Cas h=0 o h=N-1 ? (ou il y a pas de h-1 ou h+1)

    # Partial Differential Equation
    # initial values --> sigma(0,x) = 0 , sigma(t,0) = sigma (t, CantBases) ?

    # return sygmavec

