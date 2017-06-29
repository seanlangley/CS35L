#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
  

  if(argc != 3)
    {
      fprintf(stderr, "Not correct number of arguments.\n");
      exit(1);
    }

  //argv[0] contains the program name
  char *from = argv[1];
  char *to = argv[2];

  //Check if from and to are the same length
  if(strlen(from) != strlen(to))
    {
      fprintf(stderr, "Strings are not of equal length.\n");
      exit(1);
    }


  //Check if from has duplicate bytes
  
  size_t i;
  for(i = 0; i < strlen(from); i++)
    {
      size_t j;
      for(j = i+1; j < strlen(from); j++)
	  if(from[i] == from[j])
	    {
	      fprintf(stderr, "From has duplicate bytes.\n");
	      exit(1);
	    }
	
    }



  char ch = getchar();
  while(ch != EOF)
    {
      for(i = 0; i < strlen(from); i++)
	{
	  if(ch == from[i])
	    {
	      ch = to[i];
	      break;

	    }

	}
      putchar(ch);
      ch = getchar();


    }




  return 0;
}
