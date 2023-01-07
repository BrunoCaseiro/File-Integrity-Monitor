# This small little project is not meant to be very robust or aware of possible errors/exceptions
# It works well under some predictable conditions, so it is prone to exceptions
# It is also not the most efficient code, but that's not the point
# Scripting in cybersecurity means to write code fast and make it work asap, mostly for personal use
# OBVIOUSLY this depends on the situation

import sys, hashlib, os, time

# Simple function to calculate md5 hash of a file
def calcFileHash(filepath):
        return hashlib.md5(open(filepath,'rb').read()).hexdigest()


action = input("What should FIM do?\n\nA) Collect a new baseline for files in 'monitor' folder\nB) Start monitoring files in 'monitor' folder with saved baseline\n\n--> ")

# Calculate hashes and create a new baseline.txt
if action == 'A':
	files = os.listdir(os.getcwd()+'/monitor')		# Get files in /monitor folder inside current directory
	hashes = {}

	for file in files:
		hashes[file] = calcFileHash(os.getcwd()+'/monitor/'+file)	# Creates a list of md5 hashes of previously gathered files

	hashes = dict(sorted(hashes.items()))			# Sorts dictionary by keys

	f = open("baseline.txt", "w")				# Writes and displays the hashes in a pretty way
	for key in hashes.keys():
		f.write(key + " | " + hashes[key] + "\n")

	f.close()

	print("Done! Please rerun the program with option 'B' to start monitoring the '/monitor' folder for changes")
	print("Here is the created baseline file:\n")

	with open('baseline.txt', 'r') as f:
		print(f.read())

# Start monitoring files with saved baseline.txt
elif action == 'B':
	# Read baseline.txt to a list
	f = open("baseline.txt", "r")
	tempHashes = {}

	for line in f:
		tempHashes[line.split('|')[0].strip()] = line.split('|')[1][:-1].strip()		# [:-1] in order to NOT add the newline character to the tuple

	while(True):
		tempHashes = dict(sorted(tempHashes.items()))
		print(tempHashes)

		time.sleep(2)				# Check hashes every 3 seconds --> This can be changed, maybe taken as an argument
		files = os.listdir(os.getcwd()+'/monitor')
		for file in files:
			if file not in tempHashes.keys():
				print("[" + str(time.time()).split('.')[0] + "] File " + file + " has been created!")		# print a simplified timestamp along with the alert
				tempHashes[file] = calcFileHash(os.getcwd()+'/monitor/'+file)
			else:
				if(calcFileHash(os.getcwd()+'/monitor/'+file) != tempHashes[file]):
					print("[" + str(time.time()).split('.')[0] + "] File " + file + " has been modified!")
					tempHashes[file] = calcFileHash(os.getcwd()+'/monitor/'+file)

		for key in list(tempHashes.keys()):
			if key not in files:
				print("[" + str(time.time()).split('.')[0] + "] File " + key + " has been deleted!")
				del tempHashes[key]
else:
	print("\n\nPlease choose a valid option! Quitting...")
	sys.exit(0)
