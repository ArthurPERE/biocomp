# -*- coding: utf-8 -*-


### Fichier à traiter ###
fichier = open("chrom3genes.gff","r")
info_gene = open("info_gene.txt","w")
### Variables globales ###
#NB_MISMATCH = 2

### Variables ###
#nb_sequence_non_alignee = 0
#nb_sequence_alignee_ambigue = 0
#sequence_aligne = {}
#sequence_aligne_ambigue = []

#for mis in range(NB_MISMATCH +1) : sequence_aligne[mis] = 0
chaine ="#"
nbr_ligne = 0

### Parcours du fichier ###
for ligne in fichier:
	if chaine not in ligne:
		ligne = ligne.split("\t")
		if ligne[2]=="gene":
			print ligne[8]
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

