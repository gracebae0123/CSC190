struct bstNode{
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

int print_in_order(bstNode *root);
int height(bstNode *root);
int print_at_level(bstNode *root, int level);
int print_in_level_order(bstNode *root);

