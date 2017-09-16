import sys
sys.path.append('../')
from mergeTwoFiles import merger

'''
stateCSVFileLocation="../../input/__Manipur.csv"
mergedCSVFileLocation="../../input/references/merged-filtered.csv"
key='h_place_id'
m=merger(stateCSVFileLocation, mergedCSVFileLocation)
m.startMerging(key)
'''
'''
stateCSVFileLocation="../../input/Main/__Daman_and_Diu.csv"
mergedCSVFileLocation="../../input/institute_teacher_data/__Daman_and_Diu.csv"
key='EduID'
m=merger(stateCSVFileLocation, mergedCSVFileLocation)
m.startMerging(key)
'''

stateCSVFileLocation="../../input/Main/__Daman_and_Diu.csv"
mergedCSVFileLocation="../../input/institute_teacher_data/__Daman_and_Diu.csv"
key='EduID'
m=merger(stateCSVFileLocation, mergedCSVFileLocation, key)
