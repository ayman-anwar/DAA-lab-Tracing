<h2><b>Program - 5</b></h2>
<h3>Packages used:</h3>

     import heapq
* Reference - https://www.javatpoint.com/python-heapq-module
* In simple words, it maintains heap property .(refer notes)
* It gives the smallest element in the heap when an element is popped from the heap .
* It automatically maintains heap property after pushing or popping an element from the heap.

<h3>Class:</h3>



      class node:
        def __init__(self,freq,symbol,left=None,right=None):
          self.freq=freq
          self.symbol=symbol
          self.left=left
          self.right=right
          self.huff=''
      
        def __lt__(self,nxt):
          return self.freq<nxt.freq
* Class named node , which uses an initialization function to initialize freq,symbol(character),left and right nodes,huff (0 if left child 1 if right child which we will assign in later part of the code)
* left=None and right=None is mentioned in parameter because initially we ask the user the freq and char only, so we only pass freq,symbol while creating the object, so if you don't specify left=None,right=None it will throw an error.
* This function is a condition for 'less than' (<) operation (lt) , used for heap to push elements into heap. Since there are multiple attributes or variables for class node, we specify according to which value our heap should be created.We create with respect to freq.

<h3>Functions used:</h3>

<h4>def printNodes(node,val=''):</h4>

        def printNodes(node,val=''):
          newVal= val+str(node.huff)
        
          if(node.left):
            printNodes(node.left,newVal)
          if(node.right):
            printNodes(node.right,newVal)
          if (not node.left and not node.right):
            print(f"  {node.symbol}  -->  {newVal}")
* This function is used to print the encoded characters in charcter --> huffman code format.
* [Click Here](#Rest code:)Let's understand the working of the code first then get back to printing values.


<h4>Rest code:</h4>
  
