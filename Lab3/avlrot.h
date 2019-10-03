#include <stdio.h>
#include <stdlib.h>
struct avlNode{
   int balance; /* -1 Left, 0 balanced, +1 right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

int print_in_order(avlNode *root);
int height(avlNode *root);
int print_at_level(avlNode *root, int level);
int print_in_level_order(avlNode *root);

int hdiff(avlNode *root);
int isAVL(avlNode **root);
int rotate(avlNode **root, unsigned int Left0_Right1);
int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1);
int add_avl(avlNode **root, int val);


