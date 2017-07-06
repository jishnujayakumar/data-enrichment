from csvFileJoiner import csvFileJoiner
import pandas as pd
joinerObj = csvFileJoiner("../input")
#joinerObj.joinAndGenerateCSVFiles("/home/jishnu/Documents/github/data-enrichment/output/joinedCSV","joined.csv")
joinerObj.joinCSVFiles()
joinerObj.generateJoinedCSVFile("/home/jishnu/Documents/github/data-enrichment/output/joinedCSV","joined.csv")