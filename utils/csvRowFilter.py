import os
import sys
import csv

class csvRowFilter:

	def __init__(self,csvFilePath, inputColumnIds):

		try:

			self.inputFile = open(csvFilePath)

		except TypeError,e:

			print e

		self.csvFile = csv.reader(self.inputFile)

		self.inputColumnIds = inputColumnIds

		self.ROWS=[]
		for row in csv.reader(self.inputFile):
			self.ROWS.append(row)

		self.inital_size = len(self.ROWS)
		print self.inital_size

	def startFiltering(self, path, fileName):
		check = self.columnExistsInCSVFile()
		if(check['status']):
			print check['message']
			print "Filtering process begins"
			columnIndices = check['columnIndices']
		else:
			print check['error_message']
			sys.exit()

		keyData = self.getKeyColumnDataWithIndex(columnIndices)

		keysTraversed = []
		rowsToBeDeleted = [] #These would be removed
		rowsToBeAdded = [] 

		row_num = 0

		for key1 in keyData:

			print "Scanning row number: " +  str(row_num) + " | Total number of rows before filtering:" + str(self.inital_size)

			row_num = row_num + 1

			rowReplicateIndex=[]

			if key1 in keysTraversed:

				continue

			else:

				for index,key2 in enumerate(keyData):

					if key1==key2:

						rowReplicateIndex.append(index)

				if  len(rowReplicateIndex) > 1:

					for j in rowReplicateIndex:
						rowsToBeDeleted.append(j)

					rowsToBeAdded.append(self.rowUnion(rowReplicateIndex))
					
				keysTraversed.append(key1)

		print "Processing"

		count=0

		print "Deleting duplicate row entries."

		rowsToBeDeleted.sort()

		for i in rowsToBeDeleted:

			print('deleting duplicate row#:' + str(i-count))

			#print self.ROWS[i-count]

			self.ROWS.remove(self.ROWS[i-count])

			count = count + 1

		rowsToBeAdded.sort()

		print "Adding merged row entries"

		for i in range(0,len(rowsToBeAdded)):

			print('adding combined row:' + str(i + 1) + ' out of ' + str(len(rowsToBeAdded)))

			#print self.ROWS[i]

			self.ROWS.append(rowsToBeAdded[i])	
	
		print "Filtering process ended."

		print "Intial number of rows: " + str(self.inital_size)

		print "Final number of rows: " + str(len(self.ROWS))

		with open(os.path.join(path, fileName), "wb") as f:
			writer = csv.writer(f)
			writer.writerows(self.ROWS)

		print "Output: " + str(os.path.abspath(os.path.join(path, fileName)))

		self.closeInputFile()

	def displayAllRows(self):

		for row in self.ROWS:

			print row

	def rowUnion(self, rowIndices):

		rows=[]

		for i,row in enumerate(self.ROWS):

			if(i in rowIndices):

				rows.append(row)

		mergedRow=[]

		temp = []

		allColumns = self.getAllColumnIds()

		for column in range(0,len(allColumns)):

			LIST=[]

			indexCounter = 0;

			for row in rows:

				LIST.append(row[column])

			temp.append(list(set().union(LIST)))	

		for item in temp:

			if(len(item) > 1 and "" in item):

				item.remove("")

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



