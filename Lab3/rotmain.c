#include "avlrot.h"
#include<stdio.h>


int main(){
   int rval;
   avlNode *root = NULL;
   add_avl(&root,5);
   add_avl(&root,3);
   add_avl(&root,1);
   add_avl(&root,4);
   add_avl(&root,7);
   add_avl(&root,6);
   add_avl(&root,8);
   add_avl(&root,0);
   add_avl(&root,9);

//   rval = isAVL(&root);
//   printf("%d",rval);
//   rval = rotate(&root,1);
//   printf("%d",rval);
//   rval = dblrotate(&root,1);
//   printf("%d",rval);
   rval = rotate(&root,1);
   printf("IN ORDER\n");
   print_in_order(root);
   printf("LEVEL ORDER\n");
   print_in_level_order(root);
   printf("\n"); 
 
   rval = dblrotate(&root,1);
   printf("IN ORDER\n");
   print_in_order(root);
   printf("LEVEL ORDER\n");
   print_in_level_order(root);
   printf("\n"); 
   return 0;
}

