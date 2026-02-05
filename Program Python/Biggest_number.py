lst=[4,7,1,8,13,25,10]

#Method 1
largest_num = max(lst)
print("Largest number is ", largest_num)

#Method 2
largest_number = lst[0]
for num in lst:
    if num > largest_number:
        largest_number = num
    
print("Traditional Largest number is ", largest_number)

#Method 3:
lst.sort()
large_number = lst[-1]
print("Sorted largest number is ", large_number)