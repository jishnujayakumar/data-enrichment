import sys
sys.path.append('../')
from serializePythonToPHP import serializePythonToPHP

serilizeP2PObj = serializePythonToPHP('../../input/test/input_for_python_to_php_serialize_module.csv')
serilizeP2PObj.startSerializing("../../output/", "serialized_.csv")

