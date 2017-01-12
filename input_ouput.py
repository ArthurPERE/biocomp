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

		l1 = line.split()
		if l1[2] == "region":

			longeur = int(l1[4]) - (int(l1[3]) - 1)

			nom = l1[-1].split(";")[1].split("=")[1]
			id_C = l1[-1].split(";")[0].split("=")[1]

			chromo = chro.chromosome(longeur, nom, id_C)
			del(longeur)
			del(nom)
			del(id_C)

		else :

			nom_gene = l1[-1].split(";")[1].split("=")[1]
			id_gene = l1[-1].split(";")[0].split("=")[1]
	
			if str(l1[6]) == "+":
				genes.append(gene.gene(nom_gene, id_gene, l1[3], l1[4]))

			else :
				genes.append(gene.gene(nom_gene, id_gene, l1[4], l1[3]))

	file_pos.close()

	# extraire les informations des genes pour leurs taux d'initition et de terminaison
	lines = file_taux.readlines()
	for line in lines:
		# ignorer les commantaires
		if line[0] == "#":
			continue
	
		l1 = line.split()
		for i in genes :

			if i.id == l1[1]:
				i.init = float(l1[2])
				i.term = float(l1[3])

	file_taux.close()
	
	return chromo, genes
	
	
def output_sim (file_gene, file_sigma, time, genes_transcrit, sigma, t):

	if len(np.where(time == 0)[0]) != 0:

		file_gene.write("%f\t"%t)

		for i in xrange(len(genes_transcrit)-1):
			file_gene.write("%d\t"%genes_transcrit[i])
	

		file_gene.write("%d\n"%genes_transcrit[len(genes_transcrit)-1])
	

	file_sigma.write("%f\t"%t)

	for i in xrange(len(sigma)-1):
		file_sigma.write("%lg\t"%sigma[i])


	file_sigma.write("%lg\n"%sigma[len(sigma)-1])




