// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <bits/stdc++.h>

using namespace std;
// <a, b, response>
array<array<vector<tuple<string, string, int>>, 1005>, 1005> memory;

string fetch_memory(string astring, string bstring)
{
    int alen = astring.length();
    int blen = bstring.length();
    int i, vec_size = memory[alen][blen].size();
    for (i = 0; i < vec_size; i++)
    {
        if (get<0>(memory[alen][blen][i]) == astring && get<1>(memory[alen][blen][i]) == bstring)
        {
            if (get<2>(memory[alen][blen][i]) == 1)
                return "YES";
            return "NO";
        }
    }
    return "NA";
}

void store_memory(string a, string b, int response)
{
    int alen = a.length();
    int blen = b.length();
    memory[alen][blen].push_back(make_tuple(a, b, response));
}

string abbreviation(string a, string b)
{
    int alen = a.length();
    int blen = b.length();
    string memorized;
    memorized = fetch_memory(a, b);
    if (memorized != "NA")
        return memorized;
    if (b.empty())
    {
        while (!a.empty() && islower(a[0]))
            a.erase(a.begin());
        if (a.empty())
            return "YES";
        return "NO";
    }
    if (a.empty() && b.empty())
        return "YES";
    if (a.empty() || (alen < blen))
        return "NO";
    while (!a.empty() && islower(a[0]) != 0 && toupper(a[0]) != b[0])
    {
        a.erase(a.begin());
        memorized = fetch_memory(a, b);
        if (memorized != "NA")
            return memorized;
    }

    if (a.empty() || (alen < blen))
        return "NO";

    if (isupper(a[0]))
    {
        if (a[0] != b[0])
        {
            store_memory(a, b, 0);
            return "NO";
        }
        a.erase(a.begin());
        b.erase(b.begin());
        if (abbreviation(a, b) == "YES")
            return "YES";
        return "NO";
    }
    a.erase(a.begin());
    if (abbreviation(a, b) == "YES")
    {
        store_memory(a, b, 1);
        return "YES";
    }
    b.erase(b.begin());
    if (abbreviation(a, b) == "YES")
    {
        store_memory(a, b, 1);
        return "YES";
    }
    store_memory(a, b, 0);
    return "NO";
}

int main()
{
    cout << abbreviation("daBcddaBcddaBcddaBcd", "ABCABCABCABC");
    cout << abbreviation("daBcddaBcddaBcddaBcd", "ABCABCABCABC");
    cout << abbreviation("daBcddaBcd", "ABCABC");
    cout << abbreviation("daBcddaBcd", "ABCABC");
    cout << abbreviation("daBcd", "ABC");
    cout << abbreviation("daBcd", "ABC");

    cout << abbreviation("lyylyyllyyylllyylyyylyllylyllllllyyylyllyyyylllllylyylyyllylyylllyhyllllyylllyllylyllylyllllyylylylyyylyllyyylylllyylylllyyllyylylyyllyylyyylllyllylyyllyllllyylylyylllllllyllyyyyyylllyyylylylylyyyyyyyymylyyyylyyyylyyyylyyyylylylylylyllylyylllyllyylylyyllyyyylylllyyyyyllllllyllyylllylyylyllllyyllllylyyyyyllllylylllyyyylyylyyyllyylyyyylylyyyylyyyyylyylllyyllylyyllyllyyyyyylylllylyyyyyllyylyyyyylyyylyylyylylylyyllllyylllyylylllyllyylylyllylllyllyyyyyylyyyllyllyyllyllyylyllyllyyylyyyyylylllyyylllyyyllylyllylylyyllylllylyyyyylyyyylyyyylyyyyylylllllyylyylyyyylyylyyylyylllllllyyyyyyyylyyylylllllylyrlyylllyylylllllylyylyylyyllylyyyyllyyyllylllyllylllylyyyyylylylyyllyyyyylllyyyllllylyllyyyllllyyllyyylllylyylyyyllllyllylllylyllylllyyllllyllyyymyylylllyylllllllyyyyylyyyllyyyyyyylylylyylylyylylyyllyyyllylylyyyylyyyyyyyyyyylllylylllllylllyylllyyllllllyylllllyllyyllyylyyllllyylyylyyllllyyyllllyyylylylylyylyllylllyyylylylylyyylyllllllylyllllyylyllylllyllyylylllylllyllllylyyylylllyyylllyylllllllyllyyy", "LYYLYYLYYYLLLYYLYYYYLLYLLLLLLYYYLYLLYYYYLLLLYLYLYYLLYLYLLYYLLLYYLLLLYLYLLYLYLLLLYYLYLLYYLYLLYLLLLYLYLLYLYYLLYYLLYYLYYYLLLYLYLYYLLYLLYYYLYLLLLLLLYLLYYYYYLLLYYYLYLYLYLYYYYYYYLYYYLYYYYLYYLYYYYLYYLYLYLYLLYLYYLLLYLLYYLYLYLLYYYLYLLLYYYYLLLLLLYLLYYLLLYLYYLYLLLLYLLLYLYYYYYLLLLLYLLLYYYYLYYLYYLLYYLYYYYLYLYYYYLYYYYYLYYLLLYYLLYLYLLYLLYYYYYLYLLYLYYYYYLLYYLYYYYLYYYLYYLYYLYLYLYYLLLLYYLLLYYLYLLLYLLYLYLYLLYLLLYLLYYYYYYLYYYLLYLYYLLYLLYLYLLYLLYYYLYYYYLLLLYYYLLLYYYLLYLYLLYLYLYYLLYLLLYLYYYYYLYYYYLYYYYLYYYYYLYLLLLLYYLYYLYYYLYYYYYLYYLLLLLLLYYYYYYYYLYYLYLLLLYLYLYYLLYYLYLLLLLYLYYLYYLYLLYLYYYLYYYLYLLLYLLYLLYLYYYYYLLYYYLLYYYYYLLYYYLLLLYLYLLYYYLLLLYYLLYYYLLLYLYYLYYYLLLYLLYLYLYLLYLLYYLLLYLLYYYYYLYLLLYYLLLLLLLYYYYYLYYLLYYYYYYLYYLLYYLYLYYLLYYYLLYYLYYYYLYYYYYYYYYYYLLLYYLLLLLYLLLYYLLLYYLLLLLYYLLLLYLYYLLYYLYYLLLYYLYYLYYLLLLYYYLLLLYYYYLYLYLYYYLLYLLLYYYLYLYLYLYYLYLLLLLYLYLLLYYYLLYLYLLYYLYLLYLLLYLLYLYYYLYLLLYYLLYYLLLLLLYLYY");
    return 0;
}
