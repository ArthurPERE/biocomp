import gene
import chromosome as chro
import numpy as np

from donnee import *



def input_sim(chemin_gene_pos, chemin_gene_taux):
	
	file_pos = open(chemin_gene_pos, "r")
	file_taux = open(chemin_gene_taux, "r")
	
	lines = file_pos.readlines()
	
	genes = []

	for line in lines:
	
		# ignorer les commantaires
		if line[0] == "#":
			continue

		l = line.split()
		if l[2] == "region":

			longueur = int(l[4]) - (int(l[3]) - 1)

			nom = l[-1].split(";")[1].split("=")[1]
			id_C = l[-1].split(";")[0].split("=")[1]

			chromo = chro.chromosome(longueur, nom, id_C)
			del(longueur)
			del(nom)
			del(id_C)

		else :

			nom_gene = l[-1].split(";")[1].split("=")[1]
			id_gene = l[-1].split(";")[0].split("=")[1]
	
			if str(l[6]) == "+":
				genes.append(gene.gene(nom_gene, id_gene, l[3], l[4]))

			else :
				genes.append(gene.gene(nom_gene, id_gene, l[4], l[3]))

	file_pos.close()

	# extraire les informations des genes pour leurs taux d'initition et de terminaison
	lines = file_taux.readlines()
	for line in lines:
		# ignorer les commantaires
		if line[0] == "#":
			continue
	
		l = line.split()
		for i in genes :

			if i.id == l[1]:
				i.init = float(l[2])
				i.term = float(l[3])

	file_taux.close()
	
	return chromo, genes
	
	
def output_sim (file_gene, file_sigma, time, genes_transcrit, sigma, t):

	if len(np.where(time == 0)[0]) != 0:

		file_gene.write("%d\t"%t)

		for i in xrange(len(genes_transcrit)-1):
			file_gene.write("%d\t"%genes_transcrit[i])
	

		file_gene.write("%d\n"%genes_transcrit[len(genes_transcrit)-1])
	

	file_sigma.write("%d\t"%t)

	for i in xrange(len(sigma)-1):
		file_sigma.write("%f\t"%sigma[i])


	file_sigma.write("%f\n"%sigma[len(sigma)-1])