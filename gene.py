from donnee import *

class gene:
	
	def __init__(self, nom_gene, id_gene, position_deb, position_fin) :
		self.nom = nom_gene
		self.id = id_gene
		self.position_deb = int(int(position_deb) / l)
		self.position_fin = int(int(position_fin) / l)
		self.longueur = abs(self.position_fin - self.position_deb) + 1

		if ( self.position_deb > self.position_fin ):
			self.sens = -1
		else :
			self.sens = 1


		self.init = 1
		self.term = 1

		self.transcript = 0


	def __repr__(self) :
		return "id = %s, longeur = %d, transcript = %d"%(self.id, self.longueur, self.transcript)

