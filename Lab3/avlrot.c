#include <stdio.h>
#include <stdlib.h>
#include "avlrot.h"

int print_in_order(avlNode *root){
//   printf("DEBUG: INORDER\n");
   if (root == NULL){
      return -1;
   }
   print_in_order(root->l);
   printf("%d\n",root->val);
   print_in_order(root->r);
   return 0;
}

int height(avlNode *root){
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


int print_at_level(avlNode *root, int level){
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

int print_in_level_order(avlNode *root){
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

//-----------------------------------------------------------------------------//

int hdiff(avlNode *root){
   int left = height(root->l);
   int right = height(root->r);
   int rval;
   rval = left - right;
   return rval;
}


int isAVL(avlNode **root){
   int rval;
   /* avl tree if hdiff == -1//0//1 */
   if (root == NULL){
      return -1;
   }
   rval = hdiff(*root);
   if ((rval != -1) && (rval != 0) &&(rval != 1)){
      return -1;
   }
   else{
      return 0;
   }
}


int rotate(avlNode **root, unsigned int Left0_Right1){
   /* rotate the tree defined by root+pivot in the direction defined by Left0Right1 */
   avlNode *temp;
   if (root == NULL){
      return -1;
   }
   if (*root == NULL){
      return -1;
   }
   if(Left0_Right1 == 0){
      if ((*root)->r == NULL){
         return -1;
      }
      temp = (*root)->r;
      (*root)->r = temp->l;
      temp->l = *root;
      *root = temp;
      (*root)->balance = hdiff(*root);
      return 0;
   }
   else if (Left0_Right1 == 1){
      if ((*root)->l == NULL){
         return -1;
      }
      temp = (*root)->l;
      (*root)->l = temp->r;
      temp->r = *root;
      *root = temp;
      (*root)->balance = hdiff(*root);
      return 0;
   }
   return -1;
}

   
int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1){
   if (root == NULL){
      return -1;
   }
   if (*root == NULL){
      return -1;
   }
   if (MajLMinR0_MajRMinL1 == 0){
      if((*root)->r == NULL){
         return -1;
      }
      rotate(&((*root)->r),1);  
      rotate(root,0);
      return 0;
   }
   else if (MajLMinR0_MajRMinL1 == 1){
      if((*root)->l == NULL){
         return -1;
      }
      rotate(&((*root)->l),0);  
      rotate(root,1);
      return 0;
   }
   return -1;
}

int add_avl(avlNode **root, int val){
   avlNode *node = (*root);
//   printf("DEBUG: ADD(1)\n");

   if (root == NULL){
      return -1;
   }
//   printf("DEBUG: ADD(2)\n");
   if (*root == NULL){
//      printf("DEBUG: ADD(3-1)\n");
      *root = (avlNode *)malloc(sizeof(avlNode)); 
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
//      printf("DEBUG: ADD(3-2)\n");
    }
    else{
      if (val < (*root)->val){
        if ((*root)->l == NULL){
           (*root)->l = (avlNode*)malloc(sizeof(avlNode));
           (*root)->l->val = val; 
           (*root)->l->l = NULL;
           (*root)->l->r = NULL;
//            printf("DEBUG: ADD(4)\n");
           return 0;
        }
        return add_avl((&(*root)->l),val);
      } 
      else if (val > (*root)->val){
        if ((*root)->r == NULL){
           (*root)->r = (avlNode*)malloc(sizeof(avlNode));
           (*root)->r->val = val; 
           (*root)->r->l = NULL;
           (*root)->r->r = NULL;
//           printf("DEBUG: ADD(4)\n");
           return 0;
        }
        return add_avl((&(*root)->r),val);
      }
    }
   return 0;
}

/*   
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
   
   rval = rotate(&root,1);
   printf("IN ORDER\n");
   print_in_order(root);
   printf("LEVEL ORDER\n");
   print_in_level_order(root);
   
   rval = dblrotate(&root,1);
   printf("IN ORDER\n");
   print_in_order(root);
   printf("LEVEL ORDER\n");
   print_in_level_order(root);
   
   return 0;
}


*/
