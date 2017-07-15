import sys
import pandas as pd
sys.path.append('../')
from csvFileJoiner import csvFileJoiner
<<<<<<< HEAD
<<<<<<< HEAD

joinerObj = csvFileJoiner("../../input/test/csvFileJoiner")
joinerObj.joinAndGenerateCSVFiles("../../output/test/csvFileJoiner", "main_column_joined_output.csv")



=======

joinerObj = csvFileJoiner("../../input/test/in")
joinerObj.joinAndGenerateCSVFiles("../../output/", "main_column_joined_output.csv")
>>>>>>> c9b6e7e052bb267f193d4adb562920c8fc898397
=======

joinerObj = csvFileJoiner("../../input/test/in")
joinerObj.joinAndGenerateCSVFiles("../../output/", "main_column_joined_output.csv")
>>>>>>> c9b6e7e052bb267f193d4adb562920c8fc898397
