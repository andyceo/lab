#include <stdio.h>
#include <stdlib.h>
//#include <conio.h>

typedef struct{
  int k;
  void *p;
} MY_TYPE;

int main(){
    int *p;
    int a = 7;
    void *np;
    
    system("skype");
    
    p = &a;
    printf("%p , %d, %d, %d \n \n", p, *p, sizeof(int), sizeof(MY_TYPE));
    //getch();
    
    
    
    int *p1, *p2;
    int ar[5] = {2, 7, 8, 12, 6};
    p1 = ar;
    p2 = p1 + 100;
    printf("%d, %d", *p1, *p2);
    return 0;
}
