#!/usr/bin/python3
#-*-coding:utf8-*-

#Implements a simple GA module

import random
import operator

class Population:
	individuals = []
	rank = []
	fitness = lambda: None
	best = 0
	def set_fitness(self, fit,b):
		self.fitness = fit
		self.best=b
	
	def populate(self,*gene_list):
		del self.individuals[:]
		for gl in gene_list:
			self.individuals.append(gl)
	
	def test_rank(self):
		self.rank = [abs(self.best-self.fitness(*gl)) for gl in self.individuals]
		#reorder the individuals
		self.individuals = [y for (x,y) in sorted(zip(self.rank,self.individuals),key=lambda k:k[0])] 
	
	def terminate(self,n=None):
		if (n==None): #Terminate all
			del self.individuals[:]
			del self.rank[:]
			self.best = 0
			self.fitness = lambda: None
		elif (n<=len(self.individuals)and isinstance(n,(int))):
			#Remove n last individuals
			del self.individuals[-n:]
			#print (len(self.individuals))
		else:
			pass
	
	def mitosis(self, chance=0.05, factor=0.1):
		#double individuals by mitosis
		#mutations may happen in a chance by a factor 
		indiv = len(self.individuals)
		for ind in range(indiv):
			self.individuals.append(tuple([t+random.triangular(-factor,factor)*(1 if random.random() < chance else 0) for t in self.individuals[ind]]))
	
	def get_individuals(self,*args):
		if len(args) == 0:
			return self.individuals
		elif len(args) == 1:
			return self.individuals[:args[0]]
		elif len(args) >=2:
			return self.individuals[args[0]:args[1]]
	
	def get_tests(self):
		return [self.fitness(*gl) for gl in self.individuals]
