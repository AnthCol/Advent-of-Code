#include <bits/stdc++.h>
using namespace std; 

#define NUM_ATTRIBUTES 8
#define MAP_SIZE 3
#define SEED 0
#define SOIL 1
#define FERT 2
#define WATER 3
#define LIGHT 4
#define TEMP 5
#define HUMID 6
#define LOC 7

int main(void)
{

    ifstream fptr("input"); 
    string s;    
    string token; 
    int index = SEED;  

    vector<vector<long>> plant_info; 

    getline(fptr, s); 
    s.erase(0, s.find(":") + 2); 
    stringstream ss(s); 
    while (ss >> token)
    {
        vector<long> v (NUM_ATTRIBUTES, -1); 
        v[index] = stol(token); 
        plant_info.push_back(v); 
    } 

    while (getline(fptr, s))
    {
        if (s.length() < 2)
            continue; 

        if (s.find(":") != string::npos)
        { 
            for (int i = 0; i < plant_info.size(); i++)
                if (plant_info[i][index] == -1)
                    plant_info[i][index] = plant_info[i][index - 1];                 

            index += 1;           
            continue; 
        }

 
        stringstream ss(s); 
        ss >> token; 
        long dest_start = stol(token); 
        ss >> token; 
        long src_start = stol(token); 
        ss >> token; 
        long range_size = stol(token);         
        long src_end = src_start + range_size; 

        for (int i = 0; i < plant_info.size(); i++)
        {
            long val = plant_info[i][index - 1]; 
            if (val >= src_start && val < src_end)
            {
                plant_info[i][index] = dest_start + (val - src_start); 
            }
        }
    }   
    
    unsigned long long int ans = INT_MAX; 
    for (int i = 0; i < plant_info.size(); i++)
    {
        if (plant_info[i][LOC] == -1)
            plant_info[i][LOC] = plant_info[i][LOC - 1]; 

        if (plant_info[i][LOC] < ans)
            ans = plant_info[i][LOC]; 
    }

    cout << ans << endl;  

    return 0; 
}

