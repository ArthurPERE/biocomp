import numpy as np
import gene
import chromosome as chro
import numpy as np
import os

from donnee import *

from input_ouput import *






# nombre de polymerases
nb_poly = 2


chromo, genes = input_sim("../examples/chrom3genes.gff", "../examples/chrom3genes_rates.dat")





file_gene = open("../result/gene.txt", "w")
file_sigma = open("../result/sigma.txt", "w")

file_gene.write("t\t")

for i in xrange(len(genes)-1):
	file_gene.write("%s\t"% genes[i].nom)


file_gene.write("%s\n"% genes[len(genes)-1].nom)







chromo.genes = np.array(genes)

genes_transcrit = np.zeros(len(genes))


chromo.create_vector(nb_poly)


a = range(10);
time = np.array([0 for i in xrange(nb_poly)])





for t in xrange(temps_simul):
	# vecteur temps de fixation de la polymerase
	print t

	poly_des = np.where(time <= 0)[0]

	if len(poly_des) != 0:
		time[ poly_des ] = chromo.initialisation(poly_des)


	chromo.elongation()

	time -= 1

	poly_term = np.where(time == 0)[0]

	genes_transcrit[ chromo.gene_liee_poly[ poly_term ] ]  += 1




	output_sim(file_gene, file_sigma, time, genes_transcrit, chromo.sigma, t)


file_gene.close()
file_sigma.close()