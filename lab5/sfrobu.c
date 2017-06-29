#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>


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



int main(int argc, char *argv[]){

  int columns = 100;
  struct stat fileStats;

  if(fstat(0, fileStats) < 0)
    {
      fprintf(stderr, "Error with fstat.\n");
      exit(1);
    }

  char *array;
  char buff[5];

  //This checks if we have an empty file
  if(S_ISREG(fileStats.st_mode))
    {
      if(read(0, &buf, 1) == 0)
	exit(0);

      array = (char*)malloc(sizeof(char)*fileStats.st_size);
      if(array == NULL)
	{
	  fprintf(stderr, "Memory was not allocated.\n");
	  exit(1);

	}

      int file_size = fileStats.st_size;
      int temp_filesize = file_size;
      int i = 0;
      int numwords = 0;
      while(i  < s)
	{
	  read(0, &buff, 1);
	  array[i] = buff[0];
	  i++;
	  if(buff[0] == ' ')
	    numwords++;
	  
	  if(i == file_size)
	    {
	      array = realloc(array, file_size + columns);
	      if(array == NULL)
		{
		  fprintf(stderr, "Memory was not allocated.\n");
		  exit(1);
		}

	    }
	  

	}
      file_size += columns;
      fstat(0, &fileStats);
      temp_filesize = fileStats.st_size;
    }


  else
    {
      int i = 0;
      array = (char*)malloc(sizeof(char)*columns);
      if(array == NULL)
	{
	  fprintf(stderr, "Memory was not allocated.\n");
	  exit(1);
	}
      
      while(read(0, &buff, 1) > 0)
	{
	  array[i] = buff[0];
	  i++;
	  if(buff[0] == ' ')
	    numwords++;
	  if(i == columns)
	    {
	      array = realloc(array, sizeof(char)*columns*2);
	      columns *= 2;
	      if(array == NULL)
		{
		  fprintf(stderr, "Memory was not allocated.\n");
		  exit(1);
		}
	    }
      
	}
      if(array[i-1] != ' ')
	{
	  i = i+1;
	  array[i-1] = ' ';
	  numwords++;

	}

      
    }
  
  
  char **strings_array;
  strings_array = (char**)malloc(sizeof(char*) * words);
  if(strings_array == NULL)
    {
      fprintf(stderr, "Memory was not allocated.\n");
      exit(1);
    }

  int k = 0;
  strings_array[0] = array;
  int j;
  for(j = 0; j < i; j++)
    {
      if(array[j] == ' ')
	{
	  k++;
	  if(j < i - 1)
	    strings_array[k] = &array[j+1];
	}
    }


  qsort(strings_array, k, sizeof(char*), frobcmp);
  int index;
  for(index = 0; index < k; index++)
    {
      int count;
      for(count = 0; strings_array[index][count] != ' '; count++)
	{
	  putchar(strings_array[index][count]);
		  
	}
	    
      putchar(' ');
    }





  free(array);
  free(strings_array);


}

