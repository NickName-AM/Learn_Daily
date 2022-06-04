#include<stdio.h>

int main()
{
	int i=6;
	int j=0;

	j=i++;
	printf("Value of j: %d \n", j);
	printf("Value of i: %d \n\n", i);

	// i++ increases the value of i by 1
	// Meaning i becomes 7
	// But returns the value of i that was before the increment
 	// Since i++ returns previous value of i, j becomes 6


	// Again
	i=6;
	j=0;
	
	j=++i;
	printf("Value of j: %d \n", j);
	printf("Value of i: %d \n", i);

	// We set i,j to their previous values
	// ++i increases the value of i by 1
	// Meaning i becomes 7
	// But returns the value of i that will be after the increment
	// So, the value of j becomes 7
}
