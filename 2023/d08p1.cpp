#include <bits/stdc++.h>
using namespace std; 

int main(void)
{
    ifstream fptr("input"); 
    string s; 

    string instruction_list; 
    getline(fptr, instruction_list); 
    getline(fptr, s); 

    unordered_map<string, pair<string, string>> umap; 

    while (getline(fptr, s))
    {
        vector<string> tokens; 
        char * token = strtok(const_cast<char*>(s.c_str()), "()=, "); 
        while (token != nullptr)
        {
            tokens.push_back(string(token)); 
            token = strtok(nullptr, "()=, "); 
        }    
        umap[tokens[0]] = {tokens[1], tokens[2]}; 
    }   

    string key = "AAA"; 
    int total_steps = 0; 
    int instruction_index = 0; 
    int instruction_len = instruction_list.length(); 

    while (key != "ZZZ")
    {
        if (instruction_list[instruction_index] == 'L')
            key = umap[key].first; 
        else 
            key = umap[key].second;  
        
        instruction_index = (++instruction_index)%instruction_len; 
        total_steps += 1; 
    }

    printf("%d\n", total_steps); 

    return 0; 
}

