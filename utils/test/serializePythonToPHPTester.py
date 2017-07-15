import sys
sys.path.append('../')
from serializePythonToPHP import serializePythonToPHP

keyColumnIds = ['SCHOOL_CODE']
place='Daman_and_Diu'
serilizeP2PObj = serializePythonToPHP('../../input/institute_teachers/' + place +'/teachers/' + place + '.csv', place)
serilizeP2PObj.startSerializing('../../input/institute_teachers/' + place +  '/institutes/', "serialized_teachers.csv", keyColumnIds)

