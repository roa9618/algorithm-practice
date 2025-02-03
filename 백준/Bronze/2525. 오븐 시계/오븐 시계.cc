#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int H, M, R;

    scanf("%d %d", &H, &M);
    scanf("%d", &R);

    if (M + R < 60) { M += R; }
    else {
        H += (M + R) / 60;
        M = (M + R) % 60;
        if (H >= 24) { H -= 24; }
    }

    printf("%d %d", H, M);

    return 0;
}