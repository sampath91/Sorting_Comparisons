__author__ = 'Sampath'

import time
import random

def max_heapify(A, i, heap_size):
    l = 2*i
    r = l + 1
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest, heap_size)


def build_max_heap(A, heap_size):
    #heap_size = len(A[1:])
    for i in range(len(A[1:])/2-1, 0,-1):
        max_heapify(A,i, heap_size)

def heap_sort(A, heap_size):
    build_max_heap(A, heap_size)
    for i in range(len(A[1:]), 1,-1):
        A[1], A[i] = A[i], A[1]
        heap_size -= 1
        max_heapify(A,1, heap_size)
    return A

def heapsort_unsorted():

    j,s = 0,0
    count = [10,500,1000,2000,4000,8000,16000, 32000]
    for i in count:
        j += 1
        n = []
        result,s = 0,0
        if i == 10:
                print 'Three Sorting Iterations for Array of 10 numbers: '
        for k in range(1,4,1):
            s += 1
            A = random.sample(range(1,100000), i)
            A.insert(0,0)
            heap_size = len(A[1:])
            starttime = round(time.time() * 1000)
            A = heap_sort(A, heap_size)
            endtime = round(time.time() * 1000)
            A.remove(0)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'


def heapsort_sorted(r):

    j,s = 0,0
    #count = [10]
    count = [10,500,1000,2000,4000,8000,16000, 32000]
    for i in count:
        j += 1
        n = []
        result,s = 0,0
        if i == 10:
                print 'Three Sorting Iterations for Array of 10 numbers: '
        for k in range(1,4,1):
            s += 1
            A = random.sample(range(1,100000), i)
            if r == 'desc':
                A.sort(reverse=True)
            else:
                A.sort()
            A.insert(0,0)
            heap_size = len(A[1:])
            starttime = round(time.time() * 1000)
            A = heap_sort(A, heap_size)
            endtime = round(time.time() * 1000)
            A.remove(0)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'


def main():
    heapsort_unsorted()
    heapsort_sorted('desc')


if __name__ == "__main__":
  main()