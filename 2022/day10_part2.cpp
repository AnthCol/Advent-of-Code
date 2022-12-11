#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    
    int reg = 1; 
    int cycles = 0; 
 
    char crt [240]; 

    while (getline(fptr, s)){
        if (s.substr(0, 4) == "noop"){
            cycles++; 

            if (reg - 1 == ((cycles-1)%40) || ((cycles-1)%40) == reg || ((cycles-1)%40) == reg + 1) crt[cycles - 1]= '#'; 
            else crt[cycles - 1] = '.'; 
        }
        else{
            cycles++; 
        
            if (reg - 1 == ((cycles-1)%40) || ((cycles-1)%40) == reg || ((cycles-1)%40) == reg + 1) crt[cycles - 1] = '#'; 
            else crt[cycles - 1] = '.'; 

            cycles++;
        
            if (reg - 1 == ((cycles-1)%40) || ((cycles-1)%40) == reg || ((cycles-1)%40) == reg + 1) crt[cycles - 1] = '#'; 
            else crt[cycles - 1] = '.'; 

            reg += stoi(s.substr(5, 100));
        }

    }   

    for (int i = 0; i < 240; i++){
        printf("%c", crt[i]); 
        if ((i+1)%40 == 0) printf("\n"); 
    }

    return 0; 
}