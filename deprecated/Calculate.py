import os
from os import walk
import pickle
from Utils import Utils
import json

types = {
    'pickle': {
        'ext': 'txt',
        'dir': 'pickle',
        'loader': pickle
    },
    'json': {
        'ext': 'json',
        'dir': 'json',
        'loader': json
    }
}
type = types['json']



def getReferenceDicts():
    refDicts = {}
    for (dirpath, dirnames, filenames) in walk('./referemce_dicts/' + type['dir']):
        for filename in filenames:
            # Construct full path
            fullPath = dirpath + "/" + filename
            print("Loading %s...") % (filename)

            data = type['loader'].load(open(fullPath, "r"))

            # Add dictionary item
            refDicts[filename.replace(".txt", "")] = data
    return refDicts

def getTextDocument(path):
    return Utils.testStripping(path)


def classification():
	pH = 900 / (900 * 20)
	max_group = 0
	max_p = 1

	p = pH

	allDicts = []

	# Iterate over all reference dictionaries
	for (key, refDict) in getReferenceDicts().items():

		result = {
			'category': key,
			'hits': 0,
			'p' : 0
		}

		
		
		for word in getTextDocument('./dict/rec.autos/101563'):
			if word in refDict.keys():
				result['hits'] += 1
				result['p'] += refDict[word]
				#p += refDict[word]

		print("Category: " + result['category'] + "\nHits: " + str(result['hits']) + "\nP-ish: " + str(result['p']))
		
		allDicts.append(result)

	probabilities = []
	kvp = {}
	for r in allDicts:
		kvp[r['p']] = r['category']
		probabilities.append(r['p'])
		
	for item in reversed(sorted(probabilities)):
		print(str(kvp[item]) + ": " + str(item))
		
	









classification()