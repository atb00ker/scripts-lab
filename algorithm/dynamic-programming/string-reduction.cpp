// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

// Brute Attempt #2
char otherElement(char one, char two)
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
            if (seen_before % 2 == 0)
                compare = gstring[i];
            else
                compare = otherElement(compare, gstring[i]);
            seen_before = 1;
            continue;
        }
        gstring_size--;
        compare = otherElement(compare, gstring[i]);
    }
    return gstring_size;
}

int trueReduction(string gstring)
{
    int as, bs, cs;
    as = bs = cs = 0;
    for (int i = 0; gstring[i] != '\0'; i++)
    {
        if (gstring[i] == 'a')
            as++;
        if (gstring[i] == 'b')
            bs++;
        if (gstring[i] == 'c')
            cs++;
    }
    if ((as == 0 && bs == 0) || (cs == 0 && bs == 0) || (as == 0 && cs == 0))
        return gstring.size();
    else if ((as % 2 == 0 && bs % 2 == 0 && cs % 2 == 0) || (as % 2 != 0 && bs % 2 != 0 && cs % 2 != 0))
        return 2;
    return 1;
}

int main()
{
    // srand(time(NULL));
    // string gstring, options = "abc";
    // for (int j = 0; j < 100; j++)
    // {
    //     gstring.clear();
    //     for (int i = 0; i <= 10; i++)
    //         gstring.push_back(options[rand() % (3)]);
    //     if (stringReduction(gstring) != trueReduction(gstring))
    //         cout << gstring << endl;
    // }
    cout << stringReduction("baacbacabbb") << trueReduction("baacbacabbb");
    return 0;
}
