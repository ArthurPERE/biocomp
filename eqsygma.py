import numpy as np
 
''' inputs
sigma : sigma(x) a t
TabPol : data sur les polymerases. Taille N*3 (File --> Pol id. Colonne --> [0] Position pol. [1] Direction de trad, [2] ActiveGen
TabGen : data sur les gens . Taille n*2 (Fille --> Gen id. Colonne --> [0] Promoteur position, [1] Longeur Gen.)
CantBases : Quantite de bases (total dans l'ADN)
vel : velocite d'elongation
 
Outputs
Vecteur: sigma'''
 
'''Taille N --> Cant. de polymerases
Taille n --> Cant de Genes '''
 
# sigma = sigma0
t = 0
l = 10
vel = 25
 
# J0 c'est un parametre, je prendre ce valeur la pour J=v*lamda et J=J0[1+lamda]/(2*l) simplifie
J0 = 2 * l * vel
 
# D est un parametre, je prendre ce valeur la pour la bibliographie (aussi 2,55*10**3) unites : bp**2/s
D = 10 ** 5
 
# AxeX = CantBases / l
 
def eqsigma(TabGen, TabPol, AxeX, sigma, vel):
 
	dt = 1 / vel
	sigmavec = np.zeros(AxeX)
    
	PosProm = TabGen[:][0]
    # LongGen = TabGen[:][1]
	PosPol = TabPol[:][0]
	DirPol = TabPol[:][1]
	ActiveGen = TabPol[:][2]
 
	ti = (PosPol - np.take(PosProm, ActiveGen))
	
	a = J0 * ( ti * (1/l) + 1) # Equation d'origine a = ti * vel * J0 * (1/l) + J0, avec ti = (PosPol - np.take(PosProm, ActiveGen)) / vel
	
	Jp = np.multiply(DirPol, a)
	print Jp
	np.put(sigmavec, PosPol, Jp, mode="raise")
	
	
	DerJp = (np.roll(sigmavec, -1) - np.roll(sigmavec, 1)) / (2 * l)
	sigmadx = (np.roll(sigma, -1) - np.roll(sigma, 1)) / (2 * l)
	sigmadx2 = (np.roll(sigmadx, -1) - np.roll(sigmadx, 1)) / (2 * l)
	
	
	sigmadt = D * sigmadx2 - DerJp
	sigma = sigma + sigmadt * dt
	
	
	return sigma
 
# Test
 
TabGen = [[0,1000,2000,3000,4000,5000,6000,7000],[500,600,700,200,300,400,800,1000]]
TabPol = [[1200, 3050, 5100, 7005],[-1,1,1,-1],[1,3,5,7]]
AxeX = 10000
sigma = np.random.randint(10, size=AxeX)
vel = np.random.randint(20, 25, size = AxeX)
print(eqsigma(TabGen,TabPol,AxeX,sigma, vel))

#Apparement ca marche bien :D 
