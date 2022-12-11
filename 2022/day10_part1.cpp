#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    
    int reg = 1; 
    int result = 0; 
    int cycles = 0; 

    int special_cycles[] = {20, 60, 100, 140, 180, 220}; 
    int special_cycle_index = 0; 

    while (getline(fptr, s)){
        if (s.substr(0, 4) == "noop"){
            cycles++; 
            if (cycles == special_cycles[special_cycle_index]){
                result += (special_cycles[special_cycle_index] * reg); 
                special_cycle_index++; 
                if (special_cycle_index > 5) break; 
            }
        }
        else{
            cycles++; 
            if (cycles == special_cycles[special_cycle_index]){
                result += (special_cycles[special_cycle_index] * reg); 
                special_cycle_index++; 
                if (special_cycle_index > 5) break; 
            }
            cycles++;
            if (cycles == special_cycles[special_cycle_index]){
                result += (special_cycles[special_cycle_index] * reg); 
                
                special_cycle_index++; 
                if (special_cycle_index > 5) break; 
            }
            reg += stoi(s.substr(5, 100));
        }

        

        
    }   

    printf("%d\n", result); 



    return 0; 
}