#include <bits/stdc++.h>
using namespace std; 

int main(void)
{

    ifstream fptr("input"); 
    string s; 
    string token; 
    int sum = 0; 
    vector<int> matches_per_card;   

    while (getline(fptr, s))
    {
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
       

        int matches = 0; 
        for (int card_num : card)
        {
            for (int win_num : win)
            {
                if (card_num == win_num)
                {
                    matches += 1; 
                }
            }
        }
        matches_per_card.push_back(matches);      
    }   
    
    vector<int> cards (matches_per_card.size(), 1); 

    for (int i = 0; i < cards.size(); i++)
    {
        sum += cards[i]; 

        for (int j = 1; j <= matches_per_card[i]; j++)
        {
            if (i + j == cards.size())
            {
                break; 
            }

            cards[i + j] += 1 * cards[i]; 
        } 
    }

    cout << sum << "\n"; 
    
    return 0; 
}

