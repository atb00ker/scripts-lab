// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <bits/stdc++.h>

using namespace std;

string abbreviation(string a, string b)
{
    if (b.empty())
    {
        while (!a.empty() && islower(a[0]))
            a.erase(a.begin());
        if (a.empty())
            return "YES";
    }
    if (a.empty() && b.empty())
        return "YES";
    if (a.empty() || (a.length() < b.length()))
        return "NO";

    while (!a.empty() && islower(a[0]) != 0 && toupper(a[0]) != b[0])
        a.erase(a.begin());

    if (a.empty() || (a.length() < b.length()))
        return "NO";

    if (isupper(a[0]))
    {
        if (a[0] != b[0])
            return "NO";
        a.erase(a.begin());
        b.erase(b.begin());
        if (abbreviation(a, b) == "YES")
            return "YES";
        return "NO";
    }
    a.erase(a.begin());
    if (abbreviation(a, b) == "YES")
        return "YES";
    b.erase(b.begin());
    if (abbreviation(a, b) == "YES")
        return "YES";
    return "NO";
}

int main()
{
    // cout << abbreviation("AbdBD", "ABD");
    // cout << abbreviation("AfPZN", "APZNC");
    cout << abbreviation("daBcd", "ABC");
    return 0;
}
