#include <bits/stdc++.h>
using namespace std; 

vector<list<pair<string, int>>> table (256); 

void hash_func(string s)
{
    int hash_value = 0; 
    int i; 
    string label = "";

    for (i = 0; i < s.length(); i++)
    {
        if (s[i] == '=' || s[i] == '-')
            break;

        label += s[i]; 

        hash_value += int(s[i]); 
        hash_value *= 17; 
        hash_value %= 256; 
    }

    auto it = find_if(table[hash_value].begin(), table[hash_value].end(), [label](pair<string, int> p){ return p.first == label; }); 

    if (s[i] == '=')
    { 
        if (it == table[hash_value].end())
            table[hash_value].push_back({label, s[i + 1] - '0'}); 
        else
            it->second = s[i + 1] - '0'; 
    }
    else if (s[i] == '-' && it != table[hash_value].end()) 
        table[hash_value].erase(it); 


    return; 
}


int main(void)
{
    ifstream fptr("input"); 
    string s; 
    string file_data = ""; 

    while (getline(fptr, s))
        file_data += s; 
    
    char * token = strtok(const_cast<char*>(file_data.c_str()), ",\n"); 
    while (token != nullptr)
    {
        hash_func(string(token)); 
        token = strtok(nullptr, ",\n"); 
    }


    int sum = 0; 
    for (int i = 0, counter = 1; i < table.size(); i++, counter = 1)
        for (auto it = table[i].begin(); it != table[i].end(); it++, counter++)
            sum += (i + 1) * counter * it->second; 

    printf("%d\n", sum); 

    return 0; 
}

