import os
import json
from os import walk
from Utils import Utils
import multiprocessing as mp
import random
import math

dictionary_path = "./dict"
pool_size = 8 #mp.cpu_count()




def sp_getDictionaries():
    refDicts = {}
	
    for (dirpath, dirnames, filenames) in walk('./referemce_dicts/json'):
	
        for filename in filenames:
			
            # Construct full path
            fullPath = dirpath + "/" + filename
		
            print("Loading "+filename+"...")

			# Load reference dict
            data = json.load(open(fullPath, "r"))

            # Add dictionary item
            refDicts[filename.replace(".txt", "")] = data
					
    return refDicts

def sp_getTextDocument(path):
    return Utils.testStripping(path)

def sp_getTestData():
	testData = []

		
	# Generate list of test data
	document_paths = [{
		'path': dictionary_path + "/" + x,
		'category': x
	} for x in os.listdir(dictionary_path)]
	for document_path in document_paths:
		testData.extend([{
			'path': document_path['path'] + "/" + doc,
			'category': document_path['category'],
			'text': sp_getTextDocument(document_path['path'] + "/" + doc)
		} for doc in os.listdir(document_path['path'])[901:]])
	
	return testData

	
def mp_classify(params):
	
	id = random.random()
	dictionaries = params['dict']
	document = params['case']
	

	pH = 0.05#900 / (900 * 20)
	#print("Starting case: " + document['path'])
	
	result = {
		'category': document['category'],
		'path': document['path'],
		'probabilities': {}
	}
	
	for (key, category_dict) in dictionaries.items():
		dict_words = category_dict.keys()
	
		
		# Set initial probability
		result['probabilities'][key] = 0
		
		# Count occurrences of word in category_dictionary
		
		p = math.log(0.05)
		for word in document['text']:
			if word in dict_words:
				p += math.log(category_dict[word])
				
		result['probabilities'][key] = p
			
			#nOccurrence = dict_words.count(word)
			
			#if nOccurrence == 0:
			#	continue
				
			#result['probabilities'][key] += (category_dict[word] * nOccurrence)
	
	
	return result


def mp_start_process():
    print('Starting', mp.current_process().name)
	
	
def sp_handler():
	testData = sp_getTestData()
	random.shuffle(testData)
	dictionaries = sp_getDictionaries()


	# Create process pool
	pool = mp.Pool(
		processes=pool_size,
		#initializer=mp_start_process
	)
	
	# Prepare imap data
	paramData = [{
		'case': x,
		'dict': dictionaries
	} for x in testData]
	
	correct = 0
	total = 0
	
	
	for document_result in pool.imap_unordered(mp_classify, paramData):
		total += 1
	
		#print("-----------")
		#print("Category: " + document_result['category'])
		#print("Case: " + document_result['path'])
		#print("-")
		
		# Order
		ordered_prob = list(reversed(sorted(document_result['probabilities'].items(), key=lambda x:x[1])))
		
		
		if ordered_prob[0][0].replace(".json", "") == document_result['category']:
			correct += 1
		
		print(ordered_prob[0][0].replace(".json", "") + " == " + document_result['category'] + " | " + str(correct) + "/" + str(total) + " | " + str((correct / total) * 100.0) + "%")
		
		
		#for i in ordered_prob:
		#	print(str(i[0]) + ": " + str(i[1]))


	
	

	
	
	
	""""future_results = [pool.apply_async(mp_classify, args=(dictionaries, x, random.random())) for x in testData]
	for res in future_results:
		print res.get()
	
		for document_result in res.get():
			print("-----------")
			print("Category: " + document_result['category'])
			print("Case: " + document_result['path'])
			print("-")
			
			# Order
			ordered_prob = reversed(sorted(document_result['probabilities'].items(), key=lambda x:x[1]))
			for i in ordered_prob:
				print(str(i[0]) + ": " + str(i[1]))
	"""
	

		
		


	""""chunks = [testData[x:x+pool_size] for x in xrange(0, len(testData), pool_size)]
	for testDataChunk in chunks:	
		results = [pool.apply_async(mp_classify, args=(dictionaries, x, random.random())) for x in testDataChunk]
		final_result = [p.get() for p in results]
		
		print("Chunk Done!...")
		for document_result in final_result:
			print("-----------")
			print("Category: " + document_result['category'])
			print("Case: " + document_result['path'])
			print("-")
			
			# Order
			ordered_prob = reversed(sorted(document_result['probabilities'].items(), key=lambda x:x[1]))
			for i in ordered_prob:
				print(str(i[0]) + ": " + str(i[1]))
	"""
	
			
	
	

	
	
if __name__ == '__main__':
	sp_handler()



