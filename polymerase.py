
import numpy as np


class Polymerase:

	def __init__(self):

		self.vitesse = 	np.random.randint(25, 50)

		self.fixee = False

		self.x = 0

	

	# prob_genes = listes de toutes les probabilite initiation pour chaque genes
	# genes = listes de tous les genes
	def initiation(self, prob_genes, genes):

		l = len(genes)
		gene1 = rd.sample(range(l), l)

		for gene in gene1:

			
			# si la polymerase est accepte
			if rand() < prob_genes[gene] :

				self.fixee = True

				self.x = genes[gene].debut

				return True

		return False


for i in xrange(20):
	a = Polymerase()

	# a.initiation(range(10))

'''
a = np.random.randint(10, size = 10)

b = np.where(a == 0)[0]


print a 
print b'''