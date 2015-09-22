import os,re, pickle
from collections import Counter
from Utils import Utils
import json
import pickle
import multiprocessing as mp
import random
import itertools
import time

## SETTINGS
numberOfLearningArticlesInSubset = 900;
numberOfLearningArticles = 900 * 20;


### Main Dictionary
## Load our predefined dictionary
f = open('mainDict.txt','r')
output = f.read()
referenceDict = pickle.loads(output)
f.close()

	
def getExampleArticlesFromSubCat(subcat):
	# Ex: subcat  = dict/rec.autos

	# Pick n-learning articles from subset.
	lst = os.listdir(subcat)
	lst = lst[:numberOfLearningArticlesInSubset]

	# Open each file and add it to a list of wooooords.
	subsetWords = []

	for fname in lst:
		subsetWords.extend(Utils.testStripping(subcat + "/" + fname))

	# Many words we got, time to do some counting.
	print("Subset word count: ", len(subsetWords))
	return subsetWords


def mp_calculate(sublist, refDict, refTotal, categoryTotal, randId):

	result = {}
	print("Starting: " + str(randId))
	for word in refDict:
		nForWord = sublist.count(word)
		result[word] = nForWord
	print("Done: " + str(randId))
	return result

	
def mp_handler():

	data = []
	
	# Calculate P(hj) -> numberOfArticlesInSubset / TotalArticlesInExamples
	pHj = numberOfLearningArticlesInSubset / numberOfLearningArticles # 0.05


	for category in os.listdir('./dict'):
		print ('Run %s' % category)
		
		
		item = {}
		item['category'] = category
		item['words'] = []


		## Get all articles for a subcategory, take n articles, and leave n for testing.
		item['words'] = getExampleArticlesFromSubCat('dict/%s' % (category))
		
		
		data.append(item)
		

	
	for item in data:
	
		# Create process pool
		pool = mp.Pool(processes=8)
		
		# Create X processes and input chunk of words to process
		startTime = time.time()
		results = [pool.apply_async(mp_calculate, args=(x, referenceDict, len(referenceDict), len(item['words']), random.random())) for x in Utils.chunks(item['words'], 8)]
		output = [p.get() for p in results]
		endTime = time.time() - startTime
		print("Execution Time: " + str(endTime))
		
		
		# Sum up all occurences of the word in all the sublists
		completeDict = referenceDict.copy()
		for subDict in output:
			for (key, val) in subDict.items():
				completeDict[key] = completeDict[key] + val
				
				
		result = {}
		for (word, occurences) in completeDict.items():
			pForWord = (occurences + 1) / float(len(item['words']) + len(referenceDict))
			result[word] = pForWord
			
	
		
		# Save training data file
		print("Saving: " + item['category'] + " which had " + str(len(item['words'])))
		with open( "%s.json" % (item['category']), "w" ) as outfile:
			json.dump(result, outfile)
		
		
		

	
	
	
	
	
	
	
	
	
if __name__ == '__main__':
	mp_handler()


