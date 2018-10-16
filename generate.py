#!/usr/bin/python

#John Wilson 801-14-8684

#Imports
import argparse
import random

#Defines
LENGTH = 0
MAX = 0
FILE_NAME = "input.txt"
OPERATIONS = 'RW'

#Verify for Min/Max of access request to generate
def valid_range(string):
	value = int(string)
	if(value < 1 or value > 10001):
		msg = "This is an invalid value, only values between 1 and 10000"
		raise argparse.ArgumentTypeError(msg)
	else:
		return value

#Verify for Min/Max of Virtual Pages to generate
def valid_max(string):
	value = int(string)
	if(value < 1 or value > 101):
		msg = "This is an invalid value, only values between 1 and 101"
		raise argparse.ArgumentTypeError(msg)
	else:
		return value
		
#Generates the Virtual Memory Access Request
def Generate_Request():
	return str(random.choice(OPERATIONS)) + ':' + str(random.randrange(1,MAX)) + '\n'
		
#---------------------PROGRAM STARTS HERE---------------------#
#Parser Configuration and Parameters
parser = argparse.ArgumentParser(description= "Assigment 03: Memory Management | Virtual Page Access Requests Generator | Generates an input.txt file of format [Operation:Page Address] with Maximum Page of [max] and total amount of page requests of [lenght].")
parser.add_argument("max", type = valid_max, help = "Specify Max Virtual Page that the program can generate")
parser.add_argument("length", type = valid_range, help = "Specify amount of access requests the file will have")
parser.add_argument("-v", "--version", action = 'version', version = '1.0')

#Pass Arguments into namespace and verify inputs comply with arguments
args = parser.parse_args()


#Assign Values
LENGTH = args.length
MAX = args.max

#Initial Print
print("----------PROGRAM STARTED----------")
print("Initial Values are: ")
print("Total Requests: " + str(LENGTH)) 
print("Highest Page Possible: " + str(MAX))
print("")

#Open File
file = open(FILE_NAME, "w")

#Generate Access Requests and put into file
for x in range(0,LENGTH):
	file.write(Generate_Request())

	
#Close File and final print out
file.close()
print ("File with name " + FILE_NAME + " generated with " + str(LENGTH) + " requests with a maximum page number of " + str(MAX) + ".")
