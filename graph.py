class stack:
   def __init__(self):
      self.x=[]
      self.count = 0

   def store(self, value):
      self.x += [value]
      self.count+=1
      return True

   def delete(self):
      if (self.count == 0):
         return [False,0]
      r = self.x[-1]
      self.x = self.x[0:-1]
      self.count -= 1;
      return [True, r]


   def isEmpty(self):
      if (self.count == 0):
         return True
      else:
         return False

class queue:
   def __init__(self):
      self.x = []
      self.count = 0

   def store(self,val):
      self.x += [val]
      self.count +=1
      return self.count

   def delete (self):
      if (self.count == 0):
         return [False,0]
      r = self.x[0]
      self.count -= 1
      self.x = self.x[1:]
      return [True,r]

   def isEmpty(self):
      if (self.count == 0):
         return True
      else:
         return False



class graph:
   def __init__(self):
      self.store = []  
     
   def addVertex(self,n):
      if n<=0:
         return -1
      for i in range(0,n):
         length = len(self.store)
         self.store +=[[[length]]]
      return len(self.store)
      
   def addEdge(self,from_idx,to_idx,directed,weight):
      if from_idx <0 or to_idx<0 or weight ==0:
         return False
      elif from_idx>(len(self.store)-1) or to_idx>(len(self.store)-1):
         return False
      if directed:
         self.store[from_idx] +=[[to_idx,weight]]
         return True
      else:
         self.store[from_idx] +=[[to_idx,weight]]
         self.store[to_idx] +=[[from_idx,weight]]
         return True
      return False

   def traverse(self,start,typeBreadth):
      if start and start<0:
         print("fail")
         return []
      elif start>=len(self.store):
         print("too long")
         return []
      if typeBreadth:
         c = queue()
      else:
         c = stack()

      discovered = []
      processed = []
      total = []
      if start == None:
         for i in range(0,len(self.store)):
            discovered +=[False]
            processed +=[False]
         for i in range(0,len(self.store)):
            output = list() 
            if discovered[i] == False:
               c.store(self.store[i])
               discovered[i] = True

            while c.x:
               w = c.delete()[1]
            #   print("printing w",w)
            #   print(w[0])
               if processed[w[0][0]] == False:
                  output = output +w[0]
                  processed[w[0][0]] = True
               for y in range (1,len(w)):
                  x = w[y][0]
            #      print("x=",x)
                  if discovered[x] == False:
                     c.store(self.store[x])
                     discovered[x] = True
            if (output):
               total = total+[output]

      elif start != None:
         for i in range(0,len(self.store)):
            discovered +=[False]
            processed +=[False]
         i = start
         if discovered[i] == False:
            c.store(self.store[i])
            discovered[i] == True
         while c.x:
            w = c.delete()[1]
           # print("printing w",w) 
            if processed[w[0][0]] == False:
               total = total+w[0]
               processed[w[0][0]] = True 
            for y in range (1,len(w)):
               x =w[y][0]
           #    print("printing x:",x)
               if discovered[x] == False:
                  c.store(self.store[x])
                  discovered[x] = True
      return total 

      #error --> empty list
      #start = None or non-negative
      #start == None: traversal must traverse the entire graph (including all of the subgraphs that may be disconnected from one another)
      #start == int: up to the max idx of graph vertices --> traverse to whatever vertices that are connected to it
      #invalid start ==> error
      #True == Breadth False == Depth
      #rval: list consisting of all nodes visited via the traversla
      # if start is set (valid int) --> one list
      #not a set --> list of lists(sublist = differnt connected substet of the graph)
        

   def connectivity(self,vx,vy):
      output = [False,False]
      path = self.path(vx,vy)
      reverse = self.path(vy,vx)
      if path[0]:
         output[0] = True
      if reverse[0]:
         output[1] =True
      return output


   def path(self,vx,vy):
      rlist = [False,False]
      output = self.traverse(vx,True)
      #print("OUTPUT:",output)
      for i in range(len(output)-1,-1,-1):
         if output[i] == vy:
            break
         else:
            del(output[i])
      #print(output)
    
      for i in range(len(output)-2,0,-1):
         prev = self.store[output[i]]
         connected = 0
         for j in range(len(prev)-1,0,-1):
            if prev[j][0] == output[i+1]:
               connected = 1
         if connected == 0:
            del output[i]

      #print(output)
      output2 = self.traverse(vy,True)
      #print("OUTPUT2:",output2)
      for i in range(len(output2)-1,-1,-1):
         if output2[i] == vx:
            break
         else:
            del output2[i]

      #print(output2)
      for i in range(len(output2)-2,0,-1):
         prev = self.store[output2[i]]
         connected = 0
         for j in range(len(prev)-1,0,-1):
            if prev[j][0] == output2[i+1]:
               connected = 1
         if connected == 0:
            del output2[i]
      return [output,output2]
   #rlist[0] = list of vertics from vx to vy --> else []
   #rlist[1] = lsit of vertices from vy to vx --> else []



x=graph()
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
print("before:")
print(x.store)
x.addEdge(0,1,False,1)
x.addEdge(0,2,False,1)
x.addEdge(0,3,False,1)
x.addEdge(1,2,False,2)
x.addEdge(1,4,False,2)
x.addEdge(2,3,True,3)
x.addEdge(3,4,True,4)
x.addEdge(4,5,True,5)
print("after adding edges")
print(x.store)
print ("Depth")
print (x.traverse(0,False))
print ("Breadth")
print (x.traverse(0,True))
print ("Breadth; start=None")
print (x.traverse(None,True))
print(x.path(0,3))

