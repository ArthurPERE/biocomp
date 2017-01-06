import gene as g
import numpy as np
from math import *
from eqsygma import *

from donnee import *

class chromosome:
	# longeur du genome
	def __init__(self, longueur, nom, id_c):
		self.longueur = longueur
		self.nom = nom
		self.id = id_c

		# le tableau de genes
		self.genes = []

		self.sigma = -0.4 * np.ones(longueur)

		
	# fonction pour creer les vecteurs contenant les positions des promoteurs
	# et du taux initalisation
	def create_vector(self, nb_poly):


		self.id_genes = np.array(xrange(len(self.genes))).astype(int)
		self.promo = np.array([ i.position_deb for i in self.genes ]).astype(int)
		self.taux_init = np.array([ i.init for i in self.genes ])
		self.taux_term = np.array([ i.term for i in self.genes ])
		self.longueur_gene = np.array([ i.longueur for i in self.genes ]).astype(int)
		self.sens = np.array([ i.sens for i in self.genes ]).astype(int)

		self.pos_poly = - np.ones(nb_poly).astype(int)
		self.gene_liee_poly = - np.ones(nb_poly).astype(int)

		del self.genes



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

		
		return (self.longueur_gene[id_genes] / vel).astype(int)



	def elongation(self):

		eqsigma(self.pos_poly, self.promo, self.sens, self.gene_liee_poly, self.longueur, self.sigma, vel)

		
		self.pos_poly += np.round(self.sens[self.gene_liee_poly]*vel).astype(int)


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
