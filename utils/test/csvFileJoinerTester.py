import sys
sys.path.append('../')
from utils import csvFileJoiner

joinerObj = csvFileJoiner("../../input")
joinerObj.joinAndGenerateCSVFiles("../output/joinedCSV","joined1.csv")
