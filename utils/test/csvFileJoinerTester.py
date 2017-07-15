import sys
import pandas as pd
sys.path.append('../')
from csvFileJoiner import csvFileJoiner

joinerObj = csvFileJoiner("../../input/test/csvFileJoiner")
joinerObj.joinAndGenerateCSVFiles("../../output/test/csvFileJoiner", "main_column_joined_output.csv")



