def counting(arr,exp):
   count = [0]*len(arr)
   output = [0]*len(arr)
   #store count of occurances in count[]
   for i in range(0,len(arr)):
      idx = (arr[i]/exp)
      count[idx%10]+=1
   for i in range(0,len(arr)):
      count[i] +=count[i-1]
   i = len(arr) -1
   while i>=0:
      idx = (arr[i]/exp)
      output[count[idx%10]-1] = arr[i]
      count[idx%10] -=1
      i-=1
   i = 0
   for i in range(0,len(arr)):
      arr[i] = output[i]

def sortr(L):
   maxi = max(L)
   exp  = 1
   while maxi/exp >0:
      counting(L,exp)
      exp*=10


ls = [3,502,3413,54]
print(ls)
sortr(ls)
print(ls)
