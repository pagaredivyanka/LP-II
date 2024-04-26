// AND,XOR HELLO WORLD 127
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main()
{
 char str[]="Hello World";
 char str1[11];
 char str2[11];
 int i,len;
 len = strlen(str);
 for(i=0;i<len;i++)
 {
str1[i] = str[i]&127;
printf("%c",str1[i]);
}
printf("\n");
for(i=0;i<len;i++)
{
int original, modified;
original = str[i];
modified = str[i]^127;
printf("i %d char %c orig %02x mod %02x\n", i, original, original, modified);
}
}
OUTPUT:
Hello World
i 0 char H orig 48 mod 37
i 1 char e orig 65 mod 1a
i 2 char l orig 6c mod 13
i 3 char l orig 6c mod 13
i 4 char o orig 6f mod 10
i 5 char orig 20 mod 5f
i 6 char W orig 57 mod 28
i 7 char o orig 6f mod 10
i 8 char r orig 72 mod 0d
i 9 char l orig 6c mod 13
i 10 char d orig 64 mod 1b
