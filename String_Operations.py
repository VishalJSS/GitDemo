#Slicing
p="This is to test 1342 $@#"
print(p[5:10])
print(p[11:])
print(p[:10])
print(p[-8:-1])

print(p.upper())    #Converts to uppercase
print(p.lower())    #Converts to lowercase
print(p.strip())    #Removes Whitespace in beginning and end of line
print(p.replace("T","A"))   #Replacing string
q=p.split(" ") #Creatng list with delimiter specified for separation
numbers=q[4]
special=q[5]
print("We have numbers {} and special characters {}".format(numbers, special))
print("It\'s all\n right\t   backspace\bfor \\me")

string="PYTHON"
for char in string:
    print(chr(ord(char)-1))
    print(ord(char))