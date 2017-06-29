Last login: Thu Jun 29 11:41:47 on ttys000
Seans-MacBook-Air-2:~ seanlangley$ ls
961		Desktop		Downloads	Movies		Pictures	RANDOM		VirtualBox VMs
Applications	Documents	Library		Music		Public		STDERR		projects
Seans-MacBook-Air-2:~ seanlangley$ ssh seanl@lnxsrv.seas.ucla.edu
seanl@lnxsrv.seas.ucla.edu's password: 
Last login: Wed Jun 28 20:50:39 2017 from vpn-128-97-245-60.host.ucla.edu
*****************************************************************************
                 lnxsrv01.seas.ucla.edu RHEL 6
*****************************************************************************

    * Please use "lnxsrv.seas.ucla.edu" to login for load balancing
    * User processes older than 36 hours will be cleaned up
    * You can run graphical applications from your PC using SSH and Xming
    !! Please see http://www.seasnet.ucla.edu/UnixServers/lnxsrv !!

*****************************************************************************
*****************************************************************************
* ========================================================================= *
* ACCOUNT RENEWALS                                             Jun  1, 2017 *
*                                                                           *
* SEASnet has begun notifying users of the account renewal process.  The    *
* first notification has already been sent via email to your SEASnet        *
* account or Official UCLA Email Address.  Although the account renewal     *
* process actually takes place in October, we send out the first notice     *
* early as a courtesy in case you are planning on taking a leave of absence *
* for the upcoming fall quarter.  Please make sure you check your email for *
* this important announcement.  Accounts that are not renewed or placed on  *
* hold by October 31, 2017 will be removed and will NOT be restored.        *
*                                                                           *
* Detailed information about the renewal process can also be found here:    *
*       http://www.seasnet.ucla.edu/seasnet-accounts                        *
*                                                                           *
* ========================================================================= *
* SEASnet Computing Access                                                  *
*                                                                           *
* Priority is given both on the servers and in the student labs to those    *
* students doing coursework. Computing support for research is provided by  *
* each department.                                                          *
*****************************************************************************
* For assistance please contact help@seas.ucla.edu or call 206-6864.        *
*****************************************************************************
[seanl@lnxsrv01 ~]$ ls
classes  code  cs111  Desktop  Documents  Downloads  WINDOWS  www  www.20170629
[seanl@lnxsrv01 ~]$ cd cs111/project0/
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ cd Makefile
-bash: cd: Makefile: Not a directory
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ emacs Makefile
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
h[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
lkasjdflkajsf
lkasjdflkajsf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
alskdflkasdjflkasdjflkajsdlfk
alskdflkasdjflkasdjflkajsdlfk
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
asldkjfalksdjflkadsjflksdajf
asldkjfalksdjflkadsjflksdajf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
lsdkjflkasdjflkasdjflaksjfd
lsdkjflkasdjflkasdjflaksjfd
8[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
asldkjflkasdjflkasdjflkajdlfkjaslfdkjsadlfjk
asldkjflkasdjflkasdjflkajdlfkjaslfdkjsadlfjk
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
asdlkfjlaksdjflkadsjflkasdjflksdjflkasdjf
asdlkfjlaksdjflkadsjflkasdjflksdjflkasdjf
(\I[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --input file.txt
hello world
?~[seanl@lnxsrv01 ~/cs111/project0]$ emacs file.txt 
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --input file.txt
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ cat fiel
cat: fiel: No such file or directory
[seanl@lnxsrv01 ~/cs111/project0]$ cat file.txt
hello world
[seanl@lnxsrv01 ~/cs111/project0]$ emacs file.txt
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --input file.txt
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
lab0.c: In function ‘main’:
lab0.c:88: error: ‘nbytes’ undeclared (first use in this function)
lab0.c:88: error: (Each undeclared identifier is reported only once
lab0.c:88: error: for each function it appears in.)
make: *** [all] Error 1
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --input file.txt
hello world
s[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
lab0.c: In function ‘main’:
lab0.c:134: error: ‘else’ without a previous ‘if’
make: *** [all] Error 1
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0.c
-bash: ./lab0.c: Permission denied
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
size of data is 256
strlen data is 14
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
lab0.c: In function ‘main’:
lab0.c:118: error: expected expression before ‘if’
lab0.c:141: error: too few arguments to function ‘write’
lab0.c:141: error: expected ‘;’ before ‘}’ token
make: *** [all] Error 1
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
l
hello world
0[seanl@lnxsrv01 ~/cs111/project0]$ 
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world
?
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world

hello world
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
alksdjflkajsdflkasdlkfasdlkfj
data is alksdjflkajsdflkasdlkfasdlkfj
alksdjflkajsdflkasdlkfasdlkfj[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
asldkjflaksdjflkasdjflkajsdlfkajsdlfkjasdlfkj
data is asldkjflaksdjflkasdjflkajsdlfkajsdlfkjasdlfkj
asldkjflaksdjflkasdjflkajsdlfkajsdlfkjasdlfkj[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0.c
-bash: ./lab0.c: Permission denied
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world
y
hello world
y[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world
?
hello world
?[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) l
14	}
15	
16	
17	int main(int argc, char **argv)
18	{
19	
20	
21	  int c;
22	  int options_index;
23	  char *input_file = NULL;
(gdb) 
24	  char *output_file = NULL;
25	  static int segflag = 0;
26	  static int catchflag = 0;
27	  while(1)
28	    {
29	      static struct option long_options[] = 
30		{
31		  {"input", required_argument, 0, 'i'},
32		  {"output", required_argument, 0, 'o'},
33		  {"segfault", no_argument, &segflag, 1},
(gdb) 
34		  {"catch", no_argument, &catchflag, 1},
35		  {0,0,0,0}
36		};
37	
38	      options_index = 0;
39	      c = getopt_long(argc, argv, "iosc", long_options, &options_index);
40	      if(c == -1) 
41		break;
42	      
43	      switch(c)
(gdb) 
44		{
45		case 'i':
46		  input_file = optarg;
47		  break;
48		case 'o':
49		  output_file = optarg;
50		  break;
51		case 0:
52		  break;
53		default:
(gdb) 
54		  fprintf(stderr, "Incorrect argument used. Usage: ./lab0 --<argument>\nArguments: input, output, segfault, catch\nExiting with exit code *1*\n");
55		  exit(1);
56		  break;
57		}
58	
59	    }
60	
61	
62	  //if --catch option is used
63	  if(catchflag != 0)
(gdb) 
64	    {
65	
66	      signal(SIGSEGV, signalhandler);
67	      
68	      
69	    }
70	
71	
72	
73	
(gdb) 
74	  //if --segfault option is used, cause a segfault
75	  if(segflag != 0)
76	    {
77	      char *null = NULL;
78	      *null = 'k';
79	    }
80	
81	
82	
83	
(gdb) 
84	  
85	  int fd0, fd1;
86	
87	  char data[256];
88	  int nbytes = sizeof(data);
89	
90	
91	  //If --input option is used, read from a file
92	  if(input_file)
93	    {
(gdb) 
94	
95	      fd0 = open(input_file, O_RDONLY);
96	      if(fd0 < 0)
97		{
98		  fprintf(stderr, "Problem with --input. Unable to open file %s. Exiting with exit code *2*\n", input_file);
99		  exit(2);
100		}
101	      read(fd0, data, nbytes);
102	    }
103	
(gdb) 
104	
105	
106	
107	  //Otherwise, read from stdin
108	
109	  else if(read(0, data, nbytes) < 0)
110		{
111		  fprintf(stderr, "Error reading from stdin. Exiting with code *1*\n");
112		  exit(2);
113		}
(gdb) 
114	      
115	  data[strlen(data)-sizeof(char)] = '\0';
116	  printf("data is %s\n", data);
117	
118	  //If --output is used, create a file to write to
119	  if(output_file)
120	    {
121	
122	      fd1 = creat(output_file, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
123	      if(fd1 < 0)
(gdb) 
124		{
125		  fprintf(stderr, "Error creating file %s. Exiting with exit code *3*\n", output_file);
126		  exit(3);
127		}
128	      write(fd1, data, strlen(data));
129	
130	 
131	    }
132	
133	
(gdb) b 109
Breakpoint 1 at 0x4009f6: file lab0.c, line 109.
(gdb) r
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 

Breakpoint 1, main (argc=1, argv=0x7fffffffe398) at lab0.c:109
109	  else if(read(0, data, nbytes) < 0)
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) s
hello world
115	  data[strlen(data)-sizeof(char)] = '\0';
(gdb) p data
$1 = "hello world\n\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>"\214, \004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>"\200, \v@", '\000' <repeats 13 times>"\203, \006@\000\000\000\000"
(gdb) s
116	  printf("data is %s\n", data);
(gdb) p data
$2 = "hello world\n\377\000\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>"\214, \004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>"\200, \v@", '\000' <repeats 13 times>"\203, \006@\000\000\000\000"
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 

Breakpoint 1, main (argc=1, argv=0x7fffffffe398) at lab0.c:109
109	  else if(read(0, data, nbytes) < 0)
(gdb) s

115	  data[strlen(data)-sizeof(char)] = '\0';
(gdb) 
116	  printf("data is %s\n", data);
(gdb) p data
$3 = "\n!\242\v\000\000\000\000\230\333\377\367\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>"\214, \004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>"\200, \v@", '\000' <repeats 13 times>"\203, \006@\000\000\000\000"
(gdb) 
$4 = "\n!\242\v\000\000\000\000\230\333\377\367\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>"\214, \004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>"\200, \v@", '\000' <repeats 13 times>"\203, \006@\000\000\000\000"
(gdb) s
data is 
!?

119	  if(output_file)
(gdb) q
A debugging session is active.

	Inferior 1 [process 26075] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world

hello world
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
alskdflaksdflaksdflaksjdf
data is alskdflaksdflaksdflaksjdf
?
alskdflaksdflaksdflaksjdf
?[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0as
-bash: ./lab0as: No such file or directory
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
alskdfjlkasjdflkasldkfjalskdflaksdjf
data is alskdfjlkasjdflkasldkfjalskdflaksdj
alskdfjlkasjdflkasldkfjalskdflaksdj[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
alsdjflkasdfjlasjflkaflkasjdlfkasjd
data is alsdjflkasdfjlasjflkaflkasjdlfkasj
alsdjflkasdfjlasjflkaflkasjdlfkasj[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
data is hello world

hello world
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
aslkdfjlkasdflkasdjflkasjdfalskdfjlkasdf
data is aslkdfjlkasdflkasdjflkasjdfalskdfjlkasdf
??	
aslkdfjlkasdflkasdjflkasjdfalskdfjlkasdf
??	[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) b 110
Breakpoint 1 at 0x400a15: file lab0.c, line 110.
(gdb) r
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 
hello world
data is hello world

hello world

Program exited normally.
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) b 109
Breakpoint 2 at 0x4009f6: file lab0.c, line 109.
(gdb) r
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 

Breakpoint 2, main (argc=1, argv=0x7fffffffe398) at lab0.c:109
109	  else if(read(0, data, nbytes) < 0)
(gdb) s
hello world
115	  data[strlen(data)-2*sizeof(char)] = '\0';
(gdb) p data
$1 = "hello world\n\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>"\214, \004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>"\200, \v@", '\000' <repeats 13 times>"\203, \006@\000\000\000\000"
(gdb) q
A debugging session is active.

	Inferior 1 [process 26108] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  file.txt~  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
lab0.c: In function ‘main’:
lab0.c:118: warning: comparison between pointer and integer
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0.c
-bash: ./lab0.c: Permission denied
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
Segmentation fault
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
hello world
hello world
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
aldskjflkasdjflkasdjflkasdjf
aldskjflkasdjflkasdjflkasdjf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
asdkjflkasjflkasdjflaskdjflkasdjf
asdkjflkasjflkasdjflaskdjflkasdjf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
fuck youuuuuuu
fuck youuuuuuu
[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) l
14	}
15	
16	
17	int main(int argc, char **argv)
18	{
19	
20	
21	  int c;
22	  int options_index;
23	  char *input_file = NULL;
(gdb) 
24	  char *output_file = NULL;
25	  static int segflag = 0;
26	  static int catchflag = 0;
27	  while(1)
28	    {
29	      static struct option long_options[] = 
30		{
31		  {"input", required_argument, 0, 'i'},
32		  {"output", required_argument, 0, 'o'},
33		  {"segfault", no_argument, &segflag, 1},
(gdb) 
34		  {"catch", no_argument, &catchflag, 1},
35		  {0,0,0,0}
36		};
37	
38	      options_index = 0;
39	      c = getopt_long(argc, argv, "iosc", long_options, &options_index);
40	      if(c == -1) 
41		break;
42	      
43	      switch(c)
(gdb) 
44		{
45		case 'i':
46		  input_file = optarg;
47		  break;
48		case 'o':
49		  output_file = optarg;
50		  break;
51		case 0:
52		  break;
53		default:
(gdb) 
54		  fprintf(stderr, "Incorrect argument used. Usage: ./lab0 --<argument>\nArguments: input, output, segfault, catch\nExiting with exit code *1*\n");
55		  exit(1);
56		  break;
57		}
58	
59	    }
60	
61	
62	  //if --catch option is used
63	  if(catchflag != 0)
(gdb) 
64	    {
65	
66	      signal(SIGSEGV, signalhandler);
67	      
68	      
69	    }
70	
71	
72	
73	
(gdb) 
74	  //if --segfault option is used, cause a segfault
75	  if(segflag != 0)
76	    {
77	      char *null = NULL;
78	      *null = 'k';
79	    }
80	
81	
82	
83	
(gdb) 
84	  
85	  int fd0, fd1;
86	
87	  char data[256];
88	  int nbytes = sizeof(data);
89	
90	
91	  //If --input option is used, read from a file
92	  if(input_file)
93	    {
(gdb) 
94	
95	      fd0 = open(input_file, O_RDONLY);
96	      if(fd0 < 0)
97		{
98		  fprintf(stderr, "Problem with --input. Unable to open file %s. Exiting with exit code *2*\n", input_file);
99		  exit(2);
100		}
101	      read(fd0, data, nbytes);
102	    }
103	
(gdb) 
104	
105	
106	
107	  //Otherwise, read from stdin
108	
109	  else if(read(0, data, nbytes) < 0)
110		{
111		  fprintf(stderr, "Error reading from stdin. Exiting with code *1*\n");
112		  exit(2);
113		}
(gdb) 
114	
115	
116	  int newlineflag=0;
117	  int i = 0;
118	
119	
120	  for(i = 0; i < strlen(data); i++)
121	    {
122	      if(data[i] == '\n')
123		  newlineflag = 1;
(gdb) 
124	      if(newlineflag == 1)
125		{
126		data[i+1] = '\0';
127		break;
128		}
129	    }
130	
131	
132	  //If --output is used, create a file to write to
133	  if(output_file)
(gdb) 
134	    {
135	
136	      fd1 = creat(output_file, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
137	      if(fd1 < 0)
138		{
139		  fprintf(stderr, "Error creating file %s. Exiting with exit code *3*\n", output_file);
140		  exit(3);
141		}
142	      write(fd1, data, strlen(data));
143	
(gdb) b 116
Breakpoint 1 at 0x400a03: file lab0.c, line 116.
(gdb) r
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 
hello world

Breakpoint 1, main (argc=1, argv=0x7fffffffe398) at lab0.c:116
116	  int newlineflag=0;
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) p data
$1 = "hello world\n\377\177\000\000\220!\242\v8\000\000\000\230\333\377\367\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>, "t\004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>, "p\v@\000\000\000\000"
(gdb) s
117	  int i = 0;
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
120	  for(i = 0; i < strlen(data); i++)
(gdb) 
122	      if(data[i] == '\n')
(gdb) 
123		  newlineflag = 1;
(gdb) 
124	      if(newlineflag == 1)
(gdb) 
126		data[i+1] = '\0';
(gdb) 
127		break;
(gdb) 
133	  if(output_file)
(gdb) p data
$2 = "hello world\n\000\177\000\000\220!\242\v8\000\000\000\230\333\377\367\377\177\000\000.N=\366\000\000\000\000j\242\200\v8", '\000' <repeats 11 times>"\230, \333\377\367\377\177\000\000\001", '\000' <repeats 15 times>, "\001\000\000\000\000\000\000\000\220!\242\v8\000\000\000X\342\377\377\377\177\000\000U\000\000\000\000\000\000\000\t\000\000\000\000\000\000\000n\342\377\377\377\177\000\000\000\000\000\000\000\000\000\000\350$\242\v8\000\000\000\200\342\377\377\377\177\000\000\347\003\311\v8\000\000\000\230\342\377\377\377\177\000\000\000\000\000\000\001", '\000' <repeats 11 times>, "t\004@\000\000\000\000\000\302\000\000\000\000\000\000\000n\342\377\377\377\177\000\000o\342\377\377\377\177\000\000\001", '\000' <repeats 15 times>, "M\006\311\v8", '\000' <repeats 11 times>, "p\v@\000\000\000\000"
(gdb) q
A debugging session is active.

	Inferior 1 [process 26675] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ l
-bash: l: command not found
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  file.txt~  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
lasjdflakjsdflkjasdlfkjasdlkfjasdlkfjasldkfjalskdfjladksjf
lasjdflakjsdflkjasdlfkjasdlkfjasdlkfjasldkfjalskdfjladksjf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --input file.txt
hello world
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --output file1.txt
alskdfjalsfkjsadlf
[seanl@lnxsrv01 ~/cs111/project0]$ cat file1.txt 
alskdfjalsfkjsadlf
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file1.txt  file.txt  file.txt~  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ rm file1.txt 
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  file.txt~  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ make clean
rm lab0
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400940 in main (argc=2, argv=0x7fffffffe378) at lab0.c:78
78	      *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) bt
#0  0x0000000000400940 in main (argc=2, argv=0x7fffffffe378) at lab0.c:78
(gdb) k
Kill the program being debugged? (y or n) y
(gdb) r --segfault --catch
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault --catch

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400940 in main (argc=3, argv=0x7fffffffe378) at lab0.c:78
78	      *null = 'k';
(gdb) s
signalhandler (signum=0) at lab0.c:11
11	{
(gdb) s
12	  fprintf(stderr, "Segmentation fault caught with signal. Exiting with exit code *4*\n");
(gdb) 
Segmentation fault caught with signal. Exiting with exit code *4*
13	  exit(4);
(gdb) 

Program exited with code 04.
(gdb) 
The program is not being run.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400940 in main (argc=2, argv=0x7fffffffe378) at lab0.c:78
78	      *null = 'k';
(gdb) s

Program terminated with signal SIGSEGV, Segmentation fault.
The program no longer exists.
(gdb) t
No thread selected
(gdb) bt
No stack.
(gdb) clear
No breakpoint at this line.
(gdb) clean
Undefined command: "clean".  Try "help".
(gdb) 
Undefined command: "clean".  Try "help".
(gdb) q
[seanl@lnxsrv01 ~/cs111/project0]$ clear

[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400940 in main (argc=2, argv=0x7fffffffe378) at lab0.c:78
78	      *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) bt
#0  0x0000000000400940 in main (argc=2, argv=0x7fffffffe378) at lab0.c:78
(gdb) q
A debugging session is active.

	Inferior 1 [process 26751] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0
laskdjflakdf
laskdjflakdf
[seanl@lnxsrv01 ~/cs111/project0]$ ./lab0 --segfault
Segmentation fault
[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x000000000040085d in segfault () at lab0.c:21
21	  *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) bt
#0  0x000000000040085d in segfault () at lab0.c:21
#1  0x000000000040094e in main (argc=2, argv=0x7fffffffe378) at lab0.c:84
(gdb) q
A debugging session is active.

	Inferior 1 [process 26765] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ clear

[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x000000000040085d in segfault () at lab0.c:21
21	  *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) bt
#0  0x000000000040085d in segfault () at lab0.c:21
#1  0x000000000040094e in main (argc=2, argv=0x7fffffffe378) at lab0.c:84
(gdb) k
Kill the program being debugged? (y or n) y
(gdb) l
16	
17	
18	void segfault(void)
19	{
20	  char *null = NULL;
21	  *null = 'k';
22	}
23	
24	int main(int argc, char **argv)
25	{
(gdb) 
26	
27	
28	  int c;
29	  int options_index;
30	  char *input_file = NULL;
31	  char *output_file = NULL;
32	  static int segflag = 0;
33	  static int catchflag = 0;
34	  while(1)
35	    {
(gdb) b 20
Breakpoint 1 at 0x400851: file lab0.c, line 20.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Breakpoint 1, segfault () at lab0.c:20
20	  char *null = NULL;
(gdb) p null
$1 = 0x380ba22190 ""
(gdb) p var
No symbol "var" in current context.
(gdb) p *null
$2 = 0 '\000'
(gdb) q
A debugging session is active.

	Inferior 1 [process 26814] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ clear

[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Program received signal SIGSEGV, Segmentation fault.
0x000000000040085d in segfault () at lab0.c:21
21	  *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) k
Kill the program being debugged? (y or n) 
Please answer y or n.
Kill the program being debugged? (y or n) y
(gdb) q
[seanl@lnxsrv01 ~/cs111/project0]$ clera
-bash: clera: command not found
[seanl@lnxsrv01 ~/cs111/project0]$ clear





































[seanl@lnxsrv01 ~/cs111/project0]$ gdb lab0
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /w/home.10/ee/ugrad/seanl/cs111/project0/lab0...done.
(gdb) l
21	  *null = 'k';
22	}
23	
24	int main(int argc, char **argv)
25	{
26	
27	
28	  int c;
29	  int options_index;
30	  char *input_file = NULL;
(gdb) b 21
Breakpoint 1 at 0x400859: file lab0.c, line 21.
(gdb) r --segfault
Starting program: /w/home.10/ee/ugrad/seanl/cs111/project0/lab0 --segfault

Breakpoint 1, segfault () at lab0.c:21
21	  *null = 'k';
Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.209.el6_9.2.x86_64
(gdb) p *null
Cannot access memory at address 0x0
(gdb) p null
$1 = 0x0
(gdb) s

Program received signal SIGSEGV, Segmentation fault.
0x000000000040085d in segfault () at lab0.c:21
21	  *null = 'k';
(gdb) q
A debugging session is active.

	Inferior 1 [process 26825] will be killed.

Quit anyway? (y or n) y
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  file.txt~  lab0  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ make clean
rm lab0
[seanl@lnxsrv01 ~/cs111/project0]$ ls
file.txt  file.txt~  lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ rm file.txt
[seanl@lnxsrv01 ~/cs111/project0]$ rm file.txt~ 
[seanl@lnxsrv01 ~/cs111/project0]$ ls
lab0.c  lab0.c~  Makefile  Makefile~  README  README~
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ emacs Makefile
[seanl@lnxsrv01 ~/cs111/project0]$ make
gcc -g -o lab0 lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ emacs README
[seanl@lnxsrv01 ~/cs111/project0]$ emacs lab0.c
[seanl@lnxsrv01 ~/cs111/project0]$ cd ~/classes/old_labs/
[seanl@lnxsrv01 ~/classes/old_labs]$ ls
hw9.tgz  lab_1  lab_2  lab_3  lab_4  lab5  lab5_turnin  lab6_turnin  lab7_turnin  lab8  lab9  syscall.tgz
[seanl@lnxsrv01 ~/classes/old_labs]$ cd lab
-bash: cd: lab: No such file or directory
[seanl@lnxsrv01 ~/classes/old_labs]$ cd lab_1
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ ls
ans1.txt  key1.txt
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ emacs ans1.txt 
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ ls
ans1.txt  key1.txt
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ emacs key1
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ emacs key1.txt
[seanl@lnxsrv01 ~/classes/old_labs/lab_1]$ cd ..
[seanl@lnxsrv01 ~/classes/old_labs]$ ls
hw9.tgz  lab_1  lab_2  lab_3  lab_4  lab5  lab5_turnin  lab6_turnin  lab7_turnin  lab8  lab9  syscall.tgz
[seanl@lnxsrv01 ~/classes/old_labs]$ cd lab_2
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ ls
howework  lab2.log  spell_checking
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ cd howework/
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/howework]$ ls
a  b  c  d  e  sameln  sameln~
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/howework]$ emacs sameln
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/howework]$ ls
a  b  c  d  e  sameln  sameln~
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/howework]$ cd ..
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ ls
howework  lab2.log  spell_checking
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ emacs lab2.log 
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ ls
howework  lab2.log  spell_checking
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ cd spell_checking/
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/spell_checking]$ ls
assign2  assign2.html  assign2sort  buildwords  hwnwdseng.htm  hwords  hwordssort  text  words
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/spell_checking]$ cd buildwords 
-bash: cd: buildwords: Not a directory
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/spell_checking]$ emacs buildwords 
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/spell_checking]$ ls
assign2  assign2.html  assign2sort  buildwords  hwnwdseng.htm  hwords  hwordssort  text  words
[seanl@lnxsrv01 ~/classes/old_labs/lab_2/spell_checking]$ cd ..
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ ls
howework  lab2.log  spell_checking
[seanl@lnxsrv01 ~/classes/old_labs/lab_2]$ cd ..
[seanl@lnxsrv01 ~/classes/old_labs]$ ls
hw9.tgz  lab_1  lab_2  lab_3  lab_4  lab5  lab5_turnin  lab6_turnin  lab7_turnin  lab8  lab9  syscall.tgz
[seanl@lnxsrv01 ~/classes/old_labs]$ cd lab_3
[seanl@lnxsrv01 ~/classes/old_labs/lab_3]$ ls
coreutils-7.6  lab3_turnin
[seanl@lnxsrv01 ~/classes/old_labs/lab_3]$ cd lab3_turnin/
[seanl@lnxsrv01 ~/classes/old_labs/lab_3/lab3_turnin]$ ls
comm.py  comm.py~  hw3.txt  lab3.txt
[seanl@lnxsrv01 ~/classes/old_labs/lab_3/lab3_turnin]$ emacs comm.py

File Edit Options Buffers Tools Python Help                                                                                                                                                                 
#!/usr/bin/python                                                                                                                                                                                           


import random, sys
import string
import locale
from optparse import OptionParser

#File class, which stores the lines from each input file                                                                                                                                                    
class file:
    def __init__(self,filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def printlines(self):
        print(self.lines)
        return

    def __getitem__(self,i):
        return self.lines[i]
    def __len__(self):
        j=0
        for i in self:
            j=j+1
        return j


class line:

    def __init__(self,line):
        self.string=line
        self.column=0





def main():
    locale.setlocale(locale.LC_COLLATE, 'C')

    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2                                                                                                                                                            
                                                                                                                                                                                                            
Compare sorted files FILE1 and FILE2 line by line."""

#Parse the options and files, and store them in an array                                                                                                                                                    
#Options go into options, files go into args                                                                                                                                                                

    parser = OptionParser(version=version_msg, usage=usage_msg)
    parser.add_option("-1", action='store_true', dest="arg1", default=False,
                      help="suppress column 1 (lines unique to FILE1)")
    parser.add_option("-2", action='store_true', dest = "arg2", default=False,
                      help="suppress column 2 (lines unique to FILE2)")
    parser.add_option("-3", action='store_true', dest = "arg3", default=False,
                      help="suppress column 3 (lines that appear in both files)")
    parser.add_option("-u", action='store_true', dest = "arg4", default=False,
                      help="Output on unsorted files")
    options, args = parser.parse_args(sys.argv[1:])
#Check for parser errors    


    if len(args) != 2:
        parser.error("Wrong number of operands")



    file_1 = args[0]
    file_2 = args[1]

#Read input from file_1 and put the lines into file_1_lines                                                                                                                                                 
    file_1_lines = file(file_1)
    file_2_lines = file(file_2)



    strings1 = []
    strings2 = []
#Remove the newlines from file_1_lines and put the entries into strings1                                                                                                                                    
    for i in range(len(file_1_lines)):
        strings1.append(file_1_lines[i].rstrip('\n'))

    for i in range(len(file_2_lines)):
        strings2.append(file_2_lines[i].rstrip('\n'))

        #strings1 now contains all the lines from the first file                                                                                                                                            
        #strings2 contains all lines from second file                                                                                                                                                       



        #If the -u option isn't used, check if the files are sorted. If they aren't, then parser error                                                                                                      
    if options.arg4 == False:
    if strings1 != sorted(strings1):
            parser.error("First file is not sorted.")

        if strings2 != sorted(strings2):
            parser.error("Second file is not sorted.")



#Create new objects, lines1 and lines2, which contain the column informatoin for lines in each corresponding file                                                                                           
    lines1 = []
    lines2 = []

    for i in strings1:
        newline = line(i)
        lines1.append(newline)

    for i in strings2:
        newline = line(i)
        lines2.append(newline)

    #Check if lines are in both files                                                                                                                                                                       
    for i in lines1:
        for j in lines2:
            if i.string == j.string:
                i.column = 3
                j.column = 3

    #Check if the line is in the first file only     
    for i in lines1:
        in_both = False
        for j in lines2:
            if i.string == j.string:
                in_both = True
        if in_both == False:
            i.column = 1

    #Check if the line is in the second file only                                                                                                                                                           
    for i in lines2:
        in_both = False
        for j in lines1:
            if i.string == j.string:
                in_both = True
        if in_both == False:
            i.column = 2



    output = []

#If the unsorted option isn't used, the file is sorted, so put them into an output list                                                                                                                     
    if options.arg4 == False:

        for i in lines1:
            output.append(i)

        for i in lines2:
            if i.column != 3:
                output.append(i)


                #If the unsorted option is used, create a list outputting first file's order,                                                                                                               
                #then second file lines in the end                                                                                                                                                          

    if options.arg4 == True:
        for i in lines1:
            output.append(i)

        for i in lines2:
            if i.column != 3:
                output.append(i)




    newlist = sorted(output, key=lambda line: line.string)

    # for i in newlist:                                                                                                                                                                                     
    #     print i.string                                                                                                                                                                                    
    #     print i.column                                                                                                                                                                                    

    for i in newlist:
        if options.arg1 == False and i.column == 1:
            sys.stdout.write(i.string + '\n')

        if options.arg2 == False and i.column == 2:
            if options.arg1 == False:
                sys.stdout.write('\t')

            sys.stdout.write(i.string + '\n')
    if options.arg3 == False and i.column == 3:
            if options.arg1 == False:
                sys.stdout.write('\t')
            if options.arg2 == False:
                sys.stdout.write('\t')
            sys.stdout.write(i.string + '\n')





if __name__ == "__main__":
    main()
