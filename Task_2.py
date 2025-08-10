# User input and write to the file
text =input('Enter text to write to the file: ')
data=open('output.txt', 'w')
write_data =data.write(text+ '\n')
print('Data Successfully written to output.text.')
# Additional input and append to the file
additionl_text= input('Enter additional text to append:')
data=open('output.txt', 'a')
data_append=data.write(additionl_text + 'n')
print('Data Successfully appended.')
# Read and display the final content
data=open('output.txt', 'r')
final_content = data.read()
print('Final content of output.text:',)
print(final_content)

