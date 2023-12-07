#include <bits/stdc++.h>
using namespace std; 

#define FIVE_KIND 6
#define FOUR_KIND 5
#define FULL_HOUSE 4
#define THREE_KIND 3
#define TWO_PAIR 2
#define ONE_PAIR 1
#define HIGH_CARD 0
#define HAND_TYPES 7

typedef struct hand
{
    string cards; 
    int bet; 
    int type; 
} hand; 


void assign_type (hand * h)
{  
    unordered_map<char, int> umap; 

    int j_count = 0; 

    for (char c : h->cards)
    {
        if (c == 'J')
            j_count += 1; 
        else
            (umap.find(c) != umap.end()) ? (umap[c] += 1) : (umap[c] = 1); 
    }

    int highest_count = INT_MIN; 
    char highest_char; 
    for (auto p : umap)
    {
        if (p.second > highest_count)
        {
            highest_count = p.second; 
            highest_char = p.first; 
        }
    }

    umap[highest_char] += j_count; 

    if (count_if(umap.begin(), umap.end(), [](pair<char, int> p){ return p.second == 5; }))
        h->type = FIVE_KIND; 
    else if (count_if(umap.begin(), umap.end(), [](pair<char, int> p){ return p.second == 4; }))
        h->type = FOUR_KIND; 
    else if (count_if(umap.begin(), umap.end(), [](pair<char, int> p){ return p.second == 3; }))
        h->type = (count_if(umap.begin(), umap.end(), [](pair<char, int> p){ return p.second == 2; })) ? FULL_HOUSE : THREE_KIND;
    else
    {
        int count = count_if(umap.begin(), umap.end(), [](pair<char, int> p){ return p.second == 2; }); 
        if (count == 2)
            h->type = TWO_PAIR; 
        else if (count == 1)
            h->type = ONE_PAIR; 
        else
            h->type = HIGH_CARD; 
    }
    
    return; 
}


int main(void)
{

    ifstream fptr("input"); 
    string s; 
    vector<hand> hands; 

    while (getline(fptr, s))
    {
        hand h; 
        stringstream ss(s);          
        ss >> h.cards; 
        ss >> s; 
        h.bet = stoi(s); 
        assign_type(&h); 
        hands.push_back(h); 
    }

    vector<hand> final_vec; 

    sort(hands.begin(), hands.end(), [](hand h1, hand h2) { return (h1.type < h2.type); }); 

    for (int i = 0; i < HAND_TYPES; i++)
    {
        vector<hand> temp; 
        copy_if(hands.begin(), hands.end(), back_inserter(temp), [i](hand h){ return (h.type == i); }); 

        sort(temp.begin(), temp.end(), 
            [](hand h1, hand h2)
            {
                string order = "AKQT98765432J";

                for (int i = 0; i < h1.cards.size(); i++)
                {
                    if (h1.cards[i] == h2.cards[i]) 
                        continue; 
                        
                    auto it1 = order.find(h1.cards[i]); 
                    auto it2 = order.find(h2.cards[i]); 

                    return (it1 > it2); 
                }

                return false; 
            }); 

        final_vec.insert(final_vec.end(), temp.begin(), temp.end()); 
    }
    
    int sum = 0; 
    for (int i = 0; i < final_vec.size(); i++)
        sum += (final_vec[i].bet * (i + 1)); 
    printf("%d\n", sum); 

    return 0; 
}

