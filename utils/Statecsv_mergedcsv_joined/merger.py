import os
import sys
import csv

class merger():

	def __init__(self, stateCSVDirectory, mergedCSVFileLocation):

		self.stateCSVDirectory = stateCSVDirectory
		self.mergedCSV = csv.reader(open(mergedCSVFileLocation))
		self.stateCSVFiles = []
		self.rowsMarked = []

		self.MERGED_ROWS=[]

		for row in self.mergedCSV:
			
			self.MERGED_ROWS.append(row)

		
	def getAllStateCSVFiles(self):

		for file in os.listdir(self.stateCSVDirectory):
		    if file.endswith(".csv"):	
		    	self.stateCSVFiles.append(os.path.join(self.stateCSVDirectory, file))	
		if len(self.stateCSVFiles) == 0:	
			print('Warning!!! : State directory empty')

	def filterColumnHeaders(self, stateCSVColumnHeader, mergedCSVColumnHeader, key):

		keyStateIndex = 0

		keyMergedIndex = 0

		nonRepeatingColumnHeaders = []

		nonRepeatingColumnHeaderIndex = []

		for i,mergedCSVColumn in enumerate(mergedCSVColumnHeader):

			if(mergedCSVColumn not in stateCSVColumnHeader):

				#print("i:"+str(i)+" | " + str(mergedCSVColumn))

				if mergedCSVColumn != "":

					nonRepeatingColumnHeaders.append(mergedCSVColumn)

		for column in nonRepeatingColumnHeaders:

				nonRepeatingColumnHeaderIndex.append(mergedCSVColumnHeader.index(column))

		if(key in stateCSVColumnHeader and key in stateCSVColumnHeader):

			keyMergedIndex = mergedCSVColumnHeader.index(key)

			keyStateIndex = stateCSVColumnHeader.index(key)

		else:

			if(key not in stateCSVColumnHeader):

				print('Key:' + key + " not found in state file")

			if(key not in mergedCSVColumnHeader):

				print('Key:' + key + " not found in merged file")				

		return [nonRepeatingColumnHeaderIndex, nonRepeatingColumnHeaders, keyStateIndex, keyMergedIndex]

	def getRowDataof(self, row, columnHeaderIndices):

		columnData=[]

		for index in columnHeaderIndices: 

			columnData.append(row[index])

		return columnData

	def startMerging(self, key):

		print('Merging process starts')

		self.getAllStateCSVFiles()

		for file_number, file in enumerate(self.stateCSVFiles):

			print("Merging File:" + str(file_number + 1) + " out of " + str(len(self.stateCSVFiles)) + " with merged.csv" + " | Current file:" + str(file))

			output=[]

			state=[]

			List=[]

			for row in csv.reader(open(file)):
			
				state.append(row)

			usefulMergedCSVColumns = self.filterColumnHeaders(state[0], self.MERGED_ROWS[0], key)

			'''
			print usefulMergedCSVColumns[0]
			print usefulMergedCSVColumns[1]
			print usefulMergedCSVColumns[2]
			print usefulMergedCSVColumns[3]
			'''

			List=state[0] + usefulMergedCSVColumns[1]
		
			output.append(List)

			for row_index,row in enumerate(state):

				#print("Row_index:" + str(row_index) + " | row:" + str(row))

				List=[]

				for ROW_INDEX, ROW in enumerate(self.MERGED_ROWS):					

					if(row_index == 0 or ROW_INDEX in self.rowsMarked or ROW_INDEX == 0):

						continue

					if(row[usefulMergedCSVColumns[2]] == ROW[usefulMergedCSVColumns[3]] and ROW[usefulMergedCSVColumns[3]]!='' and ROW[usefulMergedCSVColumns[3]]!='None'):

							self.rowsMarked.append(ROW_INDEX)

							List=state[row_index] + self.getRowDataof(ROW, usefulMergedCSVColumns[0])

							output.append(List)

							break

			#print output

			with open(file, "wb") as f:
				writer = csv.writer(f)
				writer.writerows(output)

			print('Merging process ends')

if __name__ == '__main__':

	
	stateCSVDirectory = './input/states_data'
	mergedCSVFileLocation = './input/merged.csv'
	m = merger(stateCSVDirectory, mergedCSVFileLocation)
	m.startMerging('PLACE_ID')    #Merge based on PLACE_ID column, only one key should be given. E.g. Here PLACE_ID is given
	
	'''

	#Shashi-data of main diu(150 clmns) + diu array serialized teachers data
	stateCSVDirectory = './input/states_data'
	mergedCSVFileLocation = '../../input/institute_teachers/Daman_and_Diu/serialized_teachers_updated.csv'
	m = merger(stateCSVDirectory, mergedCSVFileLocation)
	m.startMerging('SCHOOL_CODE')
	'''
	