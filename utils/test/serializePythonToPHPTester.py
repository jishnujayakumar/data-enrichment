import sys
sys.path.append('../')
from serializePythonToPHP import serializePythonToPHP

<<<<<<< HEAD
keyColumnIds = ['SCHOOL_CODE']
place='Daman_and_Diu'
serilizeP2PObj = serializePythonToPHP('../../input/institute_teachers/' + place +'/teachers/' + place + '.csv', place)
serilizeP2PObj.startSerializing('../../input/institute_teachers/' + place +  '/institutes/', "serialized_teachers.csv", keyColumnIds)
=======
serilizeP2PObj = serializePythonToPHP('../../input/test/input_for_python_to_php_serialize_module.csv')
serilizeP2PObj.startSerializing("../../output/", "serialized_.csv")
>>>>>>> c9b6e7e052bb267f193d4adb562920c8fc898397

