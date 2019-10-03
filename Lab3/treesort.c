#include <stdio.h>
#include<stdlib.h>
#include "treesort.h"

int print_in_order(bstNode *root){
//   printf("DEBUG: INORDER\n");
   if (root == NULL){
      return -1;
   }
   print_in_order(root->l);
   printf("%d\n",root->val);
   print_in_order(root->r);
   return 0;
} 

int height(bstNode *root){
   int left;
   int right;
   if (root == NULL){
      return 0;
   }
   else{
      left = height(root->l);
      right = height(root->r);
      if (left > right){
         return (left+1);
      }  
      else{
         return (right+1);
      }
   }
}
      

int print_at_level(bstNode *root, int level){
//   printf("DEBUG: AT LEVEL\n");
   if (root == NULL){
      return -1;
   }
   if (level == 1){
      printf("%d ",root->val);
   }
   else if (level >1){
      print_at_level(root->l, level-1);
      print_at_level(root->r, level-1);
   }
   return 0;

}  

int print_in_level_order(bstNode *root){
   int length = height(root);
   int i;
   if (root == NULL){
      return -1;
   }
   for (i=1; i<=length;i++){
      print_at_level(root, i);
   }
   return 0;    
}
   
 


int add_bst(bstNode **root, int val){
   bstNode *node = (*root);
//   printf("DEBUG: ADD(1)\n");

   if (root == NULL){
      return -1;
   }
//   printf("DEBUG: ADD(2)\n");
   if (*root == NULL){
//      printf("DEBUG: ADD(3-1)\n");
      *root = (bstNode *)malloc(sizeof(bstNode)); 
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
//      printf("DEBUG: ADD(3-2)\n");
    }
    else{
      if (val < (*root)->val){
        if ((*root)->l == NULL){
           (*root)->l = (bstNode*)malloc(sizeof(bstNode));
           (*root)->l->val = val; 
           (*root)->l->l = NULL;
           (*root)->l->r = NULL;
//            printf("DEBUG: ADD(4)\n");
           return 0;
        }
        return add_bst((&(*root)->l),val);
      } 
      else if (val > (*root)->val){
        if ((*root)->r == NULL){
           (*root)->r = (bstNode*)malloc(sizeof(bstNode));
           (*root)->r->val = val; 
           (*root)->r->l = NULL;
           (*root)->r->r = NULL;
//          printf("DEBUG: ADD(4)\n");
           return 0;
        }
        return add_bst((&(*root)->r),val);
      }
    }
   return 0;
}
   


//int main(void){
//   int n =0;
//   int rval=0;
//   int value=0;
//   bstNode *root=NULL;
//   add_bst(&root,5);
//   add_bst(&root,3);
//   add_bst(&root,1);
//   add_bst(&root,4);
//   add_bst(&root,7);
//   add_bst(&root,6);
//   add_bst(&root,8);
//   print_in_order(root);
//   print_in_level_order(root);


//   printf("%d",height(root));
//----------------------------------------//
//   while (scanf("%d",&value) != EOF){
//      n++;
//      add_bst(&root,value);
//   }
//   printf("INPUT: %d\n",n);
//   rval = print_in_level_order(root);
//   if (rval != 0){
//      printf("ERROR: PRINT_LEVEL_ORDER\n");
//   }
//   rval = print_in_order(root);
//   if (rval != 0){
//      printf("ERROR: PRINT_IN_ORDER\n");
//   }
   return 0;
//   
}
 
         

