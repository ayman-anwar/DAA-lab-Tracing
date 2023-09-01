<h2><b>Program -1</b></h2>
<h3>Packages used:</h3>

    import time
    from numpy.random import seed
    from numpy.random import randint
    import matplotlib.pyplot as plt

<h3>Functions:</h3>
i) def mergesort(array)
<br>ii) def selectionsort(array,size)
<br>iii) def partition(array,low,high)
<br>iv) def quicksort(array,low,high)
<br>v) def readinput()

<h4>def mergesort(array):</h4>

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

* Works exactly as mergesort algorithm (notes)


* Entry condition for mergesort- if array size is greater than 1 then split the array

      if len(array)>1:
  
* Find the middle index of the array .<br> Since index is an integer(0,1..) we use '//' instead of '/' .<br> '/' gives floating point value and hence will throw an error.<br>L=array[:r] is moving the first half of the array to L similarly move the second half to M

      r=len(array)//2
      L=array[:r]
      M=array[r:]
* Apply mergesort to the new two splitted arrays.

      mergesort(L)
      mergesort(M)
  
* This completes the splitting of arrays part, next merge two sorted arrays.
* i is used for array L (first half) , j is used for array M (second half) , k is used for array (original array-solution)
  
      i=j=k=0
* This while loop is to compare the elements from first array (L) and second array (M).<br> Initially it compares the first element of array L with first element of array M (refer notes) .<br> If element of L is smaller add that to our solution array (array[k]) , increment the i pointer(next element of L array) or if element of M is smaller add M[j] and increment j.<br> Increment k (after if and else condition), since either of the one will be added and k should point to the next index.

      while i<len(L) and j<len(M):
          if L[i]<M[j]:
            array[k]=L[i]
            i+=1
          else :
            array[k]=M[j]
            j+=1
          k+=1
    
    
  

