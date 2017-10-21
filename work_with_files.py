import os

#os.makedirs('D:\\python\\create.txt
'''
file1 = open('D:\\python\\file.txt','r')
file1.write('Hello, world+')
file1.write('Hello, world++')
file1.write('Hello, world+++')
print(file1.readlines())'''
#print(file1.read())

input_file = open('D:\\python\\file.txt')

for l in input_file:
    print(l.rstrip() +'!')