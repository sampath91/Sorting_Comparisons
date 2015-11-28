__author__ = 'Sampath'

import random
import time
import sys
#sys.setrecursionlimit(100000)


def partition(A, start, end):
    x = A[end]
    i = start - 1
    for j in range(start, end, 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1



def quicksortendpivot(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksortendpivot(A, p, q-1)
        quicksortendpivot(A, q+1, r)
    return A



def quicksortstack(A, p, r):
    temp_stack = []
    temp_stack.append((p,r))

    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(A,left,right)
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        if piv+1 < right:
            temp_stack.append((piv+1,right))
    return A



def quicksort_unsorted():

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
            starttime = round((time.time() * 1000),2)
            start = 0
            end = len(A)-1
            A = quicksortendpivot(A,start,end)
            endtime = round((time.time() * 1000),2)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'



def quicksort_sorted(r):

    j,s = 0,0
    #count = [100]
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
            starttime = round((time.time() * 1000),2)
            start = 0
            end = len(A)-1
            A = quicksortstack(A,start,end)
            endtime = round((time.time() * 1000),2)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'


def main():
    quicksort_unsorted()
    print '------------------------------------------'
    #quicksort_sorted('asc')


if __name__ == "__main__":
  main()
