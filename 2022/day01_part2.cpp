#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("day01_part1_input.txt", "r"); 
    char * string = (char*)malloc(sizeof(char) * 10); 

    int count = 0; 
    vector<int> elves; 
   
    while (!feof(fptr)){
        fgets(string, 10, fptr); 
        if (string[0] == '\n'){
            elves.pb(count); 
            count = 0; 
        }
        else{
            string[strlen(string) - 1] = '\0'; 
            count += atoi(string);
        }
    }

    sort(elves.begin(), elves.end()); 

    printf("printing max: %d\n", elves[elves.size()-1] + elves[elves.size()-2] + elves[elves.size()-3]); 

    fclose(fptr); 
    free(string); 

    return 0; 
}