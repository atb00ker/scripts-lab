// Question: https://www.hackerrank.com/challenges/counting-valleys/problem

#include <iostream>
using namespace std;

int countingValleys(int n, string s)
{
    int i, pointer, valleys, flag;
    pointer = valleys = flag = 0;
    for (i = 0; i < n; i++)
    {
        if (s[i] == 'U')
            pointer++;
        else
            pointer--;
        if (pointer == -1 && flag == 0)
        {
            valleys++;
            flag = 1;
        }
        else if (pointer == 0)
            flag = 0;
    }
    return valleys;
}

int main()
{
    int n = 12;
    string ar = "DDUUDDUDUUUD";
    cout << countingValleys(n, ar);
    return 0;
}