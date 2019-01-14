// Question : https: //www.hackerrank.com/challenges/abbr/problem

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

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
    int acount, bcount, ccount, response, gstring_size, gstring_size_end, glength;
    gstring_size = gstring_size_end = glength = gstring.size();
    acount = bcount = ccount = 0;
    int seen_before_end, seen_before;
    seen_before_end = seen_before = 1;
    char compare_end, compare = gstring[0];
    compare_end = gstring[--glength];
    for (int i = 1; gstring[i] != '\0'; i++)
    {
        if (gstring[i] == 'a')
            acount++;
        if (gstring[i] == 'b')
            bcount++;
        if (gstring[i] == 'c')
            ccount++;
        if (compare_end == gstring[glength - i])
            seen_before_end++;
        else
        {
            gstring_size_end -= seen_before_end;
            if (seen_before_end % 2 == 0)
                compare_end = gstring[glength - i];
            else
                compare_end = otherElement(compare_end, gstring[glength - i]);
            seen_before_end = 1;
        }
        if (compare == gstring[i])
            seen_before++;
        else
        {
            gstring_size -= seen_before;
            if (seen_before % 2 == 0)
                compare = gstring[i];
            else
                compare = otherElement(compare, gstring[i]);
            seen_before = 1;
        }
    }
    if (gstring_size < gstring_size_end)
        response = gstring_size;
    else
        response = gstring_size_end;
    if (response < 3 || acount == glength || bcount == glength || ccount == glength)
        return response;
    if (response > 2 && response % 2 == 0)
        return 2;
    return 1;
}

int main()
{
    srand(time(NULL));
    string gstring, options = "abc";
    for (int j = 0; j < 10; j++)
    {
        gstring.clear();
        for (int i = 0; i <= 10; i++)
            gstring.push_back(options[rand() % (3)]);
        cout << stringReduction(gstring) << " " << gstring << endl;
    }
    return 0;
}
