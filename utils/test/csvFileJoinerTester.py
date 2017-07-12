import sys
<<<<<<< HEAD
import pandas as pd
sys.path.append('../')
from csvFileJoiner import csvFileJoiner
=======
sys.path.append('../')
from utils import csvFileJoiner
>>>>>>> c79ffbbfc7c787be306e086f3c164dc776787664

joinerObj = csvFileJoiner("../../input")
joinerObj.joinAndGenerateCSVFiles("../output/joinedCSV","joined1.csv")
