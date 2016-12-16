import gene as g
import numpy as np
from math import *

class chromosome:
	# longeur du genome
	def __init__(self, longeur, nom, id_c):
		self.longeur = longeur
		self.nom = nom
		self.id = id_c

		# le tableau de genes
		self.genes = []

		self.sigma = np.array([-0.4 for i in xrange(longeur)])

		
	
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



	def calcK(self):
		f_0 = self.sigma[self.promo]
		print f_0

		K = self.fonction_sigma(f_0)
		K *= self.taux_init
		K /= sum(K)
		return K


	'''
	def etape_init(self,sigma): 
 
		self.taux_init = [] ##vecteur des taux pour chaque gene 
		self.prob_init = [] ##vecteur des prob pour chaque gene 
		self.sigma=sigma 
		self.indice = []    ## vecteur 0 non transcrit, 1 oui 
		self.tab=[] #tester print la longeur 
		for i,x in enumerate(self.chrome): ##i indice gene 
			taux_i = self.taux_basal[i]*self.fonction_sigma(self.sigma[i]) 
			self.taux_init.append(taux_i) 
			self.tab.append(x.p()) #appelle la longeur 
		for i,x in enumerate(self.chrome): 
			prob_i = self.taux_init[i]/(sum(self.taux_init)) 
			prob = randint(0,1) 
			if prob_i<prob: 
				indice_i=0 
			else: indice_i=1 
			self.prob_init.append(prob_i) 
			self.indice.append(indice_i) 
		return(self.prob_init,self.indice,self.tab) 
	'''

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