#include <stdio.h>
int bs(int *x,int size, int (*compare)(int x,int y));
int lt(int x, int y);
int gt(int x, int y);
//int main(void){
//   int i = 0;
//   int vals[10];
//   int rval;
//   for(i=0;i<10;i++){
//      vals[i] = 100-i;
//   }
//   for (i=0;i<10;i++){
//      printf("in[%d]=%d\n",i,vals[i]);
//   }
//   /*HERE: call bs() with the appropriate comparison function */
//   rval = bs(vals,10,lt); 
//   for (i=0;i<10;i++){
//      printf("out[%d]=%d\n",i,vals[i]);
//   }
//   return 0;
//}

int bs(int *x,int size, int (*compare)(int x,int y)){
   int i;
   int j;
   int swapped=0;
   int temp;
   if (size <1){
      return -1;
   }
   if (x == NULL){
      return -1;
   }

   for (i =0;i<size;i++){
      for (j=0;j<size;j++){
         if ((*compare)(x[i],x[j])==1){
            temp = x[i];
            x[i] = x[j];
            x[j] = temp;
            swapped = 1;
         }
      }
   }
   if (swapped == 0){
      return -1;
   }
   return 0;
} 

int lt(int x, int y){
   if (x <y){
      return 1;
   }
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
