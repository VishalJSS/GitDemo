def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)
        # throws NameError if a >= 4
    print("Value of b = ", b)
try:
    fun(3)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
try:
    fun(5)
except NameError:
    print("NameError Occurred and Handled")

a=5
b='Ticket'
d={
    "name" : "Vishal",
    "age"  : 29
}

try:
    c=a+b
    print(c)

except TypeError:
    print("Type error occurred at c as one is int and other is string")

try:
    print(b[6])

except IndexError:
    print("b element doesn't has index with 6 - IndexError")

try:
    print(d["gender"])

except KeyError:
    print("dictionary doesn't have key gender - KeyError")

try:
    print(e)
except NameError:
    print("No variable with e is found - Name Error")

try:
    prin(a)
except NameError:
    print("Key word used is not correct - Name Error")
    #raise NameError ("Occured while printing a")

#try:
#    print(a
#except SyntaxError:
#    print(") is not used to close so Syntax Error Occurred")

try:
    f=int(b)
    print(f)
except ValueError:
    print("Issue while converting string to number - Value Error")

try:
    g=sqrt(16)
except ImportError:
    print("math is not imported - Import Error")