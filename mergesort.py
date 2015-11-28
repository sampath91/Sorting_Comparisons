__author__ = 'Sampath'

import time
import random


def merge(left, right):
    A = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A.append(left[i])
            i += 1
        else:
            A.append(right[j])
            j += 1
    A += left[i:]
    A += right[j:]
    return A


def merge_sort(A):
    if len(A) > 1:
        q = len(A) // 2
        left = merge_sort(A[:q])
        right = merge_sort(A[q:])
        return merge(left, right)
    return A

def mergesort_unsorted():
    j,s = 0,0
    count = [10,500,1000,2000,4000,8000,16000, 32000]
    for i in count:
        j += 1
        n=[]
        result,s = 0,0
        if i == 10:
                print 'Three Sorting Iterations for Array of 10 numbers: '
        for k in range(1,4,1):
            s += 1
            A = random.sample(range(1,100000), i)
            #print 'Unsorted list = ',A
            starttime = round(time.time() * 1000)
            A = merge_sort(A)
            endtime = round(time.time() * 1000)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'

def mergesort_sorted(r):
    j,s = 0,0
    count = [10,500,1000,2000,4000,8000,16000, 32000]
    for i in count:
        j += 1
        n=[]
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
            #print 'Unsorted list = ',A
            starttime = round(time.time() * 1000)
            A = merge_sort(A)
            endtime = round(time.time() * 1000)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'



def main():
    mergesort_unsorted()
    mergesort_sorted('desc')


if __name__ == "__main__":
    main()
