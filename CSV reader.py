#Read Image names into CSV:
#Read every 10 images per letter folder:
import os
import csv

directory = "S:/GATECH Documents/Hackathon/HacklyticsASL/asl_alphabet_train"
csvName = "namesPer10.csv"
def readIntoCSV(dir,csvName):
	allNames = []
	letters = [chr(a) for a in range(65,91)]
	for char in letters:
		names = os.listdir(dir+"/"+char)
		new = [names[b] for b in range(len(names)) if b % 10 == 0]
		for name in new:
			allNames.append(name)
	with open(csvName, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for name in allNames:
			writer.writerow([name])

def printRead(dir):
	allNames = []
	letters = [chr(a) for a in range(65,91)]
	for char in letters:
		names = os.listdir(dir+"/"+char)
		new = [names[b] for b in range(len(names)) if b % 10 == 0]
		for name in new:
			allNames.append(name)
	print(allNames)

printRead(directory)
print(readIntoCSV(directory,csvName))