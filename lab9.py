def partition(array,left,right):
   pivot = array[left]
   low = left+1
   high = right
   while low <= high: #>pivot
      while array[low] < pivot:
         low+=1
         if low == len(array):
            break
      while array[high] > pivot:
         high -=1
         if high == -1:
            break
      print("low:",low)
      print("high:",high)
      if low <= high:
         temp = array[low]
         array[low] = array[high]
         array[high] = temp
         print("partitioning:",array)
   temp = array[left]
   array[left] = array[high]
   array[high] = temp
   print("end of partitioning:",array)

   return high

def quicksort(array,left,right):
   if left <= right:
      pivot = partition(array,left,right)
      quicksort(array,left,pivot-1)
      quicksort(array,pivot+1,right) 
   return True

data = [5,1,3,7,9,2,4,6,8]
print("original",data)
quicksort(data,0,len(data)-1)
#print(data)

def hanoi(n,start,temp,final):
   if n >0:
      hanoi(n-1,start,final,temp)
      final.append(start.pop())
      hanoi(n-1,final,temp,start)
      print(start,temp,final)
      return True
   else:
      return True



#n = 3
#start = [1,2,3]
#temp = []
#final = []
#hanoi (n,start,temp,final)
