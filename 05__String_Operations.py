#Slicing
p="This is to test 1342 $@#"
print(p[5:10])          #is to
print(p[11:])           #test 1342 $@#
print(p[:10])           #This is to
print(p[-8:-1])         #1342 $@

print(p.upper())    #Converts to uppercase    THIS IS TO TEST 1342 $@#
print(p.lower())    #Converts to lowercase      this is to test 1342 $@#
print(p.strip())    #Removes Whitespace in beginning and end of line        This is to test 1342 $@#
print(p.replace("T","A"))   #Replacing string       #Ahis is to test 1342 $@#
q=p.split(" ") #Creatng list with delimiter specified for separation
numbers=q[4]
special=q[5]
print("We have numbers {} and special characters {}".format(numbers, special))   #We have numbers 1342 and special characters $@#
print("It\'s all\n right\t   backspace\bfor \\me")

"""
It's all
 right	   backspacfor \me
"""

string="PYTHON"
for char in string:
    print(chr(ord(char)-1))
    print(ord(char))

"""
O
80
X
89
S
84
G
72
N
79
M
78
"""