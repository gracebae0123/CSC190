#include <stdio.h>
#include <stdlib.h>
typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x, int y);
} intHeap_T;

int lt(int x, int y){
   if (x <y){
      return 1; }
   else{
      return 0;
   }
}
int gt(int x, int y){
   if (x>y){
      return 1;
   }
   else{
      return 0;
   }
}

int getParent(int n){
   return (n-1)/2;
}
int swap(intHeap_T* heap, int a, int b){
   int temp;
   if (heap == NULL){
      return -1;
   }
   if (heap->store == NULL){
      return -1;
   }
   if (a<0||(a>heap->size)){
      return -1;
   }
   if (b<0||(b>heap->size)){
      return -1;
   }
   temp = heap->store[a];
   heap->store[a] = heap->store[b];
   heap->store[b] = temp;
   return 0;
} 
   
int store(intHeap_T* heap, int value){
   int i =0;
   int idx = heap->end; 
   int parent;
   if (heap == NULL){
      return -1;
   }  
   if (heap->store == NULL){
      return -1;
   }
   if (heap->compare == NULL){
      return -1;
   }
   if (idx <= heap->size){
      parent = getParent(idx);
      heap->store[idx] = value;
      heap->end ++;
      while (heap->compare(heap->store[parent],heap->store[idx])==1){
         swap (heap,idx,parent);
         idx = parent;
         parent = getParent(idx);
      }
   } 
   return 0;
}

int retrieve(intHeap_T* heap, int *rvalue){
   int move = 1;
   int left = 0;
   int right = 0;
   int temp;
   int idx = 0;
   if ((heap == NULL) || (rvalue == NULL)){
      return -1;
   }
   if (heap->store == NULL){
      return -1;
   }
   if (heap-> compare == NULL){
      return -1;
   }
   *rvalue = heap->store[0];
   heap->store[0] = heap->store[heap->end-1];
   heap->end = heap->end -1;
   while (move == 1){
      move = 0;
      left = idx *2 +1;
      right = idx*2+2;
      if (left < heap->end){
         temp = left;
         if (right < heap->end){
            if (heap->compare(heap->store[left], heap->store[right])){
               temp = right;
            }
         }
         if (heap->compare(heap->store[idx],heap->store[temp])){
            swap(heap,idx,temp);
            idx = temp;
            move = 1;
         }
      }
   }
   return 0;
} 

int hs(int *x, int size, int (*compare)(int x, int y)){
   int i;
   intHeap_T heap;
   heap.store = (int *)malloc(size*sizeof(int));
   heap.size = size;
   heap.end = 0;
   heap.compare = compare;
   if (x == NULL){
      return -1;
   }
   for (i = 0; i<size; i++){
      store(&heap,x[i]);
   }
   for (i = 0; i<size;i++){
      retrieve(&heap,&(x[i]));
   }
   free (heap.store);
   return 0;
}  

//
//int main(void){
//  int i,j,rval;
//  int vals[] = {10,5,7,4,1,3,6,2,0,8};
//   rval = hs(vals,10,lt);
//   for (i=0;i<10;i++){
//      printf("%d ", vals[i]);
//   }
//   return 0;
//}
