import gene as g
import numpy as np

class chromosome:
	# longeur du genome
	def __init__(self, longeur, nom, id_c):
		self.longeur = longeur
		self.nom = nom
		self.id = id_c

		# le tableau de genes
		self.genes = False

		self.sigma = np.array([10 for i in xrange(longeur)])

		
	

	## le f(sigma) dans l'equation de taux d'init
	def fonction_sigma(self,sigma):
		sigma_t = 10
		epsilon = 0.1
		g_sigma = m/(1+exp(sigma-sigma_t)/epsilon)
		prob_sigma = exp(g_sigma)

		return prob_sigma



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