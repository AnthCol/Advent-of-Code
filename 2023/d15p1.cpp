#include <bits/stdc++.h>
using namespace std; 

int hash_func(string s)
{
    int hash_value = 0; 

    for (char c : s)
    {
        hash_value += int(c); 
        hash_value *= 17; 
        hash_value %= 256; 
    }

    return hash_value; 
}


int main(void)
{
    ifstream fptr("input"); 
    string s; 
    string file_data = ""; 

    while (getline(fptr, s))
        file_data += s; 
    
    int sum = 0; 
    
    char * token = strtok(const_cast<char*>(file_data.c_str()), ",\n"); 
    while (token != nullptr)
    {
        sum += hash_func(string(token)); 
        token = strtok(nullptr, ",\n"); 
    }

    printf("%d\n", sum); 

    return 0; 
}

