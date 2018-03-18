#coding:utf-8
def quicksort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x < pivot]
        more = [x for x in list[1:] if x >= pivot]
        return quicksort(less) + [pivot] + quicksort(more)

list1=[1,3,2,4,6,3,5,6,8,5]
print(quicksort(list1))