import sys
sys.path.append('../')
from utils import csvRowFilter

keyColumnIds = ['NAME', 'PINCODE']
row_filter = csvRowFilter('../../input/test/merged-test-copy.csv', keyColumnIds)
row_filter.startFiltering()

