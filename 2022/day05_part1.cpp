#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>


using namespace std; 

int main(void){
    ifstream fptr("input.txt"); 

    string s = ""; 
    
    vector<vector<char>> stacks; 
    vector<char> temp_stack; 

    // **** Don't have time to write all the parsing stuff because of exams ****

    temp_stack = {'J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'V', 'W', 'J'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'G', 'V', 'L', 'J', 'B', 'T', 'H'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'F', 'W', 'S', 'M', 'P', 'R', 'G'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'D', 'H', 'G', 'M', 'R'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'H', 'N', 'M', 'V', 'Z', 'D'}; 
    stacks.push_back(temp_stack); 
    temp_stack = {'G', 'N', 'F', 'H'}; 
    stacks.push_back(temp_stack); 
    


    vector<string> words; 
    s += "p"; 
    // skipping the input we don't need 
    while (s.at(0) != 'm'){
        getline(fptr, s); 
        if (s.empty()) break; 
    }

    while (getline(fptr, s)){
     
        stringstream ss(s); 
        string temp_word; 
        while (ss >> temp_word){
            words.push_back(temp_word); 
        }

        // now we have a vector with all the words in it. 
        // words[1] will be the count
        // words[3] will be the source
        // words[5] will be the destination

        int source_index = stoi(words[3]) - 1; 
        int destination_index = stoi(words[5]) - 1;
        int to_move = stoi(words[1]); 

        // less than count needed to move
        for (int i = 0; i < to_move; i++){
            if (stacks[source_index].empty()) break; 
            stacks[destination_index].push_back(stacks[source_index].at(stacks[source_index].size() - 1));
            stacks[source_index].pop_back();                     
        }
        words.clear(); 
    }   

    for (int i = 0; i < (int)stacks.size(); i++){
        printf("%c", stacks[i].at(stacks[i].size()-1));  // print top value of each 
    }
    printf("\n"); 


    return 0; 
}