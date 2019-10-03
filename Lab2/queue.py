class queue:
   def __init__(self):
      self.list = []
      self.count = 0

   def enqueue(self,val):
      self.list += [val]
      self.count +=1
      return self.count

   def dequeue(self):
      if (self.count == 0):
         return [False]

      r = self.list[0]
      self.count -= 1
      self.list = self.list[1:]
      return [True,r]

   def isEmpty(self):
      if (self.count == 0):
         return True
      else:
         return False

   
