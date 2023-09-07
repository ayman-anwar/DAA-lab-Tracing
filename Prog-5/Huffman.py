import heapq

class node:
  def __init__(self,freq,symbol,left=None,right=None):
    self.freq=freq
    self.symbol=symbol
    self.left=left
    self.right=right
    self.huff=''

  def __lt__(self,nxt):
    return self.freq<nxt.freq

def printNodes(node,val=''):
  newVal= val+str(node.huff)

  if(node.left):
    printNodes(node.left,newVal)
  if(node.right):
    printNodes(node.right,newVal)
  if (not node.left and not node.right):
    print(f"  {node.symbol}  -->  {newVal}")

def printDecode(node,val=''):
  newVal= val+str(node.huff)

  if(node.left):
    printDecode(node.left,newVal)
  if(node.right):
    printDecode(node.right,newVal)
  if (not node.left and not node.right):
    print(f"  {newVal}  -->  {node.symbol}")


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
