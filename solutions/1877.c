#include <stdio.h>
int main(void)
{
	int first_lock, second_lock;
	scanf("%d", &first_lock);
	scanf("%d", &second_lock);
	if ( first_lock % 2 == 0 || second_lock % 2 == 1 )
	{
		printf("yes\n");
	}
	else
	{
		printf("no\n");
	}
	return 0;
}