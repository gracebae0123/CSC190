class stack:
   def __init__(self):
      self.x = []
      self.count = 0
   def push (self, val):
      self.x += [val]
      self.count+=1
      return True
   def pop(self):
      r = self.x[len(self.x)-1]
      self.x = self.x[0:len(self.x)-1]
      self.count -=1
      return r
   def isEmpty(self):
      if self.count == 0:
         return True
      else: 
         return False


class queue:
   def __init__(self,length):
      self.x = []
      self.maxL = length
   def add(self, value):
      if len(self.x) == self.maxL:
         return False
      else:
         self.x = self.x + [val]
      return True
   def del(self):
      r = self.x[0]
      self.x = self.x[1:len(self.x)]
      return r

   


def main(string):
   a = stack()
   n = 0

   for char in string:
      if (char == '(' or char == '{' or char == '['):
         a.push(char)
      elif (char == ')'):
         result = a.pop()
         if (result[0] != '('):
            return False
      elif (char == ']'):
         result = a.pop()
         if (result[0] != '['):
            return False
      elif (char == '}'):
         result = a.pop()
         if (result[0] != '{'):
            return False
      n+=1
   
   if (a.isEmpty() == True):
      return True
   else:
      return False


#main("{ [1 + (a+b)] + [ 2 + (c+d) ] }")
#main("({ [1 + (a+b)) + [ 2 + (c+d) ] })")

