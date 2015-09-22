import re


class Utils(object):

	@staticmethod
	def chunks(seq, num):
		avg = len(seq) / float(num)
		out = []
		last = 0.0

		while last < len(seq):
			out.append(seq[int(last):int(last + avg)])
			last += avg

		return out

	@staticmethod
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