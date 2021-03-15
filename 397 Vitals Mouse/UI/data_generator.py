#this script can generate heart beat and o2 data values for use in testing. it has functions for both single values (for use in live feed), and a data set.
import random
import os
import csv

def singleGenerate(baseVal, rangeVal):
	x = random.randint(baseVal - rangeVal,baseVal + rangeVal)
	return x

def multiGenerate(baseVal, rangeVal, numEntries):
	i = 1
	returnData = [None]*numEntries
	while i <= numEntries:
		tempVal = singleGenerate(baseVal,rangeVal)
		returnData[i-1] = (tempVal)
		i += 1

	return returnData







if __name__ == "__main__":
	print("This program will generate heart rate and O2 level data for use in test")
	print("Please enter a base heartrate")
	baseHR = int(input())
	print("Please enter a HR variance")
	rangeHR = int(input())
	print("Please enter a base 02")
	baseOT = int(input())
	print("Please enter a 02 variance")
	rangeOT = int(input())
	print("Please enter the number of samples")
	numSamples = int(input())

	dataHR = multiGenerate(baseHR, rangeHR, numSamples)
	dataOT = multiGenerate(baseOT, rangeOT, numSamples)
	print(dataHR)
	print(dataOT)
	print("Please enter a valid file name")
	filename = input()
	f = open(filename, 'w')

	f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')

	i = 1
	while i <= numSamples:
		print('working')
		f_writer.writerow([i-1,dataHR[i-1],dataOT[i-1]])
		i += 1
	f.close()







