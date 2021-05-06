list1 = input("Enter some numbers: ").split()
list2 = input("Enter some numbers: ").split()

def get_numbers():
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)
    intersection_as_list = list(intersection)
    print(intersection_as_list)

get_numbers()