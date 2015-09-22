import json
import pickle

#f = open('mainDict.txt','r')
#output = f.read()
#referenceDict = pickle.loads(output)
#f.close()

f = open('mainDict.json','r')
output = f.read()
referenceDictt = json.loads(output)
f.close()

f = open('mainDict.txt','wb')
pickle.dump(referenceDictt, f)
f.close()





#print("PICKLE: " + str(len(referenceDict)))
#print("JSON: " + str(len(referenceDictt)))