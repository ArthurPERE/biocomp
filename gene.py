class gene:
	
	def __init__(self, nom_gene, id_gene, position_deb, position_fin) :
		self.nom = nom_gene
		self.id = id_gene
		self.position_deb = int(position_deb)
		self.position_fin = int(position_fin)
		self.longeur = abs(self.position_fin - (self.position_deb)) + 1

		self.init = 1
		self.term = 1

		self.transcript = 0

	def __repr__(self) :
		return "id = %s, longeur = %d, transcript = %d"%(self.id, self.longeur, self.transcript)

