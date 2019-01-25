// Question: https://www.hackerrank.com/challenges/minimum-swaps-2/problem

#include <bits/stdc++.h>

using namespace std;

int minimumSwaps(vector<int> ar)
{
    int i, pos, swaps = 0;
    int n = ar.size();
    for (i = 0; i < n; i++)
    {
        while (ar[i] - i != 1)
        {
            pos = ar[i] - 1;
            ar[pos] = ar[i] + ar[pos];
            ar[i] = ar[pos] - ar[i];
            ar[pos] = ar[pos] - ar[i];
            swaps++;
        }
    }
    return swaps;
}

int main()
{
    // int ar[] = {6, 4, 3, 1, 2, 5};
    int ar[] = {2, 1, 3, 5, 6, 4};
    cout << minimumSwaps(ar);
    return 0;
}
