// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <iostream>

using namespace std;

// Brute Attempt #1
char other_element(char one, char two)
{
    if (one == 'a')
        return (two == 'b') ? 'c' : 'b';
    if (one == 'b')
        return (two == 'c') ? 'a' : 'c';
    return (two == 'a') ? 'b' : 'a';
}

int stringReduction(string gstring)
{
    char compare = gstring[0];
    int gstring_size = gstring.size();
    int seen_before = 1;
    for (int i = 1; gstring[i] != '\0'; i++)
    {
        if (compare == gstring[i])
        {
            seen_before++;
            continue;
        }
        if (seen_before > 1)
        {
            gstring_size -= seen_before;
            seen_before = 1;
            if (seen_before % 2 == 0)
                compare = gstring[i];
            else
                compare = other_element(compare, gstring[i]);
            continue;
        }
        gstring_size--;
        compare = other_element(compare, gstring[i]);
    }
    return gstring_size;
}

int main()
{
    cout << stringReduction("ccbaccccbcccccbbccbaabaaabcabaabcbbcbccabccbcbacbcccbaccbabcabbcaa");
    return 0;
}
