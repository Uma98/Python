input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
print(min(list))
print(set(list))
list.sort()
print(list)
list.sort(reverse = True)
print(list)