import os
from csvRowFilter import csvRowFilter
from csvFileJoiner import csvFileJoiner

class merge():

	def __init__(self, inputPath, outputPath, outputFile, keyColumnIds):
		self.inputPath=inputPath
		self.outputPath=outputPath
		self.outputFile=outputFile 
		self.keyColumnIds=keyColumnIds
		
	def performFileJoining(self):
		joinerObj = csvFileJoiner(self.inputPath)
		joinerObj.joinAndGenerateCSVFiles(self.outputPath, self.outputFile)

	def performRowFilter(self):
		row_filter = csvRowFilter(str(os.path.abspath(os.path.join(self.outputPath, self.outputFile))), self.keyColumnIds)
		row_filter.startFiltering(self.outputPath, self.outputFile)

	def perform(self):
		self.performFileJoining()
		self.performRowFilter()
