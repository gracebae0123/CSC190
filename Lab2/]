from queue import *

class binary_tree:
   def __init__(self,val):
      self.store = [val,True,True]
   def AddLeft(self, val):
      self.store[1] = val
      return True
   def AddRight(self, val):
      self.store[2] = val
      return True

   def Get_LevelOrder(self):
      q = queue()
      q.enqueue(self.store)
      rlist = []
      while True:
         x = q.dequeue()
         if (x[0] == False):
            break
         elif (type(x[1]) == int) or (type(x[1] == str)):
            rlist += [x[1]]
         inside = x[1]
         if x[1] == []:
            continue
         else:
            if type(inside) == list:
               rlist  = rlist +[inside[0]]
               for idx in inside[1:]:
                  q.enqueue(idx)
            elif type(inside) == str:
               continue
            elif inside == []:
               continue
            else:
               rlist +=[(inside.store)[0]]
               q.enqueue((inside.store)[1]) 
               q.enqueue((inside.store)[2]) 
      return rlist

class stack:
   def __init__(self):
      self.x=[]
      self.count = 0

   def push(self, value):
      self.x = self.x + [value]
      self.count+=1
      return True

   def pop(self):
      if (self.count == 0):
         return [False]

      r = self.x[len(self.x)-1]
      self.x = self.x[0:len(self.x)-1]
      self.count -= 1;
      return [True, r]

   def isEmpty(self):
      if (self.count == 0):
         return True
      else:
         return False


class tree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self, x):
      self.store[1] = self.store[1] + [x]
      return True
   
   def getSuccessor(self):
      return self.store[1]


#Assignment 1
   def Print_DepthFirst(self):
      self.Print_DepthFirst_helper("   ")
      return True

   def Print_DepthFirst_helper(self,prefix):
      print prefix + str(self.store[0])
      for i in self.store[1]:
         i.Print_DepthFirst_helper(prefix+"  ")
      return True
      

#Assignment 2
   def Get_LevelOrder(self):
      q = queue()
      q.enqueue(self.store)
      rlist = []

      while (1):
         x = q.dequeue()
         if (x[0] == False):
            break
         else:
            inside = x[1]
            rlist += [inside[0]]
            for element in inside[1]:
               q.enqueue(element.store)
      return rlist   
             
#Assignment 4
   def ConvertToBinaryTree (self):
      init = binary_tree(self.store[0])
      nodes = self.store[1]
      init.AddLeft(self.toBinary(nodes))
      return init
 
   def toBinary (self,root):
      bint = binary_tree(root.store[0])
      sib = []
      
      if root.store[1] != []:
         for idx in range(len(root.store[1])):
            sib = sib + [binary_tree(root.store[1][idx].store[0])]
         
         for idx in range(len(sib)-1):
            if root.store[1][idx].store[1] != []:
               sib[idx] = self.toBinary(root.store[1][idx])
            sib[idx].AddRight(sib[idx+1])
             
         bint.AddLeft(sib[0])

      return bint
              
#   def toBinary(self,nodes):
#      if self.store == [] or nodes == []:
#         return False
#      else:
#         current = nodes[0]
#         if current == []:
#            return False
#         sibs = nodes[1:]
#         root = binary_tree(current.store[0])
#         L = self.toBinary(current.store[1])
#         R = self.toBinary(sibs)
#         root.AddLeft(L)
#         root.AddRight(R)
#         return root
    
root=tree(1000)
x=tree(2000)
y=tree(3000)
z=tree(4000)
x1=tree(201)
x2=tree(202)
x3=tree(203)
y1=tree(301)
y2=tree(302)
y3=tree(303)
root.AddSuccessor(x)
root.AddSuccessor(y)
root.AddSuccessor(z)
x.AddSuccessor(x1)
x.AddSuccessor(x2)
x.AddSuccessor(x3)
y.AddSuccessor(y1)
y.AddSuccessor(y2)
y.AddSuccessor(y3)
c=tree(3)
d=tree(1)
e=tree(4)
f=tree(1)
g=tree(5)
f.AddSuccessor(g)
e.AddSuccessor(f)
d.AddSuccessor(e)
c.AddSuccessor(d)
z.AddSuccessor(c)
root.Print_DepthFirst()
print (root.Get_LevelOrder())
BT=root.ConvertToBinaryTree()
print (BT.Get_LevelOrder())
