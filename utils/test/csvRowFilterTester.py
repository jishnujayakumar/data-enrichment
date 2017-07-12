import sys
<<<<<<< HEAD
import csv
sys.path.append('../')
from csvRowFilter import csvRowFilter
=======
sys.path.append('../')
from utils import csvRowFilter
>>>>>>> c79ffbbfc7c787be306e086f3c164dc776787664

keyColumnIds = ['NAME', 'PINCODE']
row_filter = csvRowFilter('../../input/test/merged-test-copy.csv', keyColumnIds)
row_filter.startFiltering()

