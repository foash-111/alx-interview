#include <stdio.h>

int main() {
    int t = 0, i = 0, j = 0, order = 0;
    int num_lines = 0;
    char line[] = "....";
    int arr[500];

    scanf("%d", &t);

    while(t--) {
        scanf("%d", &num_lines);

        j = 0;
        while(j < num_lines) {
            scanf("%s", line);

            order = 0;
            while(line[i]) {
                if (line[i] == '#')
                {
                    arr[order] = i;
                    order++;
                }
                i++;
            }
            i = 0;
        j++;
        }
        num_lines--;
        printf("%d", arr[num_lines] + 1);
        num_lines--;

        while (num_lines >= 0)
        {
            printf(" %d", arr[num_lines] + 1);
            num_lines--;
        }
        printf("\n");

    }
    return 0;
}
