// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <iostream>
#include <string.h>

using namespace std;

// O(n) with score 6/14
string abbreviation(string a, string b)
{
    int i, j, flag;
    i = j = flag = 0;

    if (a.empty() && b.empty())
        return "YES";
    if ((a.length() < b.length()) || a.empty() || b.empty())
        return "NO";

    for (i = 0; b[i] != '\0'; i++)
    {
        flag = 0;
        for (; a[j] != '\0'; j++)
        {
            if (toupper(a[j]) == b[i])
            {
                flag = 1;
                j++;
                break;
            }
            if (isupper(a[j]))
                return "NO";
        }
        if (flag == 0)
            return "NO";
    }
    for (; a[j] != '\0'; j++)
    {
        if (a[j] < 97)
            return "NO";
    }
    return "YES";
}

int main()
{
    cout << abbreviation("aBbdD", "BBD");
    return 0;
}
