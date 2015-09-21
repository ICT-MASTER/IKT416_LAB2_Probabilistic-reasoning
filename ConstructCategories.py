import os,re, pickle

## SETTINGS
numberOfLearningArticlesInSubset = 900;
numberOfLearningArticles = 900*20;

def createSubCat():

    dictList=['comp.graphics','comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x',
    'misc.forsale','rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey','sci.crypt','sci.electronics',
    'sci.med','sci.space','soc.religion.christian','talk.politics.guns','talk.politics.mideast','talk.politics.misc','talk.religion.misc']

    for x in range(len(dictList)):
        print ('Run %x' % x)
        # Calculate P(hj) -> numberOfArticlesInSubset / TotalArticlesInExamples
        pHj = numberOfLearningArticlesInSubset / numberOfLearningArticles


        # Combine all text from all examples to a string
        print(dictList[x])
        ## Get all articles for a subcategory, take n articles, and leave n for testing.
        listOfWord = getExampleArticlesFromSubCat('dict/%s' % (dictList[x]))
        ## Number of words in subset called n
        numberOfWordsInSubset = len(listOfWord)



        ## Load our predefined dictionary
        with open('mainDict.txt','r') as f:
            output = f.read()
            referenceDict = pickle.loads(output)

        ## Iterate each word in the vocabulary / referenceDict
        numOfIter = 0
        for word in referenceDict:
            nForWord = listOfWord.count(word)
            # Variables
            numberOfTotalWords = len(listOfWord)
            numbertOfDictWords = len(referenceDict)

            # Calculate percentage
            pForWord = (nForWord+1)/float((numberOfTotalWords+numbertOfDictWords))
            referenceDict[word] = pForWord

            # Save subcat to file..

        pickle.dump(referenceDict, open( "%s.txt" % (dictList[x]), "wb" ))
        print(referenceDict)



    # For each word, calculate (Wk|Hj) and construct the final dict with prob.




def getExampleArticlesFromSubCat(subcat):

    # Pick n-learning articles from subset.
    lst=os.listdir(subcat)
    lst = lst[:numberOfLearningArticlesInSubset]

    # Open each file and add it to a list of wooooords.
    subsetWords = [""]

    for fname in lst:
        subsetWords.extend(testStripping(subcat+"/"+fname))

    # Many words we got, time to do some counting.
    print("Subset word count : ", len(subsetWords))
    return subsetWords

# Same stripping method as in MakeDictionary - keep this shit consistent. Does not del dupes..
def testStripping(openFile):
    bad_words = ['Xref:',
    'Path:',"From:","Newsgroups:",
    "Subject:","Summary:","Keywords:",
    "Message-ID:","Date:","Expires:",
    "Followup-To:","Distribution:",
    "Organization:","Approved:",
    "Supersedes:","Lines:",
    "Archive-name:",
    "Alt-atheism-archive-name:",
    "Last-modified:",
    "Version: 1.0",
    "NNTP-Posting-Host:",
    "References:","Article-I.D.:","Reply-To:","Sender:",
    "X-Newsreader:","Nntp-Posting-Host:"]
    result = ""

    with open(openFile) as oldfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                result+=line;


    result = result.lower()
    match = re.compile('[A-Za-z]+').findall(result)
    return match

print("Y2O")
createSubCat();
