#include <stdio.h>
#include <string.h>

int que[10001];

int main(void)
{
    int n, x;
    int frontIdx = 0;
    int backIdx = 0;
    char cmd[6];

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%5s", cmd);

        if (strcmp(cmd, "push") == 0)
        {
            scanf("%d", &x);
            que[backIdx] = x;
            backIdx++;
        }
        else if (strcmp(cmd, "pop") == 0)
        {
            if (frontIdx == backIdx)
            {
                printf("%d\n", -1);
            }
            else
            {
                printf("%d\n", que[frontIdx]);
                frontIdx++;
            }
        }
        else if (strcmp(cmd, "size") == 0)
        {
            printf("%d\n", backIdx - frontIdx);
        }
        else if (strcmp(cmd, "empty") == 0)
        {
            if (frontIdx == backIdx)
            {
                printf("%d\n", 1);
            }
            else
            {
                printf("%d\n", 0);
            }
        }
        else if (strcmp(cmd, "front") == 0)
        {
            if (frontIdx == backIdx)
            {
                printf("%d\n", -1);
            }
            else
            {
                printf("%d\n", que[frontIdx]);
            }
        }
        else if (strcmp(cmd, "back") == 0)
        {
            if (frontIdx == backIdx)
            {
                printf("%d\n", -1);
            }
            else
            {
                printf("%d\n", que[backIdx - 1]);
            }
        }
    }

    return 0;
}