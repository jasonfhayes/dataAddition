FILE_PATH_1 = '/Users/jason/Desktop/test_data/data1.txt'
FILE_PATH_2 = '/Users/jason/Desktop/test_data/data2.txt'

file_handle = open(FILE_PATH_1, 'r')
data_1 = file_handle.read()
file_handle.close()

file_handle = open(FILE_PATH_2, 'r')
data_2 = file_handle.read()
file_handle.close()

print(f'Data total is: {int(data_1) + int(data_2)}')