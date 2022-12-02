#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("input.txt", "r"); 
    char * string = (char*)malloc(sizeof(char) * 10000); 
    int index = 0; 
    
    char one, two; 
    int score = 0; 
    // 1 = rock, 2 = paper, 3 = scissors 
    // A         B          C
    while (!feof(fptr)){
        fscanf(fptr, "%c %c ", &one, &two); 
        
        if (two == 'X'){ // loss 
            if (one == 'A') score += 3; 
            else if (one == 'B') score += 1; 
            else score+=2; 
        }
        else if (two == 'Y'){ // draw
            if (one == 'A') score += 1 + 3; 
            else if (one == 'B') score += 2 + 3; 
            else score += 6; 
        }
        else if (two == 'Z'){ // win
            if (one == 'A') score += 2 + 6; 
            else if (one == 'B') score += 3 + 6; 
            else score += 1 + 6; 
        }
    }

    printf("%d\n", score); 


    fclose(fptr); 
    free(string); 


    return 0; 
}