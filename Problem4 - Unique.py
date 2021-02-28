# Nousheen Siddiqui
# Edited on 02/25/2021
# An append function that takes a list of numbers and returns a new list with unique elements of the first list[1, 3, 3, 3, 6, 2, 3, 5].

def unique_list(a):
    empty_list=[]
    for i in a:
        if i not in empty_list:
            empty_list.append(i)
    return empty_list
print(unique_list([1,3,3,3,6,2,3,5]))

