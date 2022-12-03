#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("input.txt", "r"); 
    char * s = (char*)malloc(sizeof(char) * 10000); 
    int index = 0, sum = 0; 
    vector<int> vec; 
    string low = "abcdefghijklmnopqrstuvwxyz"; 
    string upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 

    std::string one = ""; 
    std::string two = ""; 
    
    while (!feof(fptr)){
        fgets(s, 10000, fptr); 
        s[strlen(s) - 1] = '\0'; 
        
   
        for (int i = 0; i < strlen(s)/2; i++){
            one += s[i]; 
        }
        one += "\0"; 
        for (int i = strlen(s) - 1; i >= strlen(s)/2; i--){
            two += s[i]; 
        }
        two += "\0"; 

        for (int i = 0; i < one.length(); i++){
            for (int x = 0; x < two.length(); x++){
                if (one.at(i) == two.at(x)){
                    if(islower(one.at(i))){
                        for (int j = 0; j < low.length(); j++){
                            if (one.at(i) == low.at(j)){
                                sum += j + 1; 
                                x = two.length(); 
                                i = one.length(); 
                                break; 
                            }
                        }
                    }
                    else{
                        for (int j = 0; j < upperLetters.length(); j++){
                            if (one.at(i) == upperLetters.at(j)){
                                sum += j + 1 + 26; 
                                x = two.length(); 
                                i = one.length(); 
                                break; 
                            }
                        }
                    }
                }
            }
        } 
        one = ""; 
        two = ""; 
    }


    printf("%d\n", sum); 


    fclose(fptr); 
    free(s); 


    return 0; 
}