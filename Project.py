__author__ = 'Sampath'

import quicksort_mot_insertion
import quicksort
import mergesort
import heapsort
import random
import time

def main():
    print '***Unsorted numbers Executions***'
    print 'Following are executions of \t1. Heap sort\t2. Merge sort\t3. Quick sort\t4. Quick sort with Median of three and insertion sort'
    print
    print '1. Heap Sort - \n'
    heapsort.heapsort_unsorted()
    print
    print
    print '2. Merge Sort - \n'
    mergesort.mergesort_unsorted()
    print
    print
    print '3. Quick Sort - \n'
    quicksort.quicksort_unsorted()
    print
    print
    print '4. Quick sort with Median of three and insertion sort - \n'
    quicksort_mot_insertion.quicksort_mot_ins_unsorted()
    print
    print '-----------------------------------------------------------'
    print '***Sorted numbers(Ascending order) Executions***'
    print 'Following are executions of \t1. Heap sort\t2. Merge sort\t3. Quick sort\t4. Quick sort with Median of three and insertion sort'
    print
    print '1. Heap Sort - \n'
    heapsort.heapsort_sorted('asc')
    print
    print
    print '2. Merge Sort - \n'
    mergesort.mergesort_sorted('asc')
    print
    print '3. Quick sort with Median of three and insertion sort - \n'
    quicksort_mot_insertion.quicksort_mot_ins_sorted('asc')
    print
    print
    print '4. Quick Sort - \n'
    quicksort.quicksort_sorted('asc')
    print
    print '-----------------------------------------------------------'
    print '***Sorted numbers(Descending order) Executions***'
    print 'Following are executions of \t1. Heap sort\t2. Merge sort\t3. Quick sort\t4. Quick sort with Median of three and insertion sort'
    print
    print '1. Heap Sort - \n'
    heapsort.heapsort_sorted('desc')
    print
    print
    print '2. Merge Sort - \n'
    mergesort.mergesort_sorted('desc')
    print
    print
    print '3. Quick sort with Median of three and insertion sort - \n'
    quicksort_mot_insertion.quicksort_mot_ins_sorted('desc')
    print
    print
    print '4. Quick Sort - \n'
    quicksort.quicksort_sorted('desc')
    print
    print 'Thank You!!!'


if __name__ == '__main__':
    main()



