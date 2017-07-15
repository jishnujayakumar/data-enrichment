import sys
sys.path.append('../')
from serializePythonToPHP import serializePythonToPHP

keyColumnIds = ['SCHOOL_CODE']
serilizeP2PObj = serializePythonToPHP('../../input/institute_teachers/Daman_and_Diu/teachers/Daman_and_Diu.csv')
serilizeP2PObj.startSerializing("../../input/institute_teachers/Daman_and_Diu/institutes/", "serialized_teachers.csv", keyColumnIds)

