

The main problem I ran into was properly implementing the thread splitting in the my threadfunction.
The trickiest part of this lab was understanding the implementation of the given 
ray tracing program, and trying to understand how to implement parallelism
around this complicated program. The solution ended up being not that difficult, as a majority
of it involved copying code from the original main function.

Another issue I ran into was deciding which variables should be implemented as global, which
involves thinking which variables have to be involved for each thread.

SRT's performance was greatly improved after implementing parallelism. Doubling the thread
count effectively cut the run time in half, which is amazing considering the original 
run time was 41 seconds long!
