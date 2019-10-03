#include <stdio.h>
#include <stdlib.h>

/*stack = last in first out */

struct intlist {
   int *x;
   int end;
   int len;
};
typedef struct intlist intlist;



int init(intlist *l,int len) {
   if (l==NULL) { return -1; }
   (l->x) = (int *)malloc(len * sizeof(int));
   if ((l->x) == NULL) { return -1; }
 
   l->end = -1;
   l->len=len;
 
   return 0;
}

int push(intlist *l, int val){
   l->end = (l->end) + 1;
   (l->x)[(l->end)] = val;
   return 0;
}

int pop(intlist *l){
   if(l->end == -1){
      printf("ERROR\n");
      return -1;
   }
   l->len = (l->len) -1;
   return 0;
}


/*int main(){
   intlist *l = NULL;
   init(intlist *l, 10);
   push(intlist *l, 1);
   push(intlist *l, 2);
   push(intlist *l, 3);
   push(intlist *l, 4);
   push(intlist *l, 5);
   pop(intlist *l);
   pop(intlist *l);

   return 0;
}
*/
