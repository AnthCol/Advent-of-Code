#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("input.txt", "r"); 
    char * string = (char*)malloc(sizeof(char) * 10000); 
    int index = 0; 
    
    char one, two; 
    int score = 0; 
    
    while (!feof(fptr)){
        fscanf(fptr, "%c %c ", &one, &two); 

        if (two == 'X'){
            two = 'A';  // rock
            score++; 
        }
        else if (two == 'Y'){
            two = 'B';  // paper 
            score += 2; 
        }
        else if (two == 'Z'){
            two = 'C';  // scissors 
            score += 3; 
        }

        if (one == two) score += 3; 
        else if (!(one == 'A' && two == 'C')
                && !(one == 'B' && two == 'A')
                && !(one == 'C' && two == 'B')) score += 6; 

    }

    printf("%d\n", score); 


    fclose(fptr); 
    free(string); 


    return 0; 
}