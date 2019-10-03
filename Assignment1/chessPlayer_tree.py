class queue:
   def __init__(self):
      self.store = []
      self.length = 0

   def enqueue(self,value):
      self.store +=[value]
      self.length +=1

   def dequeue(self):
      if self.length == 0:
         return [False]
      rval = self.store[0]
      self.store = self.store[1:]
      self.length -=1
      return [True,rval] 


class evalTree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1]+[x]
      return True

   def Helper(self,indentlevel):
      print (self.store[0])
      #length = length of the list in the fake binary tree
      for i in range (len(self.store[1])):
         temp = self.store[1][i]
         #tab
         for j in range(0,indentlevel):
            print("\t")
         temp.Helper(indentlevel+1)
      return 0

   def PrintDepthFirst(self):
      self.Helper(1)
      return 0

   def GetLevelOrder(self):
      x= queue()
      x.enqueue(self.store)
      accum=[]
      while True:
         y=x.dequeue()
         #y is a 2-list where y[0] = T/F
         #y[1] = actual dequeued value when y[0] ==True
         if (y[0] == False):
            break
         else:
            v=y[1]
            accum+=[v[0]]
            for i in v[1]:
               x.enqueue(i.store)
      return accum



