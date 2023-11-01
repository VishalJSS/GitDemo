#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists

#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#Because "r" for read, and "t" for text are the default values, you do not need to specify them.

f = open("demofile.txt", "r")    #Displays all content
print(f.read())
f.close()

"""
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""
print("\n")

f = open("demofile.txt", "r")
print(f.readline())                #Reads First line  Hello! Welcome to demofile.txt
f.close()

f = open("demofile.txt", "r")
print(f.readlines())                #Returns as list  ['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']
f.close()

f = open("demofile.txt", "r")
print(f.read(10))                 #Reads first 10 index characters   Hello! Wel
f.close()

f = open("demofile.txt", "r")
for x in f:
  print(x)                    #Loops through each line to display  Hello! Welcome to demofile.txt   This file is for testing purposes.    Good Luck!
f.close()

f = open("demofile.txt", "r")
f.seek(12)                    #Setting index position
print(f.tell())               #Prints current position  12
print(f.readline())           #me to demofile.txt
f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

"""
See you soon!
Over and out.Now the file has more content!
"""

f = open("demofile2.txt", "w")
f.writelines(["See you soon!\n", "Over and out."])
f.close()


f = open("demofile2.txt", "r")
print(f.read())
"""
See you soon!
Over and out.
"""
print(f.seekable())       #True
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!\nWriting in new line")
print(f.readable())         #False
print(f.seekable())         #True
print(f.isatty())           #False
print(f.writable())         #True
f.close()

f = open("demofile3.txt", "r")
print(f.fileno())     #Returns a number that represents the stream, from the operating system's perspective  3
print(f.isatty())     #returns True if the file stream is interactive   #False
print(f.readable())   #Returns true if reable if not false    #True
print(f.read())
f.close()

"""
Woops! I have deleted the content!
Writing in new line
"""

#import os
#os.remove("demofile.txt")

#if os.path.exists("demofile.txt"):
#  os.remove("demofile.txt")
#else:
#  print("The file does not exist")

#os.rmdir("myfolder")
#os.rename('oldname', 'newname')
#shutil.copy('file_path', 'new_path')
#shutil.move('file_path', 'new_path')
#os.listdir('dir_path')

#r	It opens an existing file to read-only mode. The file pointer exists at the beginning.
#rb	It opens the file to read-only in binary format. The file pointer exists at the beginning.
#r+	It opens the file to read and write both. The file pointer exists at the beginning.
#rb+	It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.
#w	It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name.
#wb	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists.
#w+	It opens the file to write and read data. It will override existing data.
#wb+	It opens the file to write and read both in binary format
#a	It opens the file in the append mode. It will not override existing data. It creates a new file if no file exists with the same name.
#ab	It opens the file in the append mode in binary format.
#a+	It opens a file to append and read both.
#ab+	It opens a file to append and read both in binary format.