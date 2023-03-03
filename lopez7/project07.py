import random
from timeit import default_timer
from bubbleSort import bubblesort
from mergeSort import *
from insertionSort import *


def mixer(size):
    '''Summary of mixer() function
    This function takes a in and returns a mi
    '''
    list = []
    for i in range(size):
        list.append(random.randint(1,size))
    return list

list5k = mixer(5000)
list10k = mixer(10000)
list50k = mixer(50000)
list100k = mixer(100000)

# list10k = mixer(10000)

list1 = list5k
list2 = list5k
list3 = list5k

list4 = list10k
list5 = list10k
list6 = list10k

list7 = list50k
list8 = list50k
list9 = list50k

list10 = list100k
list11 = list100k

start = default_timer()
bubblesort(list1)
print(f"Bubble sort on 5k item list time:  {default_timer() - start} secs")
bubblesort(list4)
print(f"Bubble sort on 10k item list time:  {default_timer() - start} secs")
bubblesort(list7)
print(f"Bubble sort on 50k item list time:  {default_timer() - start} secs")

print('--------------------------------------------------------------------')

start = default_timer()
merge_sort(list2)
print(f"Merge sort on 5k item list speed:  {default_timer() - start} secs")
merge_sort(list5)
print(f"Merge sort on 10k item list speed:  {default_timer() - start} secs")
merge_sort(list8)
print(f"Merge sort on 50k item list time:  {default_timer() - start} secs")
merge_sort(list10)
print(f"Merge sort on 100k item list time:  {default_timer() - start} secs")

print('--------------------------------------------------------------------')

start = default_timer()
insertion_sort(list3)
print(f"Insertion sort on 5k item list speed:  {default_timer() - start} secs")
insertion_sort(list6)
print(f"Insertion sort on 10k item list speed:  {default_timer() - start} secs")
insertion_sort(list9)
print(f"Insertion sort on 50k item list time:  {default_timer() - start} secs")
insertion_sort(list11)
print(f"Insertion sort on 100k item list time:  {default_timer() - start} secs")