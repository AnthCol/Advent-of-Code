#include <bits/stdc++.h>
using namespace std; 

int main(void){

    ifstream fptr("input"); 
    string s; 
    
    int sum = 0; 
    int id = 1; 

    while (getline(fptr, s)){
        
        s.erase(0, s.find(":") + 2);  
        
        vector<string> tokens; 
        char * t = strtok(const_cast<char*>(s.c_str()), ",; "); 
        while (t != nullptr)
        {
            tokens.push_back(string(t));  
            t = strtok(nullptr, ",; "); 
        }
        
        int max_r = INT_MIN; 
        int max_g = INT_MIN; 
        int max_b = INT_MIN; 

        for (int i = 0; i < tokens.size(); i+=2)
        {
            int val = stoi(tokens[i]); 
            char c = tokens[i + 1][0];     
            if (c == 'r' && val > max_r)      max_r = val; 
            else if (c == 'g' && val > max_g) max_g = val; 
            else if (c == 'b' && val > max_b) max_b = val; 
        } 

        sum += (max_r * max_g * max_b); 
       
        id++; 
    }   
    
    printf("%d\n", sum); 

    return 0; 
}


