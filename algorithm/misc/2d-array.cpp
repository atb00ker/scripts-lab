#include <bits/stdc++.h>

using namespace std;

int hourglassSum(vector<vector<int>> arr)
{
    int arrLen = arr.size() - 2, sum, max = -63;
    for (int i = 0; i < arrLen; i++)
    {
        for (int j = 0; j < arrLen; j++)
        {
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            if (sum > max)
                max = sum;
        }
    }
    return max;
}

int main()
{

    vector<vector<int>> arr{{1, 1, 1, 0, 0, 0},
                            {0, 1, 0, 0, 0, 0},
                            {1, 1, 1, 0, 0, 0},
                            {0, 0, 2, 4, 4, 0},
                            {0, 0, 0, 2, 0, 0},
                            {0, 0, 1, 2, 4, 0}};

    cout << hourglassSum(arr);
}