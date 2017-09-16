import sys
sys.path.append('../')
from serializePythonToPHP import serializePythonToPHP

keyColumnIds = ['EduID']

serilizeP2PObj = serializePythonToPHP('../../input/institute_teacher_data/__Daman_and_Diu.csv', keyColumnIds)
#serilizeP2PObj.startSerializing( keyColumnIds)
