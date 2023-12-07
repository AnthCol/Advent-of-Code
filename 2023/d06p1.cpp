#include <bits/stdc++.h>
using namespace std; 

int main(void)
{
    ifstream fptr("input"); 
    string s; 
    
    int flag = 0; 
    string token; 
    vector<int> time; 
    vector<int> dist; 
    
    while (getline(fptr, s))
    {
        s.erase(0, s.find(":") + 1); 
         
        stringstream ss(s); 
        while (ss >> token)
        {
            int val = stoi(token); 
            (flag) ? dist.push_back(val) : time.push_back(val); 
        }

        flag = 1; 
    }   

    int product = 1;    

    for (int i = 0; i < time.size(); i++)
    {
        int num_ways = 0; 

        for (int speed = 0; speed < time[i]; speed++)
            if ((speed * (time[i] - speed) >= dist[i]))
                num_ways += 1; 

        product *= num_ways;  
    }

    printf("%d\n", product); 

    return 0; 
}

