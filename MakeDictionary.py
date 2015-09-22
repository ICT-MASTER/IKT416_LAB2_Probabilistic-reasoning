import os, time, glob, fnmatch,re, json, pickle
import json
from Utils import Utils
## USED FOR CONSTRUCTING A DICT CONATINING ALL THE WORDS FROM ALL TEXTS. REMOVE DUPLICATES.

def scanfolder():
    os.chdir("dict")
    bigdict = ['']
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
