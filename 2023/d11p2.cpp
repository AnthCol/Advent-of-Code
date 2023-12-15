#include <bits/stdc++.h>
using namespace std; 

vector<vector<char>> board; 
vector<pair<int, int>> point_list; 
vector<int> blank_columns; 
vector<int> blank_rows; 

bool blank_row(vector<char> v)
{
    for (char c : v)
        if (c != '.')
            return false; 
    return true; 
}

void columns()
{
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
            blank_columns.push_back(i); 
    }
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

int shortest_path(pair<int, int> a, pair<int, int> b)
{
    int min_row = (a.first < b.first) ? a.first : b.first; 
    int max_row = (a.first > b.first) ? a.first : b.first;
    int min_col = (a.second < b.second) ? a.second : b.second; 
    int max_col = (a.second > b.second) ? a.second : b.second; 

    int added_movements = 0; 

    for (int i = 0; i < blank_rows.size(); i++)
        if (min_row < blank_rows[i] && max_row > blank_rows[i])
            added_movements += 999999; 

    for (int i = 0; i < blank_columns.size(); i++)
        if (min_col < blank_columns[i] && max_col > blank_columns[i])
            added_movements += 999999;  

    return added_movements + abs(a.first - b.first) + abs(a.second - b.second); 
}


int main(void)
{
    ifstream fptr("input"); 
    string s; 

    int row_index = 0; 
    while (getline(fptr, s))
    {
        vector<char> temp; 
        for (char c : s)
            temp.push_back(c); 

        board.push_back(temp);             

        if (blank_row(temp))
            blank_rows.push_back(row_index); 

        row_index += 1; 
    }   

    columns(); 
    find_points();

    set<pair<int, int>> point_list_indices;
    point_permutations(point_list_indices); 

    unsigned long long int sum = 0; 
    for (pair<int, int> point : point_list_indices)
        sum += shortest_path(point_list[point.first], point_list[point.second]); 
    printf("%llu\n", sum); 

    return 0; 
}

