#include <stdio.h>

int main()
{
    int c;

    printf("Ordinary Loop:\n");
    while ((c = getchar()) != EOF) {
        putchar(c);
    }

    printf("Loginc Loop:\n");
    while (c = (getchar() != EOF)) { // ???
        putchar(c);
    }

    printf("EOF = %d", c);

    return 0;
}
