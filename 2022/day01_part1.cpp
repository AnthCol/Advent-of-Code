#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("day01_part1_input.txt", "r"); 
    char * string = (char*)malloc(sizeof(char) * 10); 

    int count = 0; 
    int max = -1; 

    while (!feof(fptr)){
        fgets(string, 10, fptr); 
        if (string[0] == '\n'){
            if (count > max) max = count; 
            count = 0; 
        }
        else{
            count += atoi(string);
            string[strlen(string) - 1] = '\0'; 
        }
    }

    printf("printing max: %d\n", max); 

    fclose(fptr); 
    free(string); 

    return 0; 
}