# coding:utf-8
def bubblesort(new_list):
    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list

def bubblesort2(list2):
    for i in range(len(list2)-1):
        for j in range(i):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
    return list2

a = [1, 3, 6, 2, 3, 5, 1, 6, 3]
print(bubblesort(a))
print(bubblesort2(a))