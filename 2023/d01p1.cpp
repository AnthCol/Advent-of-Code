#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <iostream>
#include <vector>

using namespace std; 

int main(void)
{

    FILE * fptr = fopen("input", "r"); 
    char s [10000];  
    int sum = 0; 
    int flag = 0; 
    while (fgets(s, 9999, fptr) != NULL)
    {
        vector<int> digits; 
        for (int i = 0; i < strlen(s); i++)
        {
            if (isdigit(s[i]))
            {
                digits.push_back(s[i] - '0'); 
            }
        }

        sum += (digits[0] * 10) + digits[digits.size() - 1]; 
    }

    printf("%d\n", sum); 

    return 0; 
}

