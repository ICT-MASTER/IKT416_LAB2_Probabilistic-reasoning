import os, time, glob, fnmatch


def scanfolder():
    os.chdir("dict")
    for name in glob.glob('*/*'):
        #f = open(name,'r')
        #text = f.read()
        print(name)

def testStripping():
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
    "References:","Article-I.D.:","Reply-To:"]
    result = ""

    with open('test') as oldfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                result+=line;

    # Make all lowercase

    # Remove all emails
    match = result.findall(r'[\w\.-]+@[\w\.-]+', result)

    for s in match:
        result.replace(s, "")

    print(result)


#scanfolder();
testStripping()
