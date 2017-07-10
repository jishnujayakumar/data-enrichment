from csvFileJoiner import csvFileJoiner
import pandas as pd
joinerObj = csvFileJoiner("../input/jishnu_test/")
joinerObj.joinAndGenerateCSVFiles("../output/joinedCSV","joined1.csv")
