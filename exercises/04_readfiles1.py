#! /usr/bin/python3
# pw.py - 
## This is chapter 8 of the boring stuff with python book.
print('-----------------------print the directories-------------------------------')
import os
current_dir = os.path.abspath('.')
current_working_dir = os.getcwd()
print(current_dir)
print(current_working_dir)
print('-----------------------using open() to read from text file-------------------------------')
file_to_read = open('./test_dir/file_to_read.txt') # open the file in read mode (default)
content = file_to_read.read()
content_lines = file_to_read.readlines()
print(content)
print('-----------read() will empty the file object----------------------')
print(content_lines)
file_to_read = open('./test_dir/file_to_read.txt')
print(file_to_read.readlines())
print('-----------------------Using open() to write to file-----------------------------------------')
# open file in write mode or append mode (write will overwrite existing content)
file_to_write = open('./test_dir/write_file.txt', 'w') # notice the second arg: 'w'
file_to_write.write('Hello from the write method \nThis is the second line\n') 
file_to_write.close()
print('-----------------Now append-------------------------')
file_to_write = open('./test_dir/write_file.txt', 'a') # notice the second arg: 'w'
file_to_write.write('Hello from the append method \nThis is the second line\n') 
file_to_write.close()
print('----------------file size - folder content-------------------------------------')
file_size = os.path.getsize('/home/thomas/documents/sem4/python/get_things_done_with_python/tha_lecture/exercises/test_dir/file_to_read.txt')
print('file size: ',file_size)
dir = '/home/thomas/documents/sem4/python/get_things_done_with_python/tha_lecture/exercises/test_dir/'
folder_content = os.listdir('/home/thomas/documents/sem4/python/get_things_done_with_python/tha_lecture/exercises/test_dir')
print('folder content: ',folder_content)
print('folder size', sum([os.path.getsize(dir+f) for f in folder_content])) # list comprehension to get all files and transform them to list of integer and then use the sum function.
print('----------------Using shelve module to store variables to hard drive while running --------')
import shelve
shelve_file = shelve.open('./test_dir/shelve_file')
cats = ['Zophie', 'Pooka', 'Simon']
shelve_file['cats'] = cats
shelve_file.close()
print('-----------------Using shelve module to read variables from hard disk----------------------')
shelve_content = shelve.open('./test_dir/shelve_file') # shelve can be used as a session with keys and values.
print(shelve_content['cats'])
print('-----------------Using pprint module to store list of dictionaries to file-----------------')
# alternative to using shelve is to just store the data in a python file and import as module:
# pros: file can be read by humans - cons: many datatypes cannot be converted to text e.g: File, image etc.
import pprint
cats = [{'name':'sophie','age':3},{'name':'hanibal','age':1},{'name':'dorith','age':11}]
print(cats)
print(pprint.pformat(cats))
data_file = open('data_file.py','w')
data_file.write('cats='+pprint.pformat(cats))
data_file.close()
print('-----------------Using text file as module to import data----------------------------------')
import data_file
print(data_file.cats)
print('name of the first cat: ',data_file.cats[0]['name'])




