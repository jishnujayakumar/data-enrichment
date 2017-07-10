import sys
import csv
sys.path.append('../')
from csvRowFilter import csvRowFilter

keyColumnIds = ['NAME', 'PINCODE']
#row_filter = csvRowFilter('../../input/jishnu_module_test/merged-self-made-test-copy.csv', keyColumnIds)
row_filter = csvRowFilter('../../input/test/merged-test-copy.csv', keyColumnIds)
#row_filter = csvRowFilter('../../input/jishnu_module_test/merged.csv', keyColumnIds)
row_filter.startFiltering()

