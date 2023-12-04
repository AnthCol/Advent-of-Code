#include <bits/stdc++.h>
using namespace std; 

int main(void){

    ifstream fptr("input"); 
    int sum = 0; 
    string s; 
    string token;
    
    while (getline(fptr, s)){
        s.erase(0, s.find(":") + 2); 
        
        int flag = 0; 
        vector<int> card; 
        vector<int> win; 
        stringstream ss(s); 
        while (ss >> token)
        {
            if (token == "|")
            {
                flag = 1; 
                continue; 
            }

            int val = stoi(token); 
            (flag) ? win.push_back(val) : card.push_back(val); 
        }
       

        int points = 0; 
        for (int card_num : card)
        {
            for (int win_num : win)
            {
                if (card_num == win_num)
                {
                    points = (points == 0) ? 1 : points * 2; 
                }
            }
        }

        sum += points; 
    }   
    
    cout << sum << "\n"; 
    
    return 0; 
}

