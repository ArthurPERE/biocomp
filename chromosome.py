import gene as g
import numpy as np
import polymerase
from math import *
from eqsygma import *

class chromosome:
	# longeur du genome
	def __init__(self, longeur, nom, id_c):
		self.longeur = longeur
		self.nom = nom
		self.id = id_c

		# le tableau de genes
		self.genes = []

		self.sigma = -0.4 * np.ones(longeur)

		
	# fonction pour creer les vecteurs contenant les positions des promoteurs
	# et du taux initalisation
	def create_vector(self, nb_poly):


		self.id_genes = np.array(xrange(len(self.genes))).astype(int)
		self.promo = np.array([ i.position_deb for i in self.genes ]).astype(int)
		self.taux_init = np.array([ i.init for i in self.genes ])
		self.taux_term = np.array([ i.term for i in self.genes ])
		self.longeur = np.array([ i.longeur for i in self.genes ]).astype(int)
		self.sens = np.array([ i.sens for i in self.genes ]).astype(int)

		self.pos_poly = - np.ones(nb_poly).astype(int)
		self.vitesse_poly = np.random.randint(25,50, size = nb_poly)
		self.gene_liee_poly = - np.ones(nb_poly).astype(int)





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
	# indice_t : indices negatif ou nul de t
	def initialisation(self, indice_t):

		# calcul du vecteur K qui est la probabilite de choisir un gene en particulier
		K = self.calcK()

		# id : parmie les genes, on choisit les promoteur qui seront le plus a meme de recevoir les polymerases
		id_genes = np.random.choice(self.id_genes, min(len(indice_t), len(self.promo)), replace=False, p=K)

		self.pos_poly[indice_t] = self.promo[id_genes]
		self.gene_liee_poly[indice_t] = id_genes
		
		return self.longeur[id_genes] * self.vitesse_poly[indice_t] / 1000



	def elongation(self):

		eqsigma(self.pos_poly, self.promo, self.sens, self.gene_liee_poly, self.longeur, self.sigma, self.vitesse_poly)
		self.pos_poly += np.take(self.sens,self.gene_liee_poly)*self.vitesse_poly


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
