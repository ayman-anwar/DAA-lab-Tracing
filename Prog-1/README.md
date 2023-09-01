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

* The previous while loop terminates when either L or M is completely added to the array . So these two while loop is to ensure that there is no element remaining to be added . If yes , it will be added . 

        while i<len(L):
          array[k]=L[i]
          i+=1
          k+=1

        while j<len(M):
          array[k]=M[j]
          j+=1
          k+=1
<hr>
<h4>def selectionsort(array,size):</h4>

    def selectionsort(array,size):
      for step in range(size):
        min_inx=step

        for i in range(step+1,size):
          if array[i]<array[min_inx]:
            min_inx=i
        (array[min_inx],array[step])=(array[step],array[min_inx])

* Sorts with respect to index
* Two nested for loops
* Initially the smallest element will be swapped with the first index,then the next index with the next smallest such that in i'th pass i elements will be sorted
* The first for loop is for index, initially we will consider the current index as min index then the nested for loop will compare with the unsorted elements and store its index in min_inx .
* After finding the min_inx , element in min_inx is swapped with element in current index (step)
* Example:
  <br>array=[20,15,5,10]
  <br>after 1st pass: array=[5,15,20,10] # 5 was the least element, it got replaced with the first array element
  <br>after 2nd pass: array=[5,10,20,15]
  <br>after 3rd pass: array=[5,10,15,20]
  <br>after 4th pass: array=[5,10,15,20]
  <br>->After each pass the left side of the array get sorted

<hr>
<h4>def partition(array,low,high):</h4>

      def partition(array,low,high):
        pivot=array[high]
        i=low-1

        for j in range(low,high):
            if array[j]<=pivot:
                i+=1
                (array[i],array[j])=(array[j],array[i])

        (array[i+1],array[high])=(array[high],array[i+1])
        return i+1

* This function is used find the index for partition for quicksort algorithm.
* It partitions the array in two halves such that the elements in the left side of the partition element will be less than or equal to that element and the elements in the right side will be greater than that element
* Example:
  <br>[5,9,6,8,7]
  
  <br>[5,6,{7},9,8] array will look like this, 7 is the pivot element here,index of 7 is returned
* It takes parameters(low,high) which is starting index and last index.
* The last element is considered as pivot element
* i is initially low-1 that means if lower index is 0 , i will be -1
* The loop (j) will compare if the element is less than or equal to pivot: if yes it will first increment i (since initially low-2) then swap with j
* Once it iterates over all elements it will swap array[high] (i.e,pivot) with array[i+1]
* The partition index is returned (i+1)


<hr>
<h4>def quicksort(array,low,high):</h4>

        def quicksort(array,low,high):
          if low < high :
            s=partition(array,low,high)

            quicksort(array,low,s-1)
            quicksort(array,s+1,high)

* lower index should be less than high index indicating two or more elements: if true
* s = partition index returned by previous function
* recursively call quicksort for low to s-1 and s+1 to high
* <b>Note:</b> s is the partitioned index and its not included  
  
<hr>
<h4>def readinput():</h4>

    def readinput():
      a=[]  
      n=int(input("Enter no. of TV channels:"))
      print("Enter the number of viewers:")
      for _ in range(0,n):
        l=int(input())
        a.append(l)

      return a

* Takes the array input from user

<hr>
<h4>Rest code:</h4>

    elements=list()
    times=list()
    global labeldata

* elements is a list used to store length of array elements, for graph (time complexity part).Initialization .
* times is a list used to store time taken to sort ,for graph. Initialization
* labeldata is a string global variable to keep a note of the sorting technique used

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
        high=len(array)-1
        quicksort(array,0,high)
        print("Sorted list is:")
        print(array)

      else:
        labeldata="Selectionsort"
        array=readinput()
        size=len(array)
        selectionsort(array,size)
        print("Sorted list is:")
        print(array)

* Basic Menu using if else .
* <b>Note: quicksort takes the arguments lower index and high index, therefore high=len(array)-1 and low=0 <br> selectionsort takes argument size therefore size=len(array)</b>

<hr>
<h4>Running time analysis:</h4>

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
* The for loop runs for i=1 to 9
* It creates array of random integers, each time it creates array of 1000*i elements [1000,2000,....9000]
* start=time.time() stores the starting time
* end=time.time() will store the time after sorting
* elements and times is for plotting graph
* elements will contain 1000,2000,....9000
* times will contain time takes i.e, end-start


        plt.xlabel("List length")
        plt.ylabel("Time Complexity")
        plt.plot(elements,times,label=labeldata)
        plt.grid()
        plt.legend()
        plt.show()

* plt.xlabel for labelling x axis
* plt.plot to plot graph (x axis,y axix,label) #x=elements,y=times
* plt.grid() - to add grid lines #wont give error if not added
* plt.legend() - will add borders #wont give error if not added
* plt.show() - to display graph (must)

