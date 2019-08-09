#include<stdio.h>
#include<string.h>
#define MAX_SIZE 9
int main (int argc, const char * argv[]){
	int s;
	char digitString[MAX_SIZE];

	const char conversionTable[10][7] = {

		'-','|','|',' ','|','|','-',
		' ','|',' ',' ','|',' ',' ',
	  '-','|',' ','-',' ','|','-',
		'-','|',' ','-','|',' ','-',
		' ','|','|','-','|',' ',' ',
		'-',' ','|','-','|',' ','-',
		'-',' ','|','-','|','|','-',
		'-','|',' ',' ','|',' ',' ',
		'-','|','|','-','|','|','-',
		'-','|','|','-','|',' ','-',
	};

	int i, j, k;

	while(scanf("%d %s", &s, &digitString) != EOF) {
		if (!s) {
			return 0;
		}

		int n = strlen(digitString);
		int digit;

		for (i = 0; i < 2*s+3; i++) {
			for (j = 0; j < n; j ++) {

				digit = digitString[j] - '0';
				if ((i % (s + 1)) == 0) {
					printf(" ");
					for (k = 0; k < s; k++) {
						printf("%c", conversionTable[digit][(i / (s + 1)) * 3]);
					}
					printf(" ");
				}
				if (i > 0 && i < (s + 1)) {
					printf("%c", conversionTable[digit][2]);
					for (k = 0; k < s; k++) {
						printf(" ");
					}
					printf("%c", conversionTable[digit][1]);
				}
				if (i > (s + 1) && i < (2*s + 2)) {
					printf("%c", conversionTable[digit][5]);
					for (k = 0; k < s; k++) {
						printf(" ");
					}
					printf("%c", conversionTable[digit][4]);
				}
				if (j != n-1)
					printf(" ");

			}
			printf("\n");

		}
		printf("\n");

	}

	return 0;
}
