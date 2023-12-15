#include <bits/stdc++.h>
using namespace std; 


vector<char> col_to_vec(vector<vector<char>>& board, int col_num)
{
    vector<char> v; 
    for (int i = 0; i < board.size(); i++)
        v.push_back(board[i][col_num]);  

    return v; 
}

int is_horizontal_reflection(vector<vector<char>>& board, int row_num)
{
    int above = row_num; 
    int below = row_num + 1; 

    if (below == board.size())
        return 0; 

    while (above >= 0 && below < board.size())
    {
        if (board[above] != board[below])
            return 0; 
        above--; 
        below++; 
    }
    
    return 1; 
}

int is_vertical_reflection(vector<vector<char>>&board, int col_num)
{
    int left = col_num; 
    int right = col_num + 1; 

    if (right == board[0].size())
        return 0; 

    while (left >= 0 && right < board[0].size())
    {
        if (col_to_vec(board, left) != col_to_vec(board, right))
            return 0; 
        left--;
        right++; 
    }

    return 1; 
}


void check_horizontal(vector<vector<char>>& board, vector<int>& rows)
{
    for (int i = 0; i < board.size(); i++)
    {
        if (is_horizontal_reflection(board, i))
        {
            rows.push_back(i + 1); 
            break; 
        }
    }
    return; 
}

void check_vertical(vector<vector<char>>& board, vector<int>& cols)
{
    for (int i = 0; i < board[0].size(); i++)
    {
        if (is_vertical_reflection(board, i))
        {
            cols.push_back(i + 1); 
            break;
        }
    }
    return; 
}


int main(void)
{
    ifstream fptr("input"); 
    string s; 

    vector<int> rows; 
    vector<int> cols; 

    while (getline(fptr, s))
    {
        vector<vector<char>> board;  
        do
        {
            vector<char> v (s.begin(), s.end()); 
            board.push_back(v); 
        } while (getline(fptr, s) && s.length() != 0); 

        check_horizontal(board, rows); 
        check_vertical(board, cols);  
    }   

    int sum = 0; 

    for (int r : rows)
        sum += 100 * r; 

    for (int c : cols)
        sum += c; 

    printf("%d\n", sum); 

    return 0; 
}

