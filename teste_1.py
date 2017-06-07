#!/usr/bin/python3
#-*-coding:utf8-*-

#Tests GA_lib
"""
Solve a problem to tif points in a 5th grade function

"""
import ga_lib
import random
from matplotlib import pyplot as plt

#Objective is to reach error 0
#Genes are the roots of a function

def fitness_test(a,b,c,d,e,f):
	y = [(x-5)*(x-10)*(x-15)*(x-20)*(x-25) for x in range(30)]
	y_t = [a*x**5+b*x**4+c*x**3+d*x**2+e*x+f for x in range(30)]
	return sum([(s-t)**2/30 for (s,t) in zip(y,y_t)])**(0.5)

meta = 0;

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(range(30),[(x-5)*(x-10)*(x-15)*(x-20)*(x-25) for x in range(30)],'ro')
line2, =ax.plot(range(30),[0 for _ in range(30)],'bs-')
fig.show()
N=50
#Create random genes
a = [random.randint(-100,100) for i in range(N)]
b = [random.randint(-500,500) for i in range(N)]
c = [random.randint(-200,200) for i in range(N)]
genes = tuple(zip(a,b,c,a,b,c))
#Creates a population
pop = ga_lib.Population()
#Setup the fitness function and target value to population
pop.set_fitness(fitness_test,0)
#Inputs population genes
pop.populate(*genes)
err = 1
i=0
while err > 0.001:
	i=i+1
	#Rank the population
	pop.test_rank()
	#Kill the 50% (N/2) worst
	pop.terminate(int(N/2))
	#Procriate/mutate
	pop.mitosis(chance=0.05,factor=0.1)
	if i%20 == 0:
		err = pop.get_tests()[0]
		a=pop.get_individuals()[0][0]
		b=pop.get_individuals()[0][1]
		c=pop.get_individuals()[0][2]
		d=pop.get_individuals()[0][3]
		e=pop.get_individuals()[0][4]
		f=pop.get_individuals()[0][5]
		fig.suptitle("Cicle: %i. RMS: %6.4f" % (i,err))
		line2.set_ydata([a*x**5+b*x**4+c*x**3+d*x**2+e*x+f for x in range(30)])
		fig.canvas.draw()

