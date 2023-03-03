import random
from timeit import default_timer
from bubbleSort import bubblesort
from mergeSort import *
from insertionSort import *


def mixer(size):
    '''Summary of mixer() function
    This function takes an int as an argument
    and returns a randomized list the size of the argument.

    size(INT): An int that determines the size of the list.

    returns: A randomized list the size of the int passed as 
    an argument.
    '''
    list = []
    for i in range(size):
        list.append(random.randint(1,size))
    return list

# here we create our various main 
# list sizes. we do this so all 
# lists of the same size start 
# with identical values. 
list5k = mixer(5000)
list10k = mixer(10000)
list50k = mixer(50000)
list100k = mixer(100000)

# here I create our copy lists 
# to run our experiments
# note - I don't go above 50k
# for bubblesort() because it
# took too long...
# ----------------------
# 5k lists
list1 = list5k
list2 = list5k
# 10k lists
list3 = list10k
list4 = list10k
# 50k lists
list5 = list50k
list6 = list50k
# 100k lists
list7 = list100k


# the start of our experiment
# we declare out start time variable...
start = default_timer()
bubblesort(list1)
# and then call a new timer method, and subtract the start time to 
# get the time it took for the sorting to finish. we can print this
# elegantly using f strings.
print(f"Bubble sort on 5k item list time:  {default_timer() - start} secs")
bubblesort(list3)
print(f"Bubble sort on 10k item list time:  {default_timer() - start} secs")
bubblesort(list5)
print(f"Bubble sort on 50k item list time:  {default_timer() - start} secs")

print('--------------------------------------------------------------------')

start = default_timer()
merge_sort(list2)
print(f"Merge sort on 5k item list speed:  {default_timer() - start} secs")
merge_sort(list4)
print(f"Merge sort on 10k item list speed:  {default_timer() - start} secs")
merge_sort(list6)
print(f"Merge sort on 50k item list time:  {default_timer() - start} secs")
merge_sort(list7)
print(f"Merge sort on 100k item list time:  {default_timer() - start} secs")
