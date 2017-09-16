from __future__ import print_function
import os
import sys
import csv

class merger():

	def __init__(self, stateCSVFileLocation, mergedCSVFileLocation, key):

		self.stateCSVFileLocation = stateCSVFileLocation
		self.mergedCSVFileLocation = mergedCSVFileLocation
		self.mergedCSV = csv.reader(open(mergedCSVFileLocation))
		self.stateCSVFiles = []
		self.rowsMarked = []

		self.MERGED_ROWS=[]

		for row in self.mergedCSV:
			
			self.MERGED_ROWS.append(row)

		self.startMerging(key)

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

				print('Key:' + str(key) + " not found in state file")

			if(key not in mergedCSVColumnHeader):

				print('Key:' + str(key) + " not found in merged file")				

		return [nonRepeatingColumnHeaderIndex, nonRepeatingColumnHeaders, keyStateIndex, keyMergedIndex]

	def getRowDataof(self, row, columnHeaderIndices):

		columnData=[]

		for index in columnHeaderIndices: 

			columnData.append(row[index])

		return columnData

	def startMerging(self, key):

		print('Merging process starts')

		output=[]

		state=[]

		List=[]

		matched_state_row=[]

		for row in csv.reader(open(self.stateCSVFileLocation)):
		
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

			#print("Row:"+str(row_index)+"/"+str(len(state))+" | Merging file:" + str(self.stateCSVFileLocation) + " with " + str(self.mergedCSVFileLocation) + " based on (key) :" + str(key))

			print("Row:"+str(row_index)+"/"+str(len(state))+" | Merging file:" + str(os.path.basename(self.stateCSVFileLocation)) + " with " + str(os.path.basename(self.mergedCSVFileLocation)) + " based on (key) :" + str(key) + "", end='\r')

			List=[]

			for ROW_INDEX, ROW in enumerate(self.MERGED_ROWS):					

				if(row_index == 0 or ROW_INDEX in self.rowsMarked or ROW_INDEX == 0):

					continue

				if(row[usefulMergedCSVColumns[2]] == ROW[usefulMergedCSVColumns[3]] and len(ROW[usefulMergedCSVColumns[3]])!=0 and ROW[usefulMergedCSVColumns[3]]!='None'):

						self.rowsMarked.append(ROW_INDEX)

						#print self.rowsMarked

						matched_state_row.append(row_index)

						List=state[row_index] + self.getRowDataof(ROW, usefulMergedCSVColumns[0])

						output.append(List)

						break
		
		for index,row in enumerate(state):
			if index==0:
				continue
			#print(row)
			if index not in matched_state_row:
				output.append(row)
		#print output

		with open(self.stateCSVFileLocation, "wb") as f:
			writer = csv.writer(f)
			writer.writerows(output)

		print('Merging process ends')

if __name__ == '__main__':

	
	stateCSVFileLocation = '../input/' #Directory having place-id data
	mergedCSVFileLocation = '../output/test/csvRowFilter/row_filtered_updated_merged_output.csv' #This file has updated column headers based on sample.csv and it's duplicate row have been also remove based on ['Name', 'Pincode'] columns.
	m = merger(stateCSVFileLocation, mergedCSVFileLocation)
	m.startMerging('h_place_id')    #Merge based on h_place_id column, any one key (column name) can be given. E.g. Here h_place_id is given
	
	'''

	#Shashi-data of main diu(150 clmns) + diu array serialized teachers data
	stateCSVFileLocation = './input/states_data'
	mergedCSVFileLocation = '../../input/institute_teachers/Daman_and_Diu/serialized_teachers_updated.csv'
	m = merger(stateCSVFileLocation, mergedCSVFileLocation)
	m.startMerging('SCHOOL_CODE')
	'''
	
