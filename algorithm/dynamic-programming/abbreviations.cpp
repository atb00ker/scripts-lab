// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <bits/stdc++.h>

using namespace std;
array<vector<string>, 1000> amemory;
// <response, alen, reference ith, string>
array<vector<tuple<int, int, int, string>>, 1000> memory;

string fetch_memory(string astring, string bstring, int alen, int blen)
{
    int i, j;
    int asize = amemory[alen].size();
    int bsize = memory[blen].size();
    for (i = 0; i < asize; i++)
    {
        if (amemory[alen][i] == astring)
        {
            for (j = 0; j < bsize; j++)
            {
                if (get<1>(memory[blen][j]) == alen && get<2>(memory[blen][j]) == i && get<3>(memory[blen][j]) == bstring)
                {
                    if (get<0>(memory[blen][j]) == 1)
                        return "YES";
                    return "NO";
                }
            }
        }
    }
    return "NA";
}

void store_memory(string a, string b, int alen, int blen, int response)
{
    alen--;
    blen--;
    amemory[alen].push_back(a);
    int asize = amemory[alen].size() - 1;
    memory[blen].push_back(make_tuple(response, alen, asize, b));
}

string abbreviation(string a, string b)
{
    int alen = a.length();
    int blen = b.length();

    string memorized = fetch_memory(a, b, alen, blen);
    if (memorized != "NA")
        return memorized;

    if (b.empty())
    {
        while (!a.empty() && islower(a[0]))
            a.erase(a.begin());
        if (a.empty())
            return "YES";
    }
    if (a.empty() && b.empty())
        return "YES";
    if (a.empty() || (alen < blen))
        return "NO";

    while (!a.empty() && islower(a[0]) != 0 && toupper(a[0]) != b[0])
    {
        a.erase(a.begin());
        string memorized = fetch_memory(a, b, alen, blen);
        if (memorized != "NA")
            return memorized;
    }

    if (a.empty() || (alen < blen))
        return "NO";

    if (isupper(a[0]))
    {
        if (a[0] != b[0])
            return "NO";
        a.erase(a.begin());
        b.erase(b.begin());
        if (abbreviation(a, b) == "YES")
        {
            store_memory(a, b, alen, blen, 1);
            return "YES";
        }
        store_memory(a, b, alen, blen, 0);
        return "NO";
    }
    a.erase(a.begin());
    if (abbreviation(a, b) == "YES")
    {
        store_memory(a, b, alen, blen, 1);
        return "YES";
    }
    b.erase(b.begin());
    if (abbreviation(a, b) == "YES")
    {
        store_memory(a, b, alen, blen, 1);
        return "YES";
    }
    store_memory(a, b, alen, blen, 0);
    return "NO";
}

int main()
{
    cout << abbreviation("daBcddaBcddaBcddaBcd", "ABCABCABCABC");
    cout << abbreviation("daBcddaBcddaBcddaBcd", "ABCABCABCABC");
    cout << abbreviation("daBcddaBcddaBcddaBcd", "ABCABCABCABC");
    cout << abbreviation("daBcddaBcd", "ABCABC");
    cout << abbreviation("daBcddaBcd", "ABCABC");
    cout << abbreviation("daBcd", "ABC");
    return 0;
}
