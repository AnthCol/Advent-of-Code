#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    string temp = ""; 
    vector<int> vec; 

    int index = 0, sum = 0, count = 0; 

    int left_bound_1, left_bound_2;
    int right_bound_1, right_bound_2; 

    string left = ""; 
    string right = ""; 

    while (getline(fptr, s)){
        
        index = s.find(","); 
        for (int i = 0; i < index; i++){
            left += s.at(i); 
        }
        for (int i = index + 1; i < s.length(); i++){
            right += s.at(i); 
        }


        index = left.find("-"); 
        for (int i = 0; i < index; i++){
            temp += left.at(i); 
        }
        left_bound_1 = stoi(temp); 

        temp = ""; 

        for (int i = index + 1; i < left.length(); i++){
            temp += left.at(i); 
        }
        right_bound_1 = stoi(temp); 

        temp = ""; 


        index = right.find("-"); 
        for (int i = 0; i < index; i++){
            temp += right.at(i); 
        }
        left_bound_2 = stoi(temp); 

        temp = ""; 

        for (int i = index + 1; i < right.length(); i++){
            temp += right.at(i); 
        }
        right_bound_2 = stoi(temp); 
       

        if (left_bound_1 <= left_bound_2 && right_bound_1 >= right_bound_2) count++; 
        else if (left_bound_2 <= left_bound_1 && right_bound_2 >= right_bound_1) count++; 

        left = ""; 
        right = ""; 
        temp = ""; 

    }   

    cout << count << endl; 

    return 0; 
}