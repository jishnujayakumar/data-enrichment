from csvFileJoiner import csvFileJoiner
import pandas as pd
joinerObj = csvFileJoiner("../input")
joinerObj.joinAndGenerateCSVFiles("../output/joinedCSV","joined.csv")
