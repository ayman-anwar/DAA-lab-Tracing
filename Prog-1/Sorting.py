import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

def mergesort(array):
  if len(array)>1:
    r=len(array)//2
    L=array[:r]
    M=array[r:]

    mergesort(L)
    mergesort(M)

    i=j=k=0
    while i<len(L) and j<len(M):
      if L[i]<M[j]:
        array[k]=L[i]
        i+=1
      else :
        array[k]=M[j]
        j+=1
      k+=1

    while i<len(L):
      array[k]=L[i]
      i+=1
      k+=1

    while j<len(M):
      array[k]=M[j]
      j+=1
      k+=1

def selectionsort(array,size):
  for step in range(size):
    min_inx=step

    for i in range(step+1,size):
      if array[i]<array[min_inx]:
        min_inx=i

    (array[min_inx],array[step])=(array[step],array[min_inx])



def partition(array,low,high):
  pivot=array[high]

  i=low-1

  for j in range(low,high):
    if array[j]<=pivot:
      i+=1
      (array[i],array[j])=(array[j],array[i])

  (array[i+1],array[high])=(array[high],array[i+1])
  return i+1

def quicksort(array,low,high):
  if low < high :
    s=partition(array,low,high)

    quicksort(array,low,s-1)
    quicksort(array,s+1,high)

def readinput():
  a=[]
  n=int(input("Enter no. of TV channels:"))
  print("Enter the number of viewers:")
  for _ in range(0,n):
    l=int(input())
    a.append(l)

  return a


elements=list()
times=list()
global labeldata
print("1.Merge Sort   2.Quick Sort    3.Selection sort ")
ch=int(input("Enter your choice:"))

if ch==1:
  labeldata="Mergesort"
  array=readinput()
  mergesort(array)
  print("Sorted list is:")
  print(array)
elif ch==2:
  labeldata="Quicksort"
  array=readinput()
  h=len(array)-1
  quicksort(array,0,h)
  print("Sorted list is:")
  print(array)
else:
  labeldata="Selectionsort"
  array=readinput()
  h=len(array)
  selectionsort(array,h)
  print("Sorted list is:")
  print(array)


print("************Running Time Analysis************")
for i in range(1,10):
  array=randint(0,1000*i,1000*i)
  start=time.time()

  if ch==1:
    mergesort(array)

  elif ch==2:
    h=len(array)-1
    quicksort(array,0,h)

  else:
    h=len(array)
    selectionsort(array,h)

  end=time.time()

  print(len(array)," elements sorted by ",labeldata,end-start)
  elements.append(len(array))
  times.append(end-start)


plt.xlabel("List length")
plt.ylabel("Time Complexity")
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()
