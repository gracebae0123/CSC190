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


#x=stack()
#x.push(-5)
#x.push(8)
#x.push(100)
#print(x.pop())
