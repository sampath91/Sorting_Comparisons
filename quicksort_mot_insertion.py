__author__ = 'Sampath'

import random
import time

def insertionsort( A ,p,r):
  for i in range( p+1, r+1,1 ):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp
  return A

def medianofthree(A,left,right):
    center = (left + right)/2
    if A[center] < A[left]:
        #print 'center < left: ',A
        A[center],A[left] = A[left],A[center]
        #print 'center < left: ',A
    if A[right] < A[left]:
        #print 'right < left: ',A
        A[left], A[right] = A[right],A[left]
        #print 'right < left: ',A
    if A[right] < A[center]:
        #print 'right < center: ',A
        A[center],A[right] = A[right], A[center]
        #print 'right < center: ',A

    A[center], A[right-1] = A[right-1], A[center]
    return right-1

def partition(A, start, end):
    #print 'Before median of three: ',A
    x = medianofthree(A,start,end)
    #print 'After median of three: ',A
    i = start - 1
    for j in range(start, end-1, 1):
        if A[j] <= A[x]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end-1] = A[end-1], A[i+1]
    #print 'After sorting left:',A
    return i+1


def quicksort(A, p, r):
    #print r-p
    if p < r:
        if p + 15 <= r:
            q = partition(A, p, r)
            #print 'pivot: ',q
            quicksort(A, p, q-1)
            #print 'After left sort',A
            quicksort(A, q+1, r)
            #print 'After right sort',A
        else:
            #print 'insertion sort of:',A,p,r
            insertionsort(A,p,r)


def quicksort_mot_ins_unsorted():

    j,s = 0,0
    #count=[30]
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
            #print 'Unsorted list = ',A
            starttime = round(time.time() * 1000)
            start = 0
            end = len(A)-1
            quicksort(A,start,end)
            endtime = round(time.time() * 1000)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'


def quicksort_mot_ins_sorted(r):

    j,s = 0,0
    #count=[30]
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
            #print 'Unsorted list = ',A
            starttime = round(time.time() * 1000)
            start = 0
            end = len(A)-1
            quicksort(A,start,end)
            endtime = round(time.time() * 1000)
            t = endtime - starttime
            result += t
            n.append(t)
            if i == 10:
                print 'Iteration ',s,'Sorted list = ',A
            #print 'Input: ',j,'\tIteration: ',s,'\tsize: ',i,'\tStart Time (in ms): ',starttime,'\tEnd Time (in ms): ',endtime,'\tExecution Time',': ',(endtime - starttime),'ms'
        print 'Input: ',j,'\tsize: ',i,'\t3 iterations time - ',n,'\tAverage Execution Time',': ',round((result/k),2),'ms'


def main():
    quicksort_mot_ins_unsorted()
    quicksort_mot_ins_sorted('desc')

if __name__ == "__main__":
  main()
