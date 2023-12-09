#include <bits/stdc++.h>
using namespace std; 

bool all_zeros(vector<int>& v)
{
    for (int num : v)
        if (num != 0)
            return false; 
    return true; 
}

int main(void)
{
    ifstream fptr("input"); 
    string s; 
    int sum = 0; 

    while (getline(fptr, s))
    {
        vector<vector<int>> nums;
        vector<int> temp; 

        stringstream ss(s); 
        while (ss >> s)
            temp.push_back(stoi(s));  
        nums.push_back(temp); 

        for (int i = 0; i < nums.size(); i++)
        {
            temp.clear(); 
            for (int j = 0; j < nums[i].size() - 1; j++)
                temp.push_back(nums[i][j + 1] - nums[i][j]);  
            nums.push_back(temp); 

            if (all_zeros(temp))
                break; 
        }

        for (int i = 0; i < nums.size(); i++)
            reverse(nums[i].begin(), nums[i].end()); 

        nums[nums.size() - 1].push_back(0); 

        for (int i = nums.size() - 2; i >= 0; i--)
            nums[i].push_back(nums[i][nums[i].size() - 1] - nums[i + 1][nums[i + 1].size() - 1]); 

        sum += nums[0][nums[0].size() - 1];   
    }   

    cout << sum << endl; 

    return 0; 
}

