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


<a name="print"></a>
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
* [Click Here](#rest_code) Let's understand the working of the code first then get back to printing values.
* This takes two parameter one is node and val . node will contain root intially then we call recursively till we get to each leaf or child. val will be initially empty so val='' . (later when we call recursively we will pass its huff value i.e, 0 or 1 to the next node , so that we get for eg.110,101 etc)
* Initially node is root, we find newVal to pass when we call the function recursively.
* <b>Note: We gave huff values as 0 or 1 . so if we add directly it will add mathematically but we want it to just concatenate(1+0=10) so therefore we convert node.huff value to string.</b>
* We check if there exists a left child, if yes then we call the function recursively passing left child.
* Similarly check for right child.
* When there is no left child or right child anymore we print the symbol and its value .
* <b>Note: We use if condition multiple times to call recursively not if else . if else wont throw error but will give you wrong result.</b>

<h4>def printDecode(node,val=''):</h4>

          def printDecode(node,val=''):
            newVal= val+str(node.huff)
          
            if(node.left):
              printDecode(node.left,newVal)
            if(node.right):
              printDecode(node.right,newVal)
            if (not node.left and not node.right):
              print(f"  {newVal}  -->  {node.symbol}")
* This function simply prints in Value --> character format
* Works same as encoding part. 
  
<hr>
<a name="rest_code"></a>
<h4>Rest code:</h4>

               n=int(input("Enter the number of chars:"))
               chars=[]
               for i in range(n):
                 c=input(f"Enter {i+1} char:")
                 chars.append(c)
               print(chars)
               
               freq=[]
               for i in range(n):
                 f=int(input(f"Enter {i+1} freq:"))
                 freq.append(f)
               print(freq)
               
               nodes=[]
               
               for x in range(len(chars)):
                 heapq.heappush(nodes,node(freq[x],chars[x]))
               
               while len(nodes)>1:
                 left=heapq.heappop(nodes)
                 right=heapq.heappop(nodes)
                 left.huff=0
                 right.huff=1
               
                 newNode=node(left.freq+right.freq,left.symbol+right.symbol,left,right)
                 heapq.heappush(nodes,newNode)
               
               print("Encoded form is:")
               printNodes(nodes[0])
               
               print("Decodes form is:")
               printDecode(nodes[0])
* We take number of chars, and store the characters in chars=[].
* Similarly we take frequencies and store in freq=[]
* Now, the working of code is similar to problems we solve manually.
* We first sort the chars according to frequencies then add the first two nodes with lower frequency , and next step we add the newly create node to the nodes list and sort again ,continue these steps till we get one single node which is root , which will create a tree .
* The higher frequency character will have shorter code.
* So to sort initially we use heap, we store it in nodes=[]
* In this step we add all the initial characters to nodes.
  <br><b>Note:we create an object of class node by passing its freq and char ,and then add that to nodes</b>
  <br>Now nodes will have all nodes sorted


               nodes=[]
               for x in range(len(chars)):
                 heapq.heappush(nodes,node(freq[x],chars[x]))
* Now the working part: pop two nodes which will give you the two nodes with smallest frequency.left child will be the one which has the smallest frequency so first pop is for left ,second for right .(to create tree)
  <br>➡️ We assign huff vale for left(0) and right(1) .
  <br>➡️ Now we create a newnode with its freq as sum of both frequencies,symbol as sum of both symbols.(a+b=ab),now we will assign left child and right child for this newly created node and push this to nodes using heapq to sort .
  <br>➡️ We will repeat thi steps till we get single node . That is, entry condition while len(nodes)>1: will terminate when only one node is left which will be our root.


            while len(nodes)>1:
                 left=heapq.heappop(nodes)
                 right=heapq.heappop(nodes)
                 left.huff=0
                 right.huff=1
               
                 newNode=node(left.freq+right.freq,left.symbol+right.symbol,left,right)
                 heapq.heappush(nodes,newNode)
* Now that we found the tree and assigned values to left child and right child, next we will print by using printNodes function by passing the root which will be stored in nodes[0] .
 <br><b>Note: The values 0 for every left child and 1 for every right child will be stored in that particular nodes .huff value which we assigned while creating newnode .</b>
<br> [Click Here](#print) Now we print in encoding and decoding format.

               print("Encoded form is:")
               printNodes(nodes[0])
               
               print("Decodes form is:")
               printDecode(nodes[0])
