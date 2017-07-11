import sys
import pandas as pd
sys.path.append('../')
from csvFileJoiner import csvFileJoiner

joinerObj = csvFileJoiner("../../input")
joinerObj.joinAndGenerateCSVFiles("../output/joinedCSV","joined1.csv")
