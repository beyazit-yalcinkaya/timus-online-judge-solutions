#include <stdio.h>
int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	if ( a + b > 10 )
	{
		printf("%d %d\n", 10 - a, 10 - b);
	}
	else
	{
		printf("%d %d\n", b - 1, a - 1);
	}
	return 0;
}