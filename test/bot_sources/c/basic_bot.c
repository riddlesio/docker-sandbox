#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>


int main(void) {
    char    line[16384];

    while(fgets(line, 16384, stdin) != NULL) {
        if (strncmp(line, "action", 6) == 0) {
            int randNumb = rand() % 3;
            if(randNumb == 0) {
                fprintf(stdout, "rock\n");
            }
            if(randNumb == 1) {
                fprintf(stdout, "paper\n");
            }
            if(randNumb == 2) {
                fprintf(stdout, "scissors\n");
            }
			fflush(stdout);
            continue;
        }
    }

    return 0;
}
