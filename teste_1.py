#!/usr/bin/python3
#-*-coding:utf8-*-

#Teste simples da GA_lib
import ga_lib
import random
from matplotlib import pyplot as plt

#O objetivo é o menor erro na previsão da reta y=3x^2+5x-7
#Os genes são a inclinação e o offset

def fitness_test(a,b,c,d,e):
	y = [(x-5)*(x-10)*(x-15)*(x-20)*(x-25) for x in range(30)]
	y_t = [(x-a)*(x-b)*(x-c)*(x-d)*(x-e) for x in range(30)]
	return sum([(e-d)**2/30 for (e,d) in zip(y,y_t)])**(0.5)

meta = 0;

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(range(30),[(x-5)*(x-10)*(x-15)*(x-20)*(x-25) for x in range(30)],'ro')
line2, =ax.plot(range(30),[0 for _ in range(30)],'bs-')
fig.show()
N=50
#cria os gens
a = [random.randint(-100,100) for i in range(N)]
b = [random.randint(-500,500) for i in range(N)]
c = [random.randint(-200,200) for i in range(N)]
genes = tuple(zip(a,b,c,a,b))
#Cria a populacao

#print("Cria populacao")
pop = ga_lib.Population()
#print("Insere os gens")
pop.set_fitness(fitness_test,0)
#print("Fitness function")
pop.populate(*genes)
err = 1
i=0
while err > 0.001:
	i=i+1
	#print("Testa")
	pop.test_rank()
	#print("Mata")
	pop.terminate(int(N/2))
	#print("Multiplica")
	pop.mitosis(chance=0.05,factor=0.1)
	#pop.mitosis(chance=0.05,factor=0.1)
	#print("Imprime")
	if i%20 == 0:
		err = pop.get_tests()[0]
		a=pop.get_individuals()[0][0]
		b=pop.get_individuals()[0][1]
		c=pop.get_individuals()[0][2]
		d=pop.get_individuals()[0][3]
		e=pop.get_individuals()[0][4]
		fig.suptitle("Cicle: %i. RMS: %6.4f" % (i,err))
		line2.set_ydata([(x-a)*(x-b)*(x-c)*(x-d)*(x-e) for x in range(30)])
		fig.canvas.draw()

