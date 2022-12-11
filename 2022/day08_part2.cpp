#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int check_north(vector<vector<int>> map, int row, int column){
    if (row == 0) return 0; 
    int count = 0; 
    for (int i = row - 1; i >= 0; i--){
        count++; 
        if (map[i][column] >= map[row][column]) break; 
    }
    return count; 
}
int check_south(vector<vector<int>> map, int row, int column){
    if (row == (int)map.size() - 1) return 0; 
    int count = 0; 
    for (int i = row + 1; i <= (int)map.size() - 1; i++){
        count++; 
        if (map[i][column] >= map[row][column]) break;  
    }
    return count; 
}
int check_west(vector<vector<int>> map, int row, int column){
    if (column == 0) return 0; 
    int count = 0; 
    for (int i = column - 1; i >= 0; i--){
        count++; 
        if (map[row][i] >= map[row][column]) break; 
    }
    return count; 
}
int check_east(vector<vector<int>> map, int row, int column){
    if (column == (int)map[0].size() - 1) return 0; 
    int count = 0; 
    for (int i = column + 1; i <= (int)map[0].size() - 1; i++){
        count++; 
        if (map[row][i] >= map[row][column]) break; 
    }
    
    return count; 
}

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 

    vector<vector<int>> map; 
    vector<int> temp; 
    while (getline(fptr, s)){
        for (int i = 0; i < (int)s.length(); i++){
            temp.pb((int)s.at(i) - 48);
        }
        map.pb(temp); 
        temp.clear(); 
    }   

    int product, max = -1; 
    for (int i = 0; i < (int)map.size(); i++){
        for (int x = 0; x < (int)map[i].size(); x++){
            product = check_north(map, i, x) * check_south(map, i, x) * check_east(map, i, x) * check_west(map, i, x); 
            if (product > max) max = product;  
        }
    }  
    printf("%d\n", max); 
    return 0; 
}