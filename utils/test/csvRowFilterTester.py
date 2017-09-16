import sys
sys.path.append('../')
from csvRowFilter import csvRowFilter

keyColumnIds = ['Name', 'Pincode']
row_filter = csvRowFilter('../../input/references/merged.csv', keyColumnIds)
row_filter.startFiltering("../../output/test/csvRowFilter", "row_filtered_output-merged.csv")

#keyColumnIds = ['SCHOOL_CODE']
#row_filter = csvRowFilter("../../input/institute_teachers/Daman_and_Diu/institutes/raw_merged.csv", keyColumnIds)
#row_filter.startFiltering("../../output/", "Jishnu.csv")

