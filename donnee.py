D = 100
l = 10

step = 0.4

vel = 25. # en nucleotide par seconde

vel /= l
vel *= step

temps_simul = 10 # En minute

temps_simul *= 60 # converti en seconde




J0 = 0.1


def frange(start, stop, step_):
	i = start

	while i < stop:
		i += step_
		yield i
		