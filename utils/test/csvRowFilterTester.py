import sys
sys.path.append('../')
from csvRowFilter import csvRowFilter

keyColumnIds = ['NAME', 'PINCODE']
row_filter = csvRowFilter('../../input/test/merged-test-copy.csv', keyColumnIds)
row_filter.startFiltering("../../output/", "row_filtered_output.csv")

