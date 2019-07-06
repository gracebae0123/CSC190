#include <stdio.h>
#include <stdlib.h>
unsigned char FSR(unsigned char x) {
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   return r;
}


unsigned char prng(unsigned char x,unsigned char pattern){
   unsigned char oldbit0 = x&0x1;
   unsigned char r = x>>1;
   unsigned char newbit7 = oldbit0 <<7;
   r = r|newbit7;
   r = r^pattern;
   return r;
}

int crypt(char *data, unsigned int size, unsigned char password){
   int i =0;
   if (password == 0){
      return -1;
   }
   if (data == NULL | size == 0){
      return -1;
   }
   unsigned char prngval = password;
   for (i = 0; i<size;i++){
      prngval = prng(prngval, 0xb8);
      data[i] = data[i] ^ prngval;
   }
   return 0;
} 

   
int main(){
   unsigned char pattern = 0x08;
   unsigned char x = 0xF2;
   unsigned char test = prng(x,pattern);
   int i =0;
   printf("%x,\n",test);
   char data[5] = {'a','e','i','o','u'};
   int size = 5;
   unsigned char password = 0x8b;
   for (i=0;i<size;i++){
      printf("%c",data[i]);
   }
   int tst= crypt(data,size,password);
   for (i=0;i<size;i++){
      printf("%c",data[i]);
   }
   return 0;
}
   
