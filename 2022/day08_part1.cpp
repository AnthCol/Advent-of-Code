#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int check_north(vector<vector<int>> map, int row, int column){
    for (int i = 0; i < row; i++){
        if (map[i][column] >= map[row][column]) return 0; 
    }
    return 1; 
}
int check_south(vector<vector<int>> map, int row, int column){
    for (int i = (int)map.size() - 1; i > row; i--){
        if (map[i][column] >= map[row][column]) return 0; 
    }
    return 1; 
}
int check_west(vector<vector<int>> map, int row, int column){
    for (int i = 0; i < column; i++){
        if (map[row][i] >= map[row][column]) return 0; 
    }
    return 1; 
}
int check_east(vector<vector<int>> map, int row, int column){
    for (int i = (int)map[0].size() - 1; i > column; i--){
        if (map[row][i] >= map[row][column]) return 0; 
    }
    return 1; 
}

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    vector<int> vec; 

    int sum = 0; 
    vector<vector<int>> map; 
    vector<int> temp; 
    while (getline(fptr, s)){
        for (int i = 0; i < (int)s.length(); i++){
            temp.pb((int)s.at(i) - 48);
        }
        map.pb(temp); 
        temp.clear(); 
    }   

    for (int i = 0; i < (int)map.size(); i++){
        for (int x = 0; x < (int)map[i].size(); x++){
            if (check_north(map, i, x) || check_south(map, i, x) || check_east(map, i, x) || check_west(map, i, x)) sum++; 
        }
    }

    printf("%d\n", sum); 

    return 0; 
}