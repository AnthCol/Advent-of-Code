#include <bits/stdc++.h>
using namespace std; 

int main(void){

    ifstream fptr("input"); 
    string s; 
    
    int sum = 0; 
    int id = 1; 
    int val; 
    int bad_flag; 
    char c; 

    while (getline(fptr, s)){
        
        s.erase(0, s.find(":") + 2);  
        bad_flag = 0; 
        
        vector<string> tokens; 
        char * t = strtok(const_cast<char*>(s.c_str()), ",; "); 
        while (t != nullptr)
        {
            tokens.push_back(string(t));  
            t = strtok(nullptr, ",; "); 
        }
        
        for (int i = 0; i < tokens.size(); i+=2)
        {
            val = stoi(tokens[i]); 
            c = tokens[i + 1][0]; 
            if ((c == 'r' && val > 12) ||
                (c == 'g' && val > 13) ||
                (c == 'b' && val > 14))
            {
                bad_flag = 1; 
                break; 
            }
        } 

       
        if (!bad_flag)
            sum += id; 
        id++; 
    }   
    
    printf("%d\n", sum); 

    return 0; 
}


