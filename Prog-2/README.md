<h2><b>Program -2</b></h2>
<h3>Classes and objects:</h3>
Reference - https://www.javatpoint.com/python-objects-classes

* In simple words, class will contain variables (attributes) and methods , which can be used by objects .
* Its similar to structures in C but structures can only contain variables not functions .
* Objects must be created to access the class attributes and functions

<br>
<br>

      class Job:
        def __init__(self,taskId,deadline,profit):
          self.taskId=taskId
          self.deadline=deadline
          self.profit=profit
* This function is a constructor to initialize variables of that class .
* Here, class Job has taskId,deadline,profit as its attributes and no functions .

<h3>Functions:</h3>

<h4>def scheduleJobs(jobs,T):</h4>

    def scheduleJobs(jobs,T):
      slot=[-1]*T
      profit=0
      jobs.sort(key=lambda x:x.profit ,reverse=True)
      for job in jobs:
        for j in reversed(range(job.deadline)):
          if j<T and slot[j]==-1:
            slot[j]=job.taskId
            profit+=job.profit
            break
      print("The scheduled jobs are:",list(filter(lambda x:x!=-1,slot)))
      print("The total profit is",profit)

* This function takes jobs and T as parameters .
* jobs - contain objects job1,job2,.....jobn <br> T - is the deadline limit for the job.
* This function works exactly as algorithm/problems. (notes)
* Initially all the slots will be empty , therefore we make all the slots as -1 .

      slot=[-1]*T #this will create a slot =[-1,-1,....upto the value T]
  Example: slot=[-1]*4 will give you slot=[-1,-1,-1,-1]
* Profit will be initially 0 .
* This line sorts the jobs . The catch here is each job in jobs contain 3 attributes so therefore we must specify sort according to what, which is done be using  key=lambda .
  <br> We specify x:x.profit - meaning sort according to their profits . <br> The next thing here is sort generally sorts ascending order but according to the problem we sort descending order of profits (max profit first) therefore we specify reverse=True

      jobs.sort(key=lambda x:x.profit ,reverse=True)
* Now our jobs will be in descending order of profits
* Next step is to assign slots for each job
<br>
<br>

       for job in jobs:
        for j in reversed(range(job.deadline)):
          if j<T and slot[j]==-1:
            slot[j]=job.taskId
            profit+=job.profit
            break

* for job in jobs - will iterate every job present in jobs .<br> As its already sorted, we must now assign it a slot .<br> In problems, we assign the max slot possible according to its deadline.(if its deadline is 3 we try to assign it to slot 2-3 , if there is already a job assigned to it we check the next available slot).<br> Here the line

      for j in reversed(range(job.deadline)):
  is to check the same . it checks from its deadline to 0, therefore reversed(range(job.deadline))
* next it checks if the deadline is less than the limit and if there is already a job assigned to that slot.(if slot==-1 means slot is empty)
* if the conditions are met that slot is assigned to that job .(taskId)
* profit of that job is added to total profit
* break .<b> Note : break is used because once you assign a slot theres no point of checking for other slots, failing to put break will assign the first job to every slot available </b>
<br>
<br>

      print("The scheduled jobs are:",list(filter(lambda x:x!=-1,slot)))
      print("The total profit is",profit)

* print scheduled jobs and profit
* while printing slots we only print the jobs scheduled , there might be a slot which is not assigned with any job and that slot will have the value -1 .So therefore while printing to make sure that -1 is not printed we use the following function which defines filter, filter what? , lambda x:x!=-1 , meaning filter only those values which are not equal to -1 from slot

<h4>if __name__ =="__main__":</h4>

      if __name__ =="__main__":
        jobs=[]
        print("Enter decreasing order:")
        n=int(input("Enter no. of jobs:"))
        for i in range(n):
          taskId=int(input(f"Enter the taskID for job {i+1}: "))
          deadline=int(input(f"Enter the deadline for job {i+1}: "))
          profit=int(input(f"Enter the profit for job {i+1}: "))
          jobs.append(Job(taskId,deadline,profit))

        T=int(input("Deadline limit:"))
        scheduleJobs(jobs,T)

* This is the main function , similar to void main() in C . The entry point for execution
* jobs=[] is to initialize a list to which we will add each job
* We take the number of jobs as input .
* Then taskid,deadline,profit for each job .
* Now we have to store all these values in an object ,i.e, we will call the class Job() and pass these three arguments.
* Then we append that object to jobs list
* jobs.append(Job(taskId,deadline,profit)) , this line does the two steps , and basically the jobs list will contain object of job1,job2,..jobn and each job will contain its own taskid,deadline and profit
* Enter the deadline limit and call the function .
  
