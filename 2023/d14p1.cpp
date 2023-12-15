#include <bits/stdc++.h>
using namespace std; 

void tilt(vector<vector<char>>& board)
{
    for (int i = 0; i < board[0].size(); i++)
    {
        for (int j = 0; j < board.size(); j++)
        {
            if (board[j][i] == 'O')
            {
                board[j][i] = '.'; 
                // found a rock, iterate back upwards of the column until the last available . 
                int z; 
                for (z = j - 1; z >= 0; z--)
                    if (board[z][i] == 'O' || board[z][i] == '#')
                        break; 
                board[z + 1][i] = 'O'; 
            }
        }
    }
    return;
}

int calc(vector<vector<char>>& board)
{
    int sum = 0; 
    for (int i = 0; i < board.size(); i++)
        for (int j = 0; j < board[0].size(); j++)
            if (board[i][j] == 'O')
                sum += board.size() - i; 
    return sum; 
}

int main(void)
{
    ifstream fptr("input"); 
    string s; 

    vector<vector<char>> board; 

    while (getline(fptr, s))
    {
        vector<char> v (s.begin(), s.end()); 
        board.push_back(v); 
    }   

    tilt(board); 
    printf("%d\n", calc(board)); 
    return 0; 
}

