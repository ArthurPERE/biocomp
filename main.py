
class gene:
	
	def __init__(self, nom_gene, id_gene, position_deb, position_fin, longeur) :
		self.nom_gene = nom_gene
		self.id_gene = id_gene
		self.position_deb = position_deb
		self.position_fin = position_fin
		self.longeur = longeur


		self.transcript = 0

	def __repr__(self) :
		return "id = %s, nom = %s, longeur = %d, transcript = %d"%(self.id_gene, self.nom_gene, self.longeur, self.transcript)



# lecture des fichiers
file = open("/home/arthur/Documents/Projet/proj_biocomp/examples/chrom3genes.gff","r")

lines = file.readlines()


for line in lines:
	
	if line[0] == "#":
		continue

	l = line.split()

	if l[2] == "region":

		longeur = int(l[4]) - (int(l[3]) - 1)

		nom = l[-1].split(";")[1].split("=")[1]
		id_C = l[-1].split(";")[0].split("=")[1]

		print longeur, nom, id_C

	else :

		longeur = int(l[4]) - (int(l[3]) - 1)

		nom_gene = l[-1].split(";")[1].split("=")[1]
		id_gene = l[-1].split(";")[0].split("=")[1]

		sens = str(l[6])

		if sens == "+":
			g = gene(nom_gene, id_gene, l[3], l[4],longeur)
			print g

		else :
			g = gene(nom_gene, id_gene, l[4], l[3],longeur)
			print g
		



