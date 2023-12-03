#include <bits/stdc++.h>
using namespace std; 


typedef struct number_location
{
    int num; 
    vector<pair<int, int>> indices;  
} number_location; 

typedef struct symbol_location
{
    int row, column; 
} symbol_location; 


int is_surrounding(pair<int, int> n_loc, symbol_location s_loc)
{
    int n_row = n_loc.first; 
    int n_col = n_loc.second; 
    int s_row = s_loc.row; 
    int s_col = s_loc.column; 
    // to the right
    if (n_row == s_row && n_col == s_col + 1)
        return 1;
    // to the left 
    if (n_row == s_row && n_col == s_col - 1)
        return 1; 
    // above
    if (n_row == s_row + 1 && n_col == s_col)
        return 1; 
    // below
    if (n_row == s_row - 1 && n_col == s_col)
        return 1; 
    // top left
    if (n_row == s_row + 1 && n_col == s_col - 1)
        return 1; 
    // top right
    if (n_row == s_row + 1 && n_col == s_col + 1)
        return 1; 
    // bottom left
    if (n_row == s_row - 1 && n_col == s_col - 1)
        return 1; 
    // bottom right
    if (n_row == s_row - 1 && n_col == s_col + 1)
        return 1; 

    return 0; 
}


int main(void){

    ifstream fptr("input"); 
    string s; 
    int sum = 0; 
    int row_counter = 0; 
    vector<number_location> n_locs;  
    vector<symbol_location> s_locs; 

    while (getline(fptr, s)){ 
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == '*')
            {
                symbol_location sl; 
                sl.row = row_counter; 
                sl.column = i; 
                s_locs.push_back(sl); 
            }
            int loop_taken = 0; 
            number_location nl; 
            string temp = ""; 
            vector<pair<int, int>> indices; 
            while (isdigit(s[i]))
            {
                loop_taken = 1; 
                indices.push_back({row_counter, i}); 
                temp += s[i];  
                i++; 
            }

            if (loop_taken)
            { 
                nl.num = stoi(temp); 
                nl.indices = indices; 
                n_locs.push_back(nl); 
                i--; 
            }
        }
        row_counter += 1; 
    }   

    
    for (int i = 0; i < s_locs.size(); i++)
    {
        vector<int> adj; 
        
        for (int j = 0; j < n_locs.size(); j++)
        {
            for (int x = 0; x < n_locs[j].indices.size(); x++)
            { 
                if (is_surrounding(n_locs[j].indices[x], s_locs[i]))
                {
                    adj.push_back(n_locs[j].num); 
                    break; 
                }
            }
        }  
        
        if (adj.size() == 2)
        {
            sum += (adj[0] * adj[1]);   
        }
    }
    
    printf("%d\n", sum); 

    return 0; 
}

