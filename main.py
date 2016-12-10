import numpy as np
import polymerase as poly
import gene
import chromosome as chro
import numpy as np


# vecteur de gene
genes = []


# extraire les informations des genes pour leur position dans le genome
file = open("../examples/chrom3genes.gff","r")
lines = file.readlines()

for line in lines:
	
	# ignorer les commantaires
	if line[0] == "#":
		continue

	l = line.split()
	if l[2] == "region":

		longeur = int(l[4]) - (int(l[3]) - 1)

		nom = l[-1].split(";")[1].split("=")[1]
		id_C = l[-1].split(";")[0].split("=")[1]

		chromo = chro.chromosome(longeur, nom, id_C)
		del(longeur)
		del(nom)
		del(id_C)

	else :

		nom_gene = l[-1].split(";")[1].split("=")[1]
		id_gene = l[-1].split(";")[0].split("=")[1]

		if str(l[6]) == "+":
			genes.append(gene.gene(nom_gene, id_gene, l[3], l[4]))

		else :
			genes.append(gene.gene(nom_gene, id_gene, l[4], l[3]))

file.close()

# extraire les informations des genes pour leurs taux d'initition et de terminaison
file = open("../examples/chrom3genes_rates.dat")
lines = file.readlines()
for line in lines:
	# ignorer les commantaires
	if line[0] == "#":
		continue
	
	l = line.split()
	for i in genes :

		if i.id == l[1]:
			i.init = float(l[2])
			i.term = float(l[3])

file.close()
del(lines)
del(line)


# donner la 
chromo.genes = np.array(genes)

print chromo.genes
print chromo.longeur