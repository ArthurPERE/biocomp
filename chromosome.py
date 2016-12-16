import gene as g
import numpy as np
import polymerase
from math import *

class chromosome:
	# longeur du genome
	def __init__(self, longeur, nom, id_c):
		self.longeur = longeur
		self.nom = nom
		self.id = id_c

		# le tableau de genes
		self.genes = []
		self.polymerases = []

		self.sigma = np.array([-0.4 for i in xrange(longeur)])

		
	# fonction pour creer les vecteurs contenant les positions des promoteurs
	# et du taux initalisation
	def create_vector(self):
		self.promo = []
		self.taux_init = []

		for i in self.genes:
			self.promo.append(i.position_deb)
			self.taux_init.append(i.init)


	## le f(sigma) dans l'equation de taux d'init
	def fonction_sigma(self,sigma):

		g_sigma = 1/(1+np.exp(sigma-(-0.4))/0.01)
		prob_sigma = np.exp(g_sigma)

		return prob_sigma


	# Fonction pour calculer K
	def calcK(self):
		f_0 = self.sigma[self.promo]

		K = self.fonction_sigma(f_0)
		K *= self.taux_init
		K /= sum(K)

		return K


	# fonction initialisation
	# indice_t : indices negatif de t
	def initialisation(self, indice_t):

		K = self.calcK()

		t = [0 for i in xrange(len(indice_t))]
		# gene : parmie les elements des genes, on choisit le nombre de polymerases inactive
		# avec differentes probabilite
		genes = np.random.choice(self.genes, len(indice_t), replace=False, p=K)

		


	# 
	def update_initial(self, indice_t, P_inac, genes):



	def simulation(self,sigma): 
		self.sigma=sigma 
		print self.etape_init(self.sigma) 


'''
taux_basal=[100,20,1000] 
sigma = [1,1,1] 
longeur=[76,46,50] 
chrom1= chromosome(taux_basal,3,longeur) 
chrom1.simulation(sigma)
'''