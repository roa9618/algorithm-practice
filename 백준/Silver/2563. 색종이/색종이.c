#include <stdio.h>

int main(void) 
{
    int n, x, y;
    int total = 0;
    int a[101][101] = { 0 };

    scanf("%d", &n);
    for (int i = 0; i < n; i++) 
    {
        scanf("%d %d", &x, &y);
        for (int o = x; o < x + 10; o++) 
        {
            for (int p = y; p < y + 10; p++) 
            {
                a[o][p] = 1;
            }
        }
    }
    for (int i = 0; i <= 100; i++) 
    {
        for (int j = 0; j <= 100; j++) 
        {
            total += a[i][j];
        }
    }
    printf("%d", total);

    return 0;
}