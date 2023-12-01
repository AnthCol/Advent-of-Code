#include <bits/stdc++.h>

using namespace std; 

int main(void)
{ 
    ifstream fptr("input"); 
    string s; 
    int sum = 0; 

    unordered_map<string, int> umap; 
    umap.insert({"one", 1}); 
    umap.insert({"two", 2}); 
    umap.insert({"three", 3}); 
    umap.insert({"four", 4}); 
    umap.insert({"five", 5}); 
    umap.insert({"six", 6}); 
    umap.insert({"seven", 7}); 
    umap.insert({"eight", 8}); 
    umap.insert({"nine", 9}); 
    umap.insert({"1", 1}); 
    umap.insert({"2", 2}); 
    umap.insert({"3", 3}); 
    umap.insert({"4", 4}); 
    umap.insert({"5", 5}); 
    umap.insert({"6", 6}); 
    umap.insert({"7", 7}); 
    umap.insert({"8", 8}); 
    umap.insert({"9", 9}); 


    while (getline(fptr, s))
    {
        vector<int> digits; 

        int len = s.length(); 

        for (int i = 0; i < len; i++)
        {
            for (auto it = umap.begin(); it != umap.end(); it++)
            {
                if (s.compare(0, it->first.length(), it->first) == 0)
                {
                    digits.push_back(it->second); 
                    break;
                }
            }

            s.erase(0, 1); 
        } 

        sum += (10 * digits[0]) + digits[digits.size() - 1]; 
    }

    printf("%d\n", sum); 

    return 0; 
}

