#include <stdio.h>
#include <stdlib.h>
typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
}HeapType;

int initHeap (HeapType *pHeap, int size){
   if (pHeap == NULL){
      return -1;
   }
   pHeap->size = size;
   pHeap->end = 0;
   pHeap->store = (int *)malloc(sizeof(int)*size);
   if (pHeap->store == NULL){
      return -1;
   }
   return 0;
}
int Helper(HeapType *pHeap, int **output, int*o_size, int root,int *next,int trav){
   if (trav == 1){
   /*1 == inorder*/
      if (2*root+1< *o_size){
         Helper(pHeap,output,o_size,2*root+1,next,trav);
         *next= *next+1;
      }
      (*output)[*next] = (pHeap->store)[root];
      if (2*root+2 <*o_size){
         *next= *next+1;
         Helper(pHeap,output,o_size,2*root+2,next,trav);
      }
      return 0;
   }
   else if (trav == 2){
   /*2 == preorder*/
      (*output)[*next] = (pHeap->store)[root];
      if (2*root+1 < *o_size){
         *next= *next+1;
          Helper(pHeap,output,o_size,2*root+1,next,trav);
      }
      if (2*root+2 <*o_size){
         *next= *next+1;
          Helper(pHeap,output,o_size,2*root+2,next,trav);
      }
      return 0;
   }     
   else if (trav == 3){ 
   /*3 == postorder*/
      if (2*root+1 < *o_size){
         Helper(pHeap,output,o_size,2*root+1,next,trav);
         *next= *next+1;
      }
      if (2*root+2 <*o_size){
         Helper(pHeap,output,o_size,2*root+2,next,trav);
         *next= *next+1;
      }
      (*output)[*next] = (pHeap->store)[root];
      return 0;
   }
   return -1;
}
   
   
int inorder (HeapType *pHeap, int **output, int *o_size){
   int root = 0;
   int next = 0;
   int trav = 1;
   if (pHeap == NULL){
      return -1;
   }
   if (output == NULL){
      return -1;
   }
   if (*output == NULL){
      *output = (int *)malloc(sizeof(int)*(pHeap->end));
      *o_size = pHeap->end;
   }
   if (*output == NULL){
      return -1;
   }
   //LNR 
   Helper(pHeap,output,o_size,root,&next,trav); 
   return 0;
}

//----------------------------------------preorder--------------------------------------//
int preorder (HeapType *pHeap, int **output, int *o_size){
   int trav = 2;
   int root = 0;
   int next = 0;
   if (pHeap == NULL){
      return -1;
   }
   if (output == NULL){
      return -1;
   }
   if (*output == NULL){
      *output = (int *)malloc(sizeof(int));
      *o_size = pHeap->end;
   }
   if (*output == NULL){
      return -1;
   }
   Helper(pHeap, output, o_size,root,&next,trav);
   //NLR
   return 0;
}
//----------------------------------------postorder--------------------------------------//

int postorder (HeapType *pHeap, int **output, int *o_size){
   int trav = 3;
   int root = 0;
   int next = 0;
   if (pHeap == NULL){
      return -1;
   }
   if (output == NULL){
      return -1;
   }
   *output = (int *)malloc(sizeof(int));
   if (*output == NULL){
      return -1;
   }
   //LRN
   Helper(pHeap,output,o_size,root,&next,trav);
   return 0;
}
//----------------------------------------------------------------------------------------//

int ReheapUp (HeapType *pHeap,int idx){
   // Put the next node in the next available spot
   // Push the new node upward, swapping with its parent 
   // until the new node reaches an acceptable location
   int temp=0;
   if ((pHeap->store)[(idx-1)/2] < (pHeap->store)[idx]){
      temp = (pHeap->store)[(idx-1)/2];
      (pHeap->store)[(idx-1)/2] = (pHeap->store)[idx];
      (pHeap->store)[idx] = temp;
      ReheapUp(pHeap,(idx-1)/2);
   }
   return 0;
}
   

int addHeap (HeapType *pHeap, int key){
   int temp[pHeap->end];
   int i =0;
   if (pHeap == NULL){
      return -1;
   }
   if (pHeap->end == pHeap->size){
      for (i=0;i<pHeap->end;i++){
         temp[i] = (pHeap->store)[i];
      }
      free(pHeap->store);
      pHeap->store = (int *)malloc(sizeof(int)*pHeap->size);
      for (i=0;i<pHeap->end;i++){
         (pHeap->store)[i] = temp[i];
      }
      pHeap->size= pHeap->size +1;
      
   }
   pHeap->end=pHeap->end +1;
   (pHeap->store)[pHeap->end] = key;
   ReheapUp(pHeap,(pHeap->end));
      
   return 0;
}
   
      
int findHeap (HeapType *pHeap, int key){
   int i;
   if (pHeap == NULL){
      return -1;
   }
   for (i=0;i<(pHeap->end);i++){
      if ((pHeap->store)[i] == key){
         return 1;
      }
   }
   return 0;
}

     

int delHeap (HeapType *pHeap, int *key){
   // Move the last node onto the root
   // Push the out-of-place node downward, swapping with its larger child
   // until the new node reaches an acceptable location
   int r;
   int rval;
   int i;
   if (pHeap == NULL){
      return -1;
   }
   r = findHeap (pHeap, *key);
   if (r != 1){
      return -1;
   }
   
   rval = (pHeap->store)[0];
   for (i = 0; i<(pHeap->end);i++){
      (pHeap->store)[i] = (pHeap->store)[i+1];
   }
   pHeap->end = pHeap->end -1;
   return rval;
}
   
   


int main(){
   HeapType *heap;
   int *out = NULL;
   int len = 0;
   int i = 0;
   int r;
   int key = 100;
   initHeap(heap,10);
   (heap->store)[0] = 100;
   (heap->store)[1] = 50;
   (heap->store)[2] = 25;
   (heap->store)[3] = 30;
   (heap->store)[4] = 20;
   (heap->store)[5] = 10;
   (heap->store)[6] = 5;
   (heap->store)[7] = 4;
   (heap->store)[8] = 3;
   (heap->store)[8] = 3;
   heap->end +=9;

   printf("BEFORE: end %d, size %d\n",heap->end,heap->size);

   inorder(heap,&out,&len);
   printf("-----------INORDER---------\n");
   for (i = 0;i<(heap->end);i++){
      printf("%d\n",out[i]);
   }

   printf("ADD 75\n");
   addHeap(heap,75);
   printf("AFTER: end %d, size %d\n",heap->end,heap->size);
   printf("ADDED\n");

   preorder(heap,&out,&len);
   printf("-----------PREORDER---------\n");
   for (i = 0;i<len;i++){
      printf("%d\n",out[i]);
   }
   postorder(heap,&out,&len);
   printf("-----------POSTORDER---------\n");
   for (i = 0;i<len;i++){
      printf("%d\n",out[i]);
   }
   printf("----------------------FIND------------------\n");
   r= findHeap(heap,30);
   printf("%d\n",r);
   printf("---------------------DELETE---------------\n");
   r = delHeap(heap,&key);
   printf("%d\n",r);
   return 0;
}

