#include <bits/stdc++.h>
#define pb push_back
using namespace std; 

int main(void){
    FILE * fptr = fopen("input.txt", "r"); 
    char * one = (char*)malloc(sizeof(char) * 10000); 
    char * two = (char*)malloc(sizeof(char) * 10000); 
    char * three = (char*)malloc(sizeof(char) * 10000); 
    int index = 0, sum = 0; 
    vector<int> vec; 
    string low = "abcdefghijklmnopqrstuvwxyz"; 
    string upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 

    
    while (!feof(fptr)){
        fgets(one, 10000, fptr); 
        one[strlen(one) - 1] = '\0'; 
        fgets(two, 10000, fptr); 
        two[strlen(two) - 1] = '\0'; 
        fgets(three, 10000, fptr); 
        three[strlen(three) - 1] = '\0'; 
        
        for (int i = 0; i < strlen(one); i++){
            for (int x = 0; x < strlen(two); x++){
                if (one[i] == two[x]){
                    for (int j = 0; j < strlen(three); j++){
                        if (three[j] == two[x]){
                            if (islower(two[x])){
                                for (int z = 0; z < low.length(); z++){
                                    if (two[x] == low.at(z)){
                                        sum += z + 1; 
                                        j = strlen(three); 
                                        x = strlen(two); 
                                        i = strlen(one); 

                                        break; 
                                    }
                                }
                            }
                            else{
                                for (int z = 0; z < upperLetters.length(); z++){
                                    if (two[x] == upperLetters.at(z)){
                                        sum += z + 1 + 26; 
                                        j = strlen(three); 
                                        x = strlen(two); 
                                        i = strlen(one); 

                                        break; 
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        
    }


    printf("%d\n", sum); 


    fclose(fptr); 



    return 0; 
}