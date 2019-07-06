def selection_sort(u):
   for i in range(len(u)):
      mini = i
      for j in range(i+1,len(u)):
         if u[mini] > u[j]:
            mini = j
      temp = u[i]
      u[i] = u[mini]
      u[mini] = temp
   return True

def heap_helper(u,end,root):
   left = (2*root)+1
   right = (2*root)+2
   m = root
   if left <end and u[root] < u[left]:
      m = left
   if right<end and u[m] <u[right]:
      m = right
   if m != root:
      temp = u[root]
      u[root] = u[m]
      u[m] = temp
      heap_helper(u,end,m)
   return True


def heapify(u):
   for i in range(len(u),-1,-1):
      heap_helper(u,len(u),i)
   return True   

def reheapify(u,end):
   temp = u[0]
   u[0] = u[end]
   u[end] = temp
   return True 

def heap_sort(u):
   heapify(u)
   for i in range(len(u)-1,0,-1):
      reheapify(u,i)
      heap_helper(u,i,0)
   return True

def merge_help(u):
   if len(u)<= 1:
      return u 
   half = len(u)/2
   left = merge_help(u[:half])
   right = merge_help(u[half:])
   help_merge(u,left,right)
   return u
   

def help_merge(u,left,right):
   temp = []
   done = False
   i = j = 0
   while not done:
      if left[i] < right[j]:
         temp+=[left[i]]
         i+=1
      else:
         temp+=[right[j]]
         j+=1
      if i == len(left):
         temp+=right[j:]
         break
      if j == len(right):
         temp +=left[i:]
         break
   for i in range (len(u)):
      u[i] = temp[i]
   return u 
      
def merge_sort(u):
   if len(u) <=1:
      return u
   merge_help(u)
   return True


v1=[10,9,8,7,6,5,4,3,2,1,0]
v2=[100,1,1000,9,8,7,2,2000,10]
v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

for i in [ v1,v2,v3 ]:
   x=list(i)
   print("selection sort:")
   selection_sort(x)
   print (x)

   x=list(i)
   print("heapify: ")
   heapify(x)
   print (x)

   x=list(i)
   print("heap sort:")
   heap_sort(x)
   print (x)

   x=list(i)
   print("merge sort")
   merge_sort(x)
   print (x)

   print ("\n NEXT ONE\n")
