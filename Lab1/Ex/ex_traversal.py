class Queue:
   def __init__(self):
      self.list = []
      self.count = 0
   
   def enqueue(self,val):
      self.list = self.list+[val]
      self.count +=1
      return True

   def dequeue(self):
      d=self.list[0]
      self.count -=1
      self.list = self.list[1:]
      return d

   def empty(self):
      if self.count == 0:
         return True
      else:
         return False
      


def traverse_breadth(T):
   x = Queue()
   x.enqueue(T)
   while (x.empty() == False):
      r=x.dequeue()
      print(r[0])
      for i in r[1:]:
         x.enqueue(i)


T = ['a',['b',['c','d','e','f'],'g'],['h',['I',['j',['k','l'],'m']]]]

traverse_breadth(T)
