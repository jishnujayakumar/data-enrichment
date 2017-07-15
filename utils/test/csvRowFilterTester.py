import sys
sys.path.append('../')
from csvRowFilter import csvRowFilter

keyColumnIds = ['NAME', 'PINCODE']
<<<<<<< HEAD
row_filter = csvRowFilter('../../input/test/csvRowFilter/merged-test-copy.csv', keyColumnIds)
row_filter.startFiltering("../../output/test/csvRowFilter", "row_filtered_output.csv")

keyColumnIds = ['SCHOOL_CODE']
row_filter = csvRowFilter("../../input/institute_teachers/Daman_and_Diu/institutes/raw_merged.csv", keyColumnIds)
row_filter.startFiltering("../../output/", "Jishnu.csv")
=======
row_filter = csvRowFilter('../../input/test/merged-test-copy.csv', keyColumnIds)
row_filter.startFiltering("../../output/", "row_filtered_output.csv")
>>>>>>> c9b6e7e052bb267f193d4adb562920c8fc898397

