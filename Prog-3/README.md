<h2><b>Program -3</b></h2>
<h3>Packages used:</h3>

     import heapq
* Reference - https://www.javatpoint.com/python-heapq-module
* In simple words, it maintains heap property .(refer notes)
* It gives the smallest element in the heap when an element is popped from the heap .
* It automatically maintains heap property after pushing or popping an element from the heap.

<h3>Functions used:</h3>

<h4>def dijkstra(graph,start):</h4>

      def dijkstra(graph,start):
        distances={node:float('inf') for node in graph}
        distances[start]=0
        heap=[(0,start)]

        while heap:
          current_dist,current_node=heapq.heappop(heap)
          
          if current_dist > distances[current_node]:
            continue

          for neighbor,weight in graph[current_node].items():
            distance=current_dist+weight
            if distance < distances[neighbor]:
              distances[neighbor]=distance
              heapq.heappush(heap, (distance,neighbor))

        return distances


* This function is used to find the shortest distance from a source to all otter nodes .
* In this program source is A ,so shortest distance from (A-B, A-C,....,A-E).
* The program is to find the optimal path from source to destination .(shortest)
* This function will give us the shortest distance using dijkstras algorithm . (notes)
* We use dictionary (data structure in python) to store the distances .<br> distances={node:float('inf') for node in graph} : is used to initialize shortest distance of all nodes as infinity initially . So distances will initally look like: <br> distances={'A':inf(♾️),'B':inf,.......,'E':inf}
  <br>   node:float('inf') for node in graph : means all those nodes which in present in graph .(A,....E)
  <br> We know the shortest distance from source to itself is 0. therefore  distances[start]=0, (start will contain A.)
 
  
      distances={node:float('inf') for node in graph}
      distances[start]=0
* We use heap to find the shortest distance so initially heap will contain (0,A) it uses (distance,node) format .

        heap=[(0,start)]

