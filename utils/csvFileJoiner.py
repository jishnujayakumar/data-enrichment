import os
import errno
import pandas as pd

class csvFileJoiner:

	fileFrames = []
	dirContainsFile = False
	joinedFrame = None

	def __init__(self, fileDirectoryPath):
		self.fileDirectoryPath = fileDirectoryPath
		for file in os.listdir(self.fileDirectoryPath):
		    if file.endswith(".csv"):	
		    	dataframe=pd.read_csv(os.path.join(self.fileDirectoryPath, file))
		    	dataframe.columns = map(str.upper, dataframe.columns) #Converting the coloumn header to upper case (Capital case)
		    	self.fileFrames.append(dataframe)	
		if len(self.fileFrames) > 0:	
			self.dirContainsFile = True

	def joinAndGenerateCSVFiles(self, path, fileName):
		if(self.dirContainsFile):
			self.joinedFrame = pd.concat(self.fileFrames, join='outer')
			#self.joinedFrame = pd.merge(self.fileFrames[0],self.fileFrames[1], on=keys, how=method)	
			self.makeSurePathExists(path)
			pd.DataFrame.to_csv(self.joinedFrame,os.path.join(path, fileName),header=True, index=False,index_label=None)
			print "Output: " + str(os.path.abspath(os.path.join(path, fileName)))
		else:
			print "The specified directory doesn't have any csv file."

	def makeSurePathExists(self,path):
	    try:
	        os.makedirs(path)
	    except OSError as exception:	
	    	if exception.errno != errno.EEXIST:
	            raise
