a = 200
b = 33
c = 500
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#AND, OR and NOT
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not b > a:
  print("b is NOT greater than a")

if a > b:
    pass

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

for x in range(6):
  print(x)
print("\n")
for x in range(2, 6):
  print(x)
print("\n")
for x in range(2, 30, 3):
  print(x)