*
  ➡️ We pop the shortest distance everytime to calculate the shortest path .(similar to notes)
  <br> current_dist will contain the popped distance, current_node will contain the node .(<b>(distance,node)format</b>)
  <br> Initially the first popped distance and node is (0,A)
  <br>

      if current_dist > distances[current_node]:
        continue
  this line checks if the popped value is greater than previously found shortest distance of that node .(we will update the shortest distance of each node everytime, therefore if the value popped is greater than the previously found value, there's no point of checking the shortest distance so continue , it will pop the next smallest distance and contniue
  <br>
  <br> ➡️ Now we check the shortest distance from source to all its neighbor .
  <br> We use dictionaries here, our graph looks like :

          graph = {
                    'A': {'B': 3, 'C': 99, 'D': 7, 'E': 99},
                    'B': {'A': 3, 'C': 4, 'D': 2, 'E': 99},
                    'C': {'A': 99, 'B': 4, 'D': 5, 'E': 6},
                    'D': {'A': 7, 'B': 2, 'C': 5, 'E': 4},
                    'E': {'A': 99, 'B': 99, 'C': 6, 'D': 4}
                  }
  <br> so neighbor,weight for A will look like neighbor,weight will look like { (B,3) , (C,99) , (D,7) , (E,99) }

                      'A': {'B': 3, 'C': 99, 'D': 7, 'E': 99},
                      ⬆️    ⬆️  ⬆️
               graph[A]  neighbor weight 
<br> ➡️ Therefore we use graph[current_node].items()
<br> Then we calculate the distance from the current_node to neighbor to check if thats the shortest path .(A-D directly mightnot be the shortest path to reach to D from A,it can be A->C->D as well therefore this will calculate the distance from current_node to all its neighbor.
<br> If the new found distance is less than the previously found distance of that neighbor . then update the shortest distance and push that to heap to continue checking for other nodes .
      
      for neighbor,weight in graph[current_node].items():
        distance=current_dist+weight
        if distance < distances[neighbor]:
          distances[neighbor]=distance
          heapq.heappush(heap, (distance,neighbor))
<br> ➡️ return distances(shortest distance from source to all nodes)

        while heap:
          current_dist,current_node=heapq.heappop(heap)
          
          if current_dist > distances[current_node]:
            continue

          for neighbor,weight in graph[current_node].items():
            distance=current_dist+weight
            if distance < distances[neighbor]:
              distances[neighbor]=distance
              heapq.heappush(heap, (distance,neighbor))

        return distances

<h4>def find_optimal_route(graph,start,destination):</h4>


     def find_optimal_route(graph,start,destination):
       distances= dijkstra(graph,start)

       if distances[destination] == float('inf'):
         return None

       route=[]
       node=destination

       while node!= start:
         route.append(node)
         neighbors=graph[node]
         min_distance=float('inf')
         next_node = None

         for neighbor,weight in neighbors.items():
           if distances[neighbor]+weight == distances[node] and distances[neighbor]<min_distance:
             min_distance=distances[neighbor]
             next_node=neighbor

         if next_node is None or next_node in route:
           return None

         node=next_node

       route.append(start)
       route.reverse()
       return route

* This function is to backtrack and find the optimal path .
* Previous function returns the value of shortest path from source to all vertices, which will be stored in distances.
* Then we check if there exists a path from source to destination.(if there's no path shortest distance would be infinity), if there's no path return
  <br>route is a list used to store the optimal path.
  <br>initialize node as destination .(destination is 'E' in this program) It will backtrack from E to source (A).

       if distances[destination] == float('inf'):
         return None

       route=[]
       node=destination

* The while loop will run until the node becomes start(A) , meaning the path is found.


       while node!= start:
         route.append(node)
         neighbors=graph[node]
         min_distance=float('inf')
         next_node = None

  
  <br> ➡️ We find the route from E to A , so initially it will append E, (then D,B later on)
  <br>We initialize min_distance and next_node to find the min_distance to find the path and next_node to indicate the next node in the path .
  <br>Neighbors is used to keep all the neighbors of that current node . (initially neighbors of E)

       for neighbor,weight in neighbors.items():
           if distances[neighbor]+weight == distances[node] and distances[neighbor]<min_distance:
             min_distance=distances[neighbor]
             next_node=neighbor
  <br> ➡️ Then we check if the shortest distance of neighbor (from source) + its distance to the node (initially E) is equal to the shortest distance of node (initially E),also we check if its less than min_distance(initially it will be infinity) (this is to make sure that the next node will give you optimal path.
  <br> If both conditons are met we then update the min_distance and next_node with neighbor (since thats the path).

       if next_node is None or next_node in route:
           return None

       node=next_node

       route.append(start)
       route.reverse()
       return route


  <br> ➡️ Then we check if next_node is empty or if its already in route (meaning it forms a cycle).if true return None (no optimal path)
  <br>node is updated with the previously found next_node and the loop runs until the node becomes A.
  <br> Since it terminates from the loop when its A, A is not added to the route so append(start) .
  <br> The route we found is in reverse order(E-D-B-A) , so reverse route, then return.

            
       while node!= start:
         route.append(node)
         neighbors=graph[node]
         min_distance=float('inf')
         next_node = None

         for neighbor,weight in neighbors.items():
           if distances[neighbor]+weight == distances[node] and distances[neighbor]<min_distance:
             min_distance=distances[neighbor]
             next_node=neighbor

         if next_node is None or next_node in route:
           return None

         node=next_node

       route.append(start)
       route.reverse()
       return route

<h4>Rest code:</h4>


     graph = {
    'A': {'B': 3, 'C': 99, 'D': 7, 'E': 99},
    'B': {'A': 3, 'C': 4, 'D': 2, 'E': 99},
    'C': {'A': 99, 'B': 4, 'D': 5, 'E': 6},
    'D': {'A': 7, 'B': 2, 'C': 5, 'E': 4},
    'E': {'A': 99, 'B': 99, 'C': 6, 'D': 4}
     }

     start_location = 'A'
     destination_location = 'E'

     optimal_route = find_optimal_route(graph, start_location, destination_location)

     if optimal_route is None:
         print("No valid route exists from the start to the destination.")
     else:
         print("Optimal Route:", ' -> '.join(optimal_route))

* Initialize graph , start and destination.
* Find the optimal path by calling find_optimal_route() function.
* Print optimal route.
  <br> Optimal route will be a list containing A,B,D,E so to print in A->B->D->E  format we use

            print("Optimal Route:", ' -> '.join(optimal_route))
  So it will print one value from optimal route then add "->".
