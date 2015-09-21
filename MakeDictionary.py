import os, time, glob, fnmatch,re, json, pickle

## USED FOR CONSTRUCTING A DICT CONATINING ALL THE WORDS FROM ALL TEXTS. REMOVE DUPLICATES.

def scanfolder():
    os.chdir("dict")
    bigdict = ['']
    for name in glob.glob('*/*'):
        bigdict.extend(testStripping(name))

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

    pickle.dump( d, open( "..\\mainDict.txt", "wb" ) )

    print ("Total length : ",len(d))
    print(d)




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


scanfolder();
