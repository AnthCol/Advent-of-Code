#include <bits/stdc++.h>
#define pb push_back
using namespace std; 


int check_unique (string input){
    for (int i = 0; i < (int)input.length(); i++){
        for (int x = i + 1; x < (int)input.length(); x++){
            if (input.at(i) == input.at(x)) return 0; 
        }
    }

    return 1; 
}

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    string substring; 
    vector<int> vec; 

    int index = 0, sum = 0; 
 
    getline(fptr, s); 

    for (int i = 0; i < (int)s.length() - 5; i++){
        substring = s.substr(i, 4); 
        if (check_unique(substring)){
            printf("%d\n", i + 4); 
            break; 
        }
    }



    return 0; 
}