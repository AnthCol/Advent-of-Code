#include <bits/stdc++.h>
using namespace std; 

int main(void)
{
    ifstream fptr("input"); 
    string s; 
    
    int flag = 0; 
    string token; 
    string temp; 
    long time; 
    long dist; 
    
    while (getline(fptr, s))
    {
        s.erase(0, s.find(":") + 1); 
         
        stringstream ss(s); 
        temp = ""; 

        while (ss >> token)
            temp += token; 
        
        (flag) ? (dist = stol(temp)) : (time = stol(temp)); 
         
        flag = 1; 
    }   

    long num_ways = 0; 

    for (long speed = 0; speed < time; speed++)
        if ((speed * (time - speed) >= dist))
            num_ways += 1; 

    printf("%ld\n", num_ways); 

    return 0; 
}

