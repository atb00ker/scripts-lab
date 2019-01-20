// Question: https://www.hackerrank.com/challenges/sock-merchant/problem

#include <iostream>
using namespace std;

// Complete the sockMerchant function below.
int sockMerchant(int n, int *ar)
{
    int i, j, pairs = 0;
    for (i = 0; i < n; i++)
    {
        if (ar[i] == 0)
            continue;
        for (j = i + 1; j < n; j++)
        {
            if (ar[j] != 0 && ar[i] == ar[j])
            {
                ar[i] = ar[j] = 0;
                pairs++;
            }
        }
    }
    return pairs;
}

int main()
{
    int n = 9;
    int ar[] = {10, 20, 20, 10, 10, 30, 50, 10, 20};
    sockMerchant(n, ar);
    return 0;
}
