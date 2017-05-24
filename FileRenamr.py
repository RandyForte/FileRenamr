import easygui
import os
#easygui.egdemo()

def getFiles(dir):
	print easygui.msgbox('Choose files in the order you wanted them names, EX EP.1 EP.2',"FileRenamr")
	files = []
	while True:
		file = easygui.choicebox("Please choose the file, cancel when done, please note that this program will not add items twice if you accidently choose them,also make sure they are the same extension","FileRenamr",os.listdir(dir))
		if file == None:
			return files
		elif file not in files:
			files.append(file)

def getDirectory():
	print easygui.msgbox('Please choose location of file or files to rename',"FileRenamr")
	return easygui.diropenbox()#you need to add a / when saving

def showRename(directory):
	files =getFiles(directory)#calls the fun that returns a list of the files in order
	fieldNames = ["Title","Season"]
	fieldValues = easygui.multenterbox("Enter info about the show","FileRenamr",fieldNames)
	extension = os.path.splitext(directory+"/"+files[0])[1]
	newNames = []
	for x in range(1,len(files)+1):
		newNames.append(fieldValues[0]+' S'+str(fieldValues[1])+'E'+str(x)+extension)
	print(newNames)
	for x in range(0,len(files)):
		os.rename(directory+"/"+files[x],directory+"/"+newNames[x])

def fileRename(directory):
	if directory == None:
		return
	while True:
		file = easygui.choicebox("Please choose the file, cancel when done, please note that this program will do the extension so you dont have to\nPRESS CANCEL WHEN YOU ARE DONE","FileRenamr",os.listdir(directory))
		if file == None:
			return
		else:
			newName = easygui.enterbox("Enter a new name for: " + file + "Don't worry about file extension", "Filerenamr")
			extension = os.path.splitext(directory+"/"+file)[1]
			os.rename(directory+"/"+file,directory+"/"+newName+extension)
def main():
	directory = getDirectory()
	if directory == None:
		main()
	else:
		while True:
			option = easygui.ynbox("Rename Movie or Show","ReNamer",("File/Movie","TV Show"))
			if option == 0:
				showRename(directory)
			elif option == 1:
				fileRename(directory)
			else:
				break
			directory = getDirectory()
main()
