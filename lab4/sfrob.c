#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int frobcmp(const void *a, const void *b){

  char *s1 = *(char **)a;
  char *s2 = *(char **)b;

  int len1 = strlen(s1);
  int len2 = strlen(s2);

  int index;

  for(index = 0; index <= len1 && index <= len2; index++)
    {
      char s1frob = s1[index] ^ 42;
      char s2frob = s2[index] ^ 42;
      
    
      if(s1frob > s2frob) return 1;
      if(s2frob > s1frob) return -1;
     

    }

  //If this loop doesn't return, all characters up to a prefix were the same
  //Check which one is shorter/longer
  if(len1 > len2) return 1;
  if(len2 > len1) return -1;

  //Strings are the same
  return 0;

}


int main(){

  char *curr_string;
  char **array;
  int ch = '#';
  int numstrings = 0;

  array = (char**)malloc(sizeof(char*));
  curr_string = (char*)malloc(sizeof(char));

  if(array == NULL || curr_string == NULL)
    exit(1);

  int i = 0;
  ch = getchar();


  //Read input from stdin
  while(ch != EOF)
    {

      array[numstrings] = curr_string;
      if(ch != ' ')
      	{
	  curr_string[i] = ch;
	  i++;
	  int len = strlen(curr_string);
	  
	  curr_string = (char*)realloc(curr_string, sizeof(char) * (len + 1));

	  if(curr_string == NULL)
	    exit(1);

	  ch = getchar();
      	}


      //Allocate Space for a second word
      if(ch == ' ')
	  {
      	  numstrings++;
	  //New array size should be numstrings + 1
      	  array =(char**)realloc(array, sizeof(char*)*(numstrings+1));

	  if(array == NULL)
	    exit(1);
	  //Allocate a new string
	  curr_string = (char*)malloc(sizeof(char));

	  if(curr_string == NULL)
	    exit(1);

	  array[numstrings] = curr_string;
      	  i = 0;
	  ch = getchar();
	  
	}
    }
  
  qsort(array, numstrings, sizeof(char*), frobcmp);


  //stdout functions
  int index = 0;
  for(index = 0; index <= numstrings; index++)
    {
      int j = 0;
      int len = strlen(array[index]);


      for(j = 0; j < len; j++)
	  putchar(array[index][j]);


      putchar(' ');
      

    }
  
  free(array);
  free(curr_string);

  
  

  return 0;

}
