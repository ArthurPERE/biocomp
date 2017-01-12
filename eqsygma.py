import numpy as np

from donnee import *
 
''' inputs
sigma : sigma(x) a t
TabPol : data sur les polymerases. Taille N*3 (File --> Pol id. Colonne --> [0] Position pol. [1] Direction de trad, [2] ActiveGen
TabGen : data sur les gens . Taille n*2 (Fille --> Gen id. Colonne --> [0] Promoteur position, [1] Longueur Gen. [2] Sens de transc)
CantBases : Quantite de bases (total dans l'ADN)
vel : velocite d'elongation
 
Outputs
Vecteur: sigma'''


 
def eqsigma(PosPol, PosProm, DirGen, ActiveGen, CantBases, sigma, vel):

	AxeX = CantBases
	dt = 1 / vel
	sigmavec = np.zeros(AxeX)




 	ti = (PosPol - np.take(PosProm, ActiveGen))
	DirPol = np.take(DirGen, ActiveGen)
	a = J0 * ( ti * (1/l) + 1)
	Jp = np.multiply(DirPol, a)

	np.put(sigmavec, PosPol, Jp, mode="raise")

	DerJp = (np.roll(sigmavec, -1) - np.roll(sigmavec, 1)) / (2 * l)
	sigmadx = (np.roll(sigma, -1) - np.roll(sigma, 1)) / (2 * l)
	sigmadx2 = (np.roll(sigmadx, -1) - np.roll(sigmadx, 1)) / (2 * l)
	

	sigmadt = D * sigmadx2 - DerJp

	sigma += sigmadt * dt
	
	
	return sigma





# Test
'''
vel = 30.

PosPol = [1200, 3050, 5100, 7005]
PosProm = [0,1000,2000,3000,4000,5000,6000,7000]
Dirgen = [-1,1,1,-1, -1, 1, -1, 1]
ActiveGen = [1,3,5,7]
CantBases = 10000
sigma = -0.4 * np.ones(CantBases)


sigma = eqsigma(PosPol, PosProm, Dirgen, ActiveGen, CantBases, sigma, vel)
'''

