import os, time, glob, fnmatch,re, json, pickle
import json
from Utils import Utils
## USED FOR CONSTRUCTING A DICT CONATINING ALL THE WORDS FROM ALL TEXTS. REMOVE DUPLICATES.

def scanfolder():

	biglist = []

	for category in os.listdir('./dict'):
		print("Category: " + category)
		documents = os.listdir('./dict/' + category)[:900]
		
		stripped_documents = [Utils.testStripping('./dict/' + category + '/' + doc) for doc in documents]
		
		for strip_doc in stripped_documents:
			biglist.extend(strip_doc)
		
		
	# Remove duplicates
	biglist = list(set(biglist))
	bigdict = {}
	
	for word in biglist:
		bigdict[word] = 0
	
	
	with open( "./mainDict.json", "w" ) as outfile:
		json.dump(bigdict, outfile, indent=4, separators=(',', ': '))
	
		


	return
	os.chdir("dict")
	
	for name in glob.glob('*/*'):
		bigdict.extend(Utils.testStripping(name))

	#print(bigdict)
	print(' Current length  : ',len(bigdict))
	print(' Removing dupes : ')
	finalList = list(set(bigdict))
	print(' New size : ', len(finalList))


	# Make dict
	d = {}
	# Save to disk as dict
	for item in finalList:
		d[item] = 0

	with open( "..\\mainDict.json", "w" ) as outfile:
		json.dump(d, outfile)


	print ("Total length : ",len(d))
	#print(d)



scanfolder();
