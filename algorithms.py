from random import randint
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
from merge_sort import merge_sort

L = [randint(1,1000) for i in range(100)]

#This is for testing the algorithms
print("Unsorted List:", L, "\n")

print("\nInsertion Sort:", insertion_sort(L[:]))

print("\nHeap Sort:", heap_sort(L[:]))

print("\nQuick Sort:", quick_sort(L[:]))

print("\nMerge Sort:", merge_sort(L[:]))