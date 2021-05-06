input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
#sum of all numbers
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
#minimum 
print(min(list))
#eliminating duplictes
print(set(list))
#sorting in ascending order
list.sort()
print(list)
#descending sort
list.sort(reverse = True)
print(list)
