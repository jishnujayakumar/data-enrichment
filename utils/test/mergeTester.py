import sys
sys.path.append('../')
from mergeFile import merge

inputPath="../../input/test/final_merge"
outputPath="../../output/"
outputFile="mergeTesterOutput.csv"
keyColumnIds=['EDUID', 'PLACE_ID', 'PINCODE']

m = merge(inputPath, outputPath, outputFile, keyColumnIds)
m.perform()