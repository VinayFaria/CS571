#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc !=2) {
        printf("Usage: StringProcess string\n");
        return (-1);
    }
    printf("%s %d\n",argv[1],strlen(argv[1]));
    return 0;
}