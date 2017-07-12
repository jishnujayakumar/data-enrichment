import sys
import pandas as pd
sys.path.append('../')
from csvFileJoiner import csvFileJoiner

joinerObj = csvFileJoiner("../../input/test/in")
joinerObj.joinAndGenerateCSVFiles("../../output/", "main_column_joined_output.csv")
