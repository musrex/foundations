import random
from timeit import default_timer
from bubbleSort import bubblesort
from mergeSort import *
from insertionSort import *


def mixer(size):
    list = []
    for i in range(size):
        list.append(random.randint(1,size))
    return list

list10k = mixer(10000)
list50k = mixer(50000)
list100k = mixer(100000)
# list10k = mixer(10000)

list1 = list10k
list2 = list10k
list3 = list10k

list4 = list50k
list5 = list50k
list6 = list50k

list7 = list100k
list8 = list100k
list9 = list100k

start = default_timer()
bubblesort(list1)
print(f"Bubble sort on 10k item list time:  {default_timer() - start} secs")
bubblesort(list4)
print(f"Bubble sort on 50k item list time:  {default_timer() - start} secs")

start = default_timer()
merge_sort(list2)
print(f"Merge sort on 10k item list speed:  {default_timer() - start} secs")
merge_sort(list5)
print(f"Merge sort on 50k item list speed:  {default_timer() - start} secs")

start = default_timer()
insertion_sort(list3)
print(f"Insertion sort on 10k item list speed:  {default_timer() - start} secs")
insertion_sort(list6)
print(f"Insertion sort on 50k item list speed:  {default_timer() - start} secs")
