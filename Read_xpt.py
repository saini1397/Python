#Import required Libraries
import os
import xport as xp

#Changing the current directory.
os.chdir('C:/Training/PilotProjectData/cdiscpilot_SDTM/SDTM')

#Read all files,directory and subdirectory from the path provided above.
for subdir, dirs, files in os.walk('.'):
    pass

#Function has been created , it would return xpt to a dataframe 	
def xptodf(i):
     with open(i, 'rb') as f:
            return xp.to_dataframe(f)
#Since we could have files other than .xpt; so we are reading all files which ends with .xpt         
for i in files:
    if i.endswith(".xpt"):
#Initialize indx variable, find will return the index position where string starts with .xpt	
        indx = i.find(".xpt")
#Removing the .xpt text since file name should not contain any extension applied formating to change i to given file name 		
        globals()['%s' % i[0:indx]] = xptodf(i)