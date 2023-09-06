<h2><b>Program -3</b></h2>

<h3>Packages used:</h3>

      from collections import defaultdict

* defaultdict is used for dictionaries. If you try to access a key which is not present in the dictionary it will give a 'Key Error' , to avoid that we use this class.

<h3>Class:</h3>

            class Graph:
                def __init__(self, subjects):
                    self.subjects = subjects
                    self.graph = defaultdict(list)
            
                def add_edge(self, subject1, subject2):
                    self.graph[subject1].append(subject2)
                    self.graph[subject2].append(subject1)
            
                def graph_coloring(self):
                    color_map = {}
                    available_colors = set(range(1, len(self.subjects) + 1))
            
                    for subject in self.subjects:
                        used_colors = set()
            
                        for neighbor in self.graph[subject]:
                            if neighbor in color_map:
                                used_colors.add(color_map[neighbor])
            
                        available_color = available_colors - used_colors
            
                        if available_color:
                            color_map[subject] = min(available_color)
                        else:
                            # If no available color, assign a new color
                            color_map[subject] = len(available_colors) + 1
                            available_colors.add(color_map[subject])
            
                    return color_map
            
                def get_minimum_time_slots(self):
                    color_map = self.graph_coloring()
                    return max(color_map.values())


* class name Graph , it will contain the subjects list (math,....,biology) and graph(which represents the subjects connected)
* All the functions in this program is written inside the class.
* it initializes subjects with subjects and graph as defaultdict(list)
* The theory behind this is simple, each subject is considered as vertices and it will be connected to other subjects, we have to color the vertices such as no two vertices(subjects) will have the same color.
<br><hr>
<h4> def add_edge(self, subject1, subject2):</h4>

       def add_edge(self, subject1, subject2):
          self.graph[subject1].append(subject2)
          self.graph[subject2].append(subject1)
* This function is used to add edge to the graph .
* Since it's an undirected graph if theres an edge from 1-2 implies theres an edge from 2-1 as well.
* We add (math,physics).......(physics,biology) in later part of the code , so finally our graph will look like
  <br>

          graph={
                'Math':['Physics','Chemistry'],
                'Physics':['Math'],
                'Chemistry':['Math','Physics'],
                'Biology':['Physics']
                }
  This is our graph to refer for coloring, math is connected to physics and chemistry,....biology is connected to physics.

<br>
<hr>
<h4> def graph_coloring(self):</h4>

                  def graph_coloring(self):
                    color_map = {}
                    available_colors = set(range(1, len(self.subjects) + 1))
            
                    for subject in self.subjects:
                        used_colors = set()
            
                        for neighbor in self.graph[subject]:
                            if neighbor in color_map:
                                used_colors.add(color_map[neighbor])
            
                        available_color = available_colors - used_colors
            
                        if available_color:
                            color_map[subject] = min(available_color)
                        else:
                            # If no available color, assign a new color
                            color_map[subject] = len(available_colors) + 1
                            available_colors.add(color_map[subject])
            
                    return color_map
* This function will asign a color to each subject and return (color_map) ,we use (1,2,3,4) as different colors.
* color_map is a dictionary used to store the subject and the respective color assigned
* Then we set available colors as a set(1,2,3,4) ,since there are 4 subjects we need max 4 colors.

      available_colors = set(range(1, len(self.subjects) + 1))
 len(self.subjects)-4 but range from(1,4) will not include 4 so therefore len(self.subjects)+1 .
 <br> You can simply use:

      available_colors = set(range(1,5))
  it will work the same

* Next step is to assign color,first we will find the available colors for that subject, for that we must know which are the colors used by its neighbors(the vertices with which it has an edge) .
  <br>➡️ We make use used_colors=set() for this .
  <br>➡️ Now we check if the neighbor is already assigned a color , to know that we will check in color_map ( it will contain the color assigned to every subject, initially it will be empty as we assign colors we will update color_map, so if neighbor is in color_map implies neighbor is already assigned a color,and that color cannot be used for this subject)
  <br>➡️ so if neighbor is in color_map we will add that color to used_colors which we will get from 'color_map[neighbor]'.
  <br>➡️ For the first subject there will not be any used colors since no neighbor is assigned a color.
  <br>➡️ then we find availale_color for that particular subject.(it will be the difference of available_colors (1,2,3,4) and used_colors (depending on each subject's neighbors)

                      for subject in self.subjects:
                        used_colors = set()
            
                        for neighbor in self.graph[subject]:
                            if neighbor in color_map:
                                used_colors.add(color_map[neighbor])
            
                        available_color = available_colors - used_colors
  <br>➡️ Then if there is any available color we assign the minimum possible color for that subject. For Math, available_color will be 1,2,3,4 so we assign 1 as the color of maths.Update color_map.(else part can be skipped)

        if available_color:
          color_map[subject] = min(available_color)
  
  <br>➡️ color_map after assigning color to math will look like:

        color_map={
                    'Math':1
                  }
  <br>➡️ Similarly we will find available colors for all subjects and assign a color.
  <br>➡️ Since math is assigned a color since physics & chemistry has math as a neighbor they cant use the color 1.
  <br>➡️ Our question is to find the min colors required such that the conditions are met.
  <br>➡️ Once every subject is assigned a color it will look like this :

      {'Math': 1, 'Physics': 2, 'Chemistry': 3, 'Biology': 1}
➡️ So we can see that we had to use min of three colors to color the subjects.(which we will return in the next function)
<b>Note: This part of the code can be skipped since there is already 4 colors for 4 subjects and we dont need more colors</b>

        else:
          # If no available color, assign a new color
          color_map[subject] = len(available_colors) + 1
          available_colors.add(color_map[subject])


<hr>
<h4> def get_minimum_time_slots(self):</h4>

      def get_minimum_time_slots(self):
        color_map = self.graph_coloring()
        return max(color_map.values())
* It will use the previous function to assign colors and store it in color_map and then return the max of value assigned to subject.(since max i.e, 3 is the minimum no. of colors required.)
<hr>
<h4> Rest code:</h4>

      subjects = ['Math', 'Physics', 'Chemistry', 'Biology']
      students = {
          'Math': ['Alice', 'Bob', 'Charlie'],
          'Physics': ['Alice', 'Charlie', 'David'],
          'Chemistry': ['Bob', 'Charlie', 'Eve'],
          'Biology': ['Alice', 'David', 'Eve']
      }
      
      graph = Graph(subjects)
      graph.add_edge('Math', 'Physics')
      graph.add_edge('Math', 'Chemistry')
      graph.add_edge('Physics', 'Chemistry')
      graph.add_edge('Physics', 'Biology')
      
      minimum_time_slots = graph.get_minimum_time_slots()
      print(f"Minimum time slots needed: {minimum_time_slots}")

* subjects will contain the list of subjects
* students dictionary can be skipped since we are not using it anywhere in the code or just define some random names .

        students = {
          'Math': ['Alice', 'Bob', 'Charlie'],
          'Physics': ['Alice', 'Charlie', 'David'],
          'Chemistry': ['Bob', 'Charlie', 'Eve'],
          'Biology': ['Alice', 'David', 'Eve']
      }

  <br>
* Use the Graph class in object graph.
* Add all edges and call the function.
  
