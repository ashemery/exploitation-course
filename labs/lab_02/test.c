#include<stdio.h>
#include<string.h>

void myfun2(char* x) {
	printf("You entered : % s\n", x);
}

void myfun1(char* str) {
	char buffer[16];
	strcpy(buffer, str);
	myfun2(buffer);
}

int main(int argc, char* argv[]) {
	if (argc > 1)
		myfun1(argv[1]);
	else
		printf("No arguments!\n");

	return 0;
}
