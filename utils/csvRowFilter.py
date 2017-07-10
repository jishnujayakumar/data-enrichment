import os
import sys
import csv
import errno
import pandas as pd
import numpy as np

class csvRowFilter:

	def __init__(self,csvFilePath, inputColumnIds):

		#'../input/jishnu_module_test/merged-test-copy.csv'

		try:

			self.inputFile = open(csvFilePath)

		except TypeError,e:

			print e

		self.csvFile = csv.reader(self.inputFile)

		self.inputColumnIds = inputColumnIds

		self.ROWS=[]
		for row in csv.reader(self.inputFile):
			self.ROWS.append(row)

		#self.displayAllRows()
		self.inital_size = len(self.ROWS)
		print self.inital_size

	def startFiltering(self):
		check = self.columnExistsInCSVFile()
		if(check['status']):
			print check['message']
			print "Filtering process begins"
			columnIndices = check['columnIndices']
		else:
			print check['error_message']
			sys.exit()



		#pull out the key columns data

		keyData = self.getKeyColumnDataWithIndex(columnIndices)

		keysTraversed = []
		rowsToBeDeleted = [] #These would be removed
		rowsToBeAdded = [] #pd.concat (axis=0)this would be appended to the csvFile

		row_num = 0

		for key1 in keyData:

			print "Row number: " +  str(row_num)

			row_num = row_num + 1

			rowReplicateIndex=[]

			#print "key1" + str(key1) + " | " + "keyTRA" + str(keysTraversed)

			if key1 in keysTraversed:

			#	print "key1 in keysTRA" + str(key1 in keysTraversed)

				continue

			else:

				for index,key2 in enumerate(keyData):

					if key1==key2:

						rowReplicateIndex.append(index)

#						print "rowRep" + str(rowReplicateIndex)

			#	print "rowReplicateIndex"

			#	print len(rowReplicateIndex)


				if  len(rowReplicateIndex) > 1:

					#union of the replicate rows
					#Intersection in individual rows
					for j in rowReplicateIndex:
						rowsToBeDeleted.append(j)

					rowsToBeAdded.append(self.rowUnion(rowReplicateIndex))
					
			#		print 'rowsToBeAdded'
			#		print rowsToBeAdded
			#		print 'seq:rowsToBeDeleted'
			#		print rowsToBeDeleted
			#		print 'rowsToBeDeleted'
					
			#		for i in rowsToBeDeleted:

						#print i

			#			print self.ROWS[i]						
					
				keysTraversed.append(key1)

		print "Processing"

		count=0

		#print len(self.ROWS)

		#print 'seq:rowsToBeDeleted'
		#print rowsToBeDeleted

		for i in rowsToBeDeleted:
	
			#print "removing at:"

			#print self.ROWS[i-count]


			self.ROWS.remove(self.ROWS[i-count])

			count = count + 1

			#print len(self.ROWS)

		for i in range(0,len(rowsToBeAdded)):

			#print "Adding:"

			#print rowsToBeAdded[i]

			self.ROWS.append(rowsToBeAdded[i])	

		#Deleting the rowsToBeDeleted and adding rowsToBeadded

		#print self.ROWS[0]

		#self.displayAllRows()
		print len(self.ROWS)

	
		print "Filtering process ended."

		print "Intial number of rows: " + str(self.inital_size)

		print "Final number of rows: " + str(len(self.ROWS))

		print "Creating the output file"

		with open("../../output/filtered_output.csv", "wb") as f:
			writer = csv.writer(f)
			writer.writerows(self.ROWS)

		self.closeInputFile()

	def displayAllRows(self):

		for row in self.ROWS:

			print row

	def rowUnion(self, rowIndices):

		rows=[]

		for i,row in enumerate(self.ROWS):

			if(i in rowIndices):

				#print i

				rows.append(row)

		mergedRow=[]

		temp = []

		allColumns = self.getAllColumnIds()

		for column in range(0,len(allColumns)):

			LIST=[]

			for row in rows:

				if(row[column] != ""):

					LIST.append(row[column])

			temp.append(list(set().union(LIST)))	

		for item in temp:

			mergedRow.extend(item)

		return mergedRow

	def getKeyColumnDataWithIndex(self, columnIndices):
		rows=[]

		for row in self.ROWS:

			temp = []
			for columnIndex in columnIndices:
				temp.append(row[columnIndex])
			rows.append(temp)
		
		return rows


	def getAllColumnIds(self):
		
		rows = []

		for row in self.ROWS:
			rows=row
			#self.ROWS.remove(row)
			break

		return rows

	def columnExistsInCSVFile(self):
		count = 0
		columnIdsNotFound = []
		columnIndices = []

		headers = self.getAllColumnIds()

		for columnId in self.inputColumnIds:

			if(columnId in headers):
				count = count + 1
				columnIndices.append(headers.index(columnId))
			else:
				columnIdsNotFound.append(columnId)


		if(count == len(self.inputColumnIds)):
			return {
				'status':True,
				'message':"Success: All the inputed columns are present in csv File.",
				'columnIndices':columnIndices
			}

		else:
			return {
				'status':False,
				'error_message':"Warning: " + "Columns not found : " + str(columnIdsNotFound)
			}

	def closeInputFile(self):

		self.inputFile.close()



