import csv

FILE_NAME = "test.csv"

header_list = ['a', 'b', 'c', 'd']
list = [[1,2,3,4],
       [ 5,6,7,8]]

with open(FILE_NAME, 'w', newline = '') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header_list)
    writer.writerows(list)