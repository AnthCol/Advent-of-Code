#include <bits/stdc++.h>
using namespace std; 

vector<vector<char>> board; 
vector<pair<int, int>> point_list; 


bool blank_row(vector<char> v)
{
    for (char c : v)
        if (c != '.')
            return false; 
    return true; 
}

void column()
{
    vector<int> blank_column_indices; 
    for (int i = 0; i < board[0].size(); i++)
    {
        int blank_flag = 1; 
        for (int j = 0; j < board.size(); j++)
        {
            if (board[j][i] == '#')
            {
                blank_flag = 0; 
                break; 
            }
        }

        if (blank_flag)
            blank_column_indices.push_back(i); 
    }

    vector<vector<char>> updated; 

    for (int i = 0; i < board.size(); i++)
    {
        vector<char> temp; 
        for (int j = 0; j < board[0].size(); j++)
        {
            temp.push_back(board[i][j]); 
            if (find(blank_column_indices.begin(), blank_column_indices.end(), j) != blank_column_indices.end())
                temp.push_back('.'); 
        }
        updated.push_back(temp); 
    }

    board = updated;  
    return; 
}

void find_points()
{
    for (int i = 0; i < board.size(); i++)
        for (int j = 0; j < board[0].size(); j++)
            if (board[i][j] == '#')
                point_list.push_back({i, j}); 
    return; 
}

void point_permutations(set<pair<int, int>>& point_list_indices)
{
    for (int i = 0; i < point_list.size(); i++)
        for (int j = 0; j < point_list.size(); j++)
            if (i != j) 
                point_list_indices.insert((i < j) ? make_pair(i, j) : make_pair(j, i)); 
    return; 
}

inline int shortest_path(pair<int, int> a, pair<int, int> b)
{
    return abs(a.first - b.first) + abs(a.second - b.second); 
}


int main(void)
{
    ifstream fptr("input"); 
    string s; 

    while (getline(fptr, s))
    {
        vector<char> temp; 
        for (char c : s)
            temp.push_back(c); 

        board.push_back(temp);             

        if (blank_row(temp))
            board.push_back(temp); 
    }   

    column(); 

    find_points();

    set<pair<int, int>> point_list_indices;
    point_permutations(point_list_indices); 
 

    int sum = 0; 
    for (pair<int, int> point : point_list_indices)
        sum += shortest_path(point_list[point.first], point_list[point.second]); 
    printf("%d\n", sum); 

    return 0; 
}

