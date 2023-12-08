#include <bits/stdc++.h>
using namespace std; 


int is_prime_factor(int potential_prime_factor, int num)
{
    if (num%potential_prime_factor != 0)
        return 0; 

    int num_factors = 0; 

    for (int i = 1; i <= potential_prime_factor; i++)
        num_factors += (potential_prime_factor%i == 0); 

    return (num_factors == 2);
}




int main(void)
{
    ifstream fptr("input"); 
    string s; 

    string instruction_list; 
    getline(fptr, instruction_list); 
    getline(fptr, s); 

    unordered_map<string, pair<string, string>> umap; 
    vector<string> keys; 

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

        if (tokens[0][tokens[0].length() - 1] == 'A')
            keys.push_back(tokens[0]); 

    }   

    vector<int> path_lengths; 

    for (int i = 0; i < keys.size(); i++)
    {
        int steps = 0; 
        int instruction_index = 0;

        while (keys[i][keys[i].length() - 1] != 'Z')
        {
            if (instruction_list[instruction_index] == 'L')
                keys[i] = umap[keys[i]].first; 
            else
                keys[i] = umap[keys[i]].second; 
            
            instruction_index = (++instruction_index)%instruction_list.length(); 
            steps += 1; 
        } 
        path_lengths.push_back(steps);  
    }

    set<int> prime_factors; 
    for (int i = 0; i < path_lengths.size(); i++)
    {
        for (int j = 1; j < path_lengths[i]; j++)
            if (is_prime_factor(j, path_lengths[i]))
                prime_factors.insert(j); 
    }

    long lcm = 1; 
    for (auto element : prime_factors)
        lcm *= element; 

    cout << lcm << endl; 

    return 0; 
}

