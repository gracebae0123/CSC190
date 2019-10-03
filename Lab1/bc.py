from stackLib import *

def bc (string):
   z = stack()
   n = 0
   for char in string:
      if (char =='(') or (char == '[') or (char == '{'):
         z.push(char)
      elif (char == ')'):
         result = z.pop()
         if (result[0] != '('):
            return [False, n]
      elif (char == ']'):
         result = z.pop()
         if (result[0] != '['):
            return [False, n]
      elif (char == '}'):
         result = z.pop()
         if (result[0] != '{'):
            return[False, n]
      n+=1

   if (z.isEmpty() == True):
      return [True, 0]
   else:
      return [False, n]

      
         
