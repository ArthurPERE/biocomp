# -*- coding: utf-8 -*-
from numpy import *
from math import *
from random import *

### Fichier à traiter ###
fichier = open("chrom3genes.gff","r")
info_gene = open("info_gene.txt","w")
#-----------------------------------------------------------------------------------------------------------------------------
#            PARAMETRES
#-----------------------------------------------------------------------------------------------------------------------------
global sigma_t
global m
global epsilon

sigma_t=-0.4
epsilon=0.01
m=1



chaine ="#"
nbr_ligne = 0

### Parcours du fichier ###
for ligne in fichier:
	if chaine not in ligne:
		ligne = ligne.split("\t")
		if ligne[2]=="gene":
			nom_gene = str(ligne[8].split(";")[1].split("=")[1]).rstrip('\n')
			position_start = int(ligne[3])
			postion_stop = int(ligne[4])
			fichier2 = open("chrom3genes_rates.dat","r") #### IL FAUT OUVRIR LE DEUXIEME FICHIER ICI!!! SINON BUG
			for ligne2 in fichier2:
				ligne2 = ligne2.split("\t")
				if ligne2[1] in nom_gene:
					taux_init = float(ligne2[2])
					taux_termi= float(ligne2[3])
					info_gene.write("%s\t%i\t%i\t%i\t%i\n"%(nom_gene,position_start,postion_stop,taux_init,taux_termi))
fichier.close()
info_gene.close()

class gene:
	def __init__(self, longeur):
		self.longeur=longeur
	def p(self): #c'est pour tester
		return(self.longeur)

class chromosome:
	def __init__(self, taux_basal,nb,longeur):
		self.chrome=[gene(longeur=longeur[i]) for i in range(nb) ]
		self.taux_basal = taux_basal ##un vecteur des taux de basal
		self.nb = nb ##nombre de gene sur le chromosome
	
	def fonction_sigma(self,sigma): ## le f(sigma) dans l'equation de taux d'init
		g_sigma = m/(1+exp(sigma-sigma_t)/epsilon)
		prob_sigma = exp(g_sigma)
		return(prob_sigma)

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


taux_basal=[100,20,1000]
sigma = [1,1,1]
longeur=[76,46,50]
chrom1= chromosome(taux_basal,3,longeur)
chrom1.simulation(sigma)