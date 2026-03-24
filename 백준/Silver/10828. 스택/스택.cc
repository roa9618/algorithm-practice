#include <stdio.h>
#include <string.h>

int stack[10001] = {0};

int main(void)
{
    int n, x;
    int stval = 0;
    char cmd[6];

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%5s", cmd);

        if (strcmp(cmd, "push") == 0)
        {
            scanf("%d", &x);
            stack[stval] = x;
            stval = stval + 1;
        }
        else if (strcmp(cmd, "pop") == 0)
        {
            if (stval == 0)
            {
                printf("%d\n", -1);
            }
            else
            {
                printf("%d\n", stack[stval - 1]);
                stval = stval - 1;
            }
        }
        else if (strcmp(cmd, "size") == 0)
        {
            printf("%d\n", stval);
        }
        else if (strcmp(cmd, "empty") == 0)
        {
            if (stval == 0)
            {
                printf("%d\n", 1);
            }
            else
            {
                printf("%d\n", 0);
            }
        }
        else if (strcmp(cmd, "top") == 0)
        {
            if (stval == 0)
            {
                printf("%d\n", -1);
            }
            else
            {
                printf("%d\n", stack[stval - 1]);
            }
        }
    }

    return 0;
}