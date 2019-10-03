from tree import *
from queue import *

class binary_tree:

   def __init__(self,val):
      self.store = [val,None,None] 

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
    

     
#   def ConvertToTree(self,root):
#      gt = tree(self.store[0]
#      sib = []
#
#      while True:
#         for idx in range(len   
          

#take in list of branches
# if lore, return binary tree of that value
# if children: add left binary tree of first born
# if siblings: add right binary tree of other siblings
