#The code when the file does not exist
file1 =open('sample.txt', 'r')
readingfile= file1.read ()
print(readingfile)

#Correcting the error and completing the task
file1 =open('sample.txt', 'r')
readingline_1= file1.read (35)
readingline_2= file1.read (34)
print('Reading file contents:')
print( readingline_1)
print(readingline_2)
file1.close()

#Alternative method
try:
    file1 =open('sample.txt', 'r')
    print('Reading file contents:')
    for line in file1:
            print(line.strip())  # strip() removes extra newline characters
except FileNotFoundError:
    print("Error: 'sample.txt' does not exist. Please check the file name or create the file.")
