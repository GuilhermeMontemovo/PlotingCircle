import math
import matplotlib.pyplot as plt

def pointPlot(x, y): #ploting the points on the 8 octants
	plt.scatter(x, y)	
	plt.scatter(-x, y)
	plt.scatter(-x, -y)
	plt.scatter(x, -y)
	plt.scatter(y, x)	
	plt.scatter(y, -x)
	plt.scatter(-y, -x)
	plt.scatter(-y, x)
	return

def incrementalCalc(radio): # calculating the matrix by using a incremental algorithim 
	x = 0
	y = radio
	d = 1 - radio
	dE = 3
	dSE = (-2)*radio + 5

	pointPlot(x, y)

	while y > x:
		if d < 0:
			d += dE
			dE += 2
			dSE += 2

		else:
			d += dSE
			dE += 2
			dSE += 4
			y -= 1
		x += 1		
		pointPlot(x, y)
	

def sphericalCoord(radio):  
	x = radio
	y = 0
	angle = 0
	increment = math.pi/(4*radio)

	
	while angle <= math.pi/4:
		pointPlot(radio*math.cos(angle), radio*math.sin(angle))
		angle += increment
		
	return

def tradAbord(radio):
	
	for x in range(radio+1):
		pointPlot(x, math.sqrt(math.pow(radio, 2) - math.pow(x, 2))) 

	return


#interface

op = (input("Escolha a operacao:\n1: Incremental\t2: Coordendas esfericas\t3: Abordagem tradicional\n"))
print(op)
radio = int(input("Qual o raio?\n"))

if op == '1':
	incrementalCalc(radio)
elif op == '2':
	sphericalCoord(radio)
elif op == '3':
	tradAbord(radio)


plt.axis('equal')
plt.grid(True)
plt.show()
