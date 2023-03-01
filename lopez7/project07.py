import random
from timeit import default_timer
from bubbleSort import bubblesort
from mergeSort import *

list1 = []

def mixer(size):
    
    for i in range(size):
        list.append(random.randint(1,10000))
    return list

mixer(list1)
start = default_timer()
bubblesort(list1)
print(default_timer() - start)

start = default_timer()
print(list1)
print(default_timer() - start)


mixer(list1)
start = default_timer()
list1 = merge_sort(list1)
print(default_timer() - start)

start = default_timer()
print(list1)
print(default_timer() - start)