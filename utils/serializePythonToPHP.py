import os
import sys
import csv
import errno
from csvRowFilter import csvRowFilter
from csvFileJoiner import csvFileJoiner
from phpserialize import serialize, unserialize #Python replacement for PHP's serialize | https://gist.githubusercontent.com/sj26/292552/raw/ce68608a590918438c365027ebb17a85d9a0af3e/phpserialize.py

class serializePythonToPHP:

	def __init__(self,csvFilePath):

		self.schoolCodeSet = set()

		self.temp_file_name = 'raw_merged.csv'

		try:

			self.inputFile = open(csvFilePath)

		except TypeError:

			print("Error: Entered file is not a csv file")

		self.csvFile = csv.reader(self.inputFile)

		self.ROWS=[]
		for row in csv.reader(self.inputFile):
			self.ROWS.append(row)

		self.inital_size = len(self.ROWS)
		
		self.columnIds=self.ROWS[0]

	def getUniquesSchoolCodes(self):

		for i,row in enumerate(self.ROWS):

			if i==0:

				continue

			self.schoolCodeSet.add(row[0])

	def startSerializing(self, path, fileName, keyColumnIds):

		self.makeSurePathExists(path)

		self.getUniquesSchoolCodes() # get unique schoolcodes

		outputColumnHeaders = [self.columnIds[0]]

		data = []

		final_output = []

		reference_counter=0

		for school_code in self.schoolCodeSet:

			details=[]

			details.append(school_code)

			match_counter = 0

			for row in self.ROWS:

				if(row[0]==school_code):

					match_counter = match_counter + 1

					_dict = {}

					for i,item in enumerate(row):

						_dict[self.columnIds[i]] = item

					serial_str = serialize(_dict)

					details.append(serial_str)

			data.append(details)
			
			reference_counter = max(reference_counter,match_counter)


		for index in range(0,reference_counter):

			outputColumnHeaders.append('teacher_' + str(index))

		final_output.append(outputColumnHeaders)

		for item in data:

			final_output.append(item)

		self.write_to_csv(path, fileName, final_output)

		joinerObj = csvFileJoiner(path)

		joinerObj.joinAndGenerateCSVFiles(path, self.temp_file_name)

		self.performRowFilter(path, self.temp_file_name, keyColumnIds)

	def performRowFilter(self, path, fileName, keyColumnIds):
		row_filter = csvRowFilter(str(os.path.abspath(os.path.join(path, self.temp_file_name))), keyColumnIds)
		row_filter.startFiltering(path, "row_filtered_merged_output.csv")

	def write_to_csv(self,path,fileName, data):
		with open(os.path.join(path, fileName), "w") as f:
			writer = csv.writer(f)
			writer.writerows(data)

		print("Output: " + str(os.path.abspath(os.path.join(path, fileName))))


	def makeSurePathExists(self,path):
	    try:
	        os.makedirs(path)
	    except OSError as exception:	
	    	if exception.errno != errno.EEXIST:
	            raise