#create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

#check if a file exist
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#create a new if it doesn't exist
my_file = open("my_file.txt", 'w')
my_file.write("Hi! I am William & I'm 9 yrs old.")
my_file.close()

#delete file named codingal
os.remove('Codingal.txt')

#delete folder
os.rmdir('Folder')