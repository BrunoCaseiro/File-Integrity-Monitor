# This small little project is not meant to be very robust or aware of possible errors/exceptions
# It works well under some predictable conditions, so it is prone to exceptions


import sys, hashlib, os

# Simple function to calculate md5 hash of a file
def calcFileHash(filepath):
        return hashlib.md5(open(filepath,'rb').read()).hexdigest()


action = input("What should FIM do?\n\nA) Collect a new baseline for files in 'monitor' folder\nB) Start monitoring files in 'monitor' folder with saved baseline\n\n--> ")

# Calculate hashes and create a new baseline.txt
if action == 'A':
	files = os.listdir(os.getcwd()+'/monitor')		# Get files in /monitor folder inside current directory
	hashes = []

	for file in files:
		hashes.append((file, calcFileHash(os.getcwd()+'/monitor/'+file)))	# Creates a list of md5 hashes of previously gathered files
	hashes.sort()


	f = open("baseline.txt", "w")				# Writes and displays the hashes in a pretty way
	for entry in hashes:
		f.write(entry[0] + " | " + entry[1] + "\n")

	f.close()

	print("Done! Please rerun the program with option 'B' to start monitoring the '/monitor' folder for changes")

# Start monitoring files with saved baseline.txt
elif action == 'B':
	# Read baseline.txt to a dict
	## https://youtu.be/WJODYmk4ys8?t=1264

	print('y')

else:
	print("\n\nPlease choose a valid option! Quitting...")
	sys.exit(0)
