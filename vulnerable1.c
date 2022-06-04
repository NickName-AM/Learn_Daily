// Try to call callmesenpai() without giving the correct password


#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void callmesenpai()
{
	printf("No senpai, this is out fight!\nYou won\n");
}

int authenticate(char *pass)
{
	int i = 0;
	// Wasted 5 mins thinking of a suitable variable name. I gave up.
	char local_pass[30];
	strcpy(local_pass, pass);
	
	if(strcmp("himeragi", local_pass) == 0)
	{
		i++;
	}

	return i;
}

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("%s <password>", argv[0]);
		exit(-1);
	}
	
	if( authenticate(argv[1]) )
	{
		callmesenpai();
	}else{
		printf("Can't call\n");
	}

}

// HINT: How are variables stored in the stack?
