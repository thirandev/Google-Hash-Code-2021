import multiprocessing as mp
import math
import sys
import itertools
from subCode1 import Street 
from subCode2 import Car 
from subCode3 import Inter

def start(fileName):
			
	with open("Input/" + fileName, 'r') as inputfile:

		infoLine = inputfile.readline().rstrip("\n")
		info = infoLine.split(" ")

		maxTime = int(info[0])
		numInters = int(info[1])
		numStreets = int(info[2])
		numCars = int(info[3])
		bonusScore = int(info[4])


		allInters = []
		for interI in range(numInters):
			inter = Inter(interI)
			allInters.append(inter)


		allStreets = []
		streetDict = {}
		for streetI in range(numStreets):
			streetInfo = inputfile.readline().rstrip("\n").split(" ")
			street = Street(streetI, int(streetInfo[0]), int(streetInfo[1]), streetInfo[2], int(streetInfo[3]))
			allStreets.append(street)
			streetDict[street.name] = street
			
			allInters[street.begin].outs.append(street)
			allInters[street.end].ins.append(street)


		allCars = []
		for carI in range(numCars):
			carInfo = inputfile.readline().rstrip("\n").split(" ")
			path = []
			timeRemaining = maxTime
			for i in range(1, len(carInfo)):
				street = streetDict[carInfo[i]]
				path.append(street)

			for streetI in range(1, len(path)):
				street = path[streetI]
				timeRemaining -= street.time
				
			car = Car(carI, path, timeRemaining)
			allCars.append(car)


	for inter in allInters:
		print(inter.ins)
		for s in inter.ins:
			inter.schedule.append((s.index, 1))


	with open("Output/" +"output-" + fileName, "w") as txt_file:
		outInt = tuple(filter(lambda i: len(i.schedule) > 0, allInters))
		txt_file.write(str(len(outInt)))
		for inter in outInt:
			txt_file.write(f"\n{inter.index}")
			txt_file.write(f"\n{len(inter.schedule)}")
			for step in inter.schedule:
				txt_file.write(f"\n{allStreets[step[0]].name} {step[1]}")

start("a.txt")
start("b.txt")


	
	
