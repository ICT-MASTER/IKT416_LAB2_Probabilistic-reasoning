from builtins import input
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE


print("Starting Probabilistic Reasoning...")

options = [
{
	"title": "Create Reference Dictionary",
	"file": "ReferenceDictionary.py"
},
{
	"title": "Create Category Dictionaries",
	"file": "CategoryDictionary.py"
},
{
	"title": "Classify!",
	"file": "Classify.py"
},
{
	"title": "Exit",
	"file": ""
}
]

def startApplication(filename):
	Popen([executable, filename], creationflags=CREATE_NEW_CONSOLE)

c = 0
for opt in options:
	print(str(c) + ". " + dict(opt)['title'])
	c += 1


running = True

while running:	

	value = None
	selectedOption = None
	while value is None:
		try:
			value = int(input("Choice: "))
			selectedOption = dict(options[value])
		except:
			print("Error: Invalid option!")
			value = None
			pass

			

	if value == 0:
		print("Starting " + selectedOption['title'])
		startApplication(selectedOption['file'])
	elif value == 1:
		print("Starting " + selectedOption['title'])
		startApplication(selectedOption['file'])
	elif value == 2:
		print("Starting " + selectedOption['title'])
		startApplication(selectedOption['file'])
	elif value == 3:
		running = False
		exit()
