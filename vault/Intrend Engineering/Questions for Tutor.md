- batch process async lock?
	- mutex = system wide lock, shared by multiple processes
	- semaphore = lock that can be acquired by one thread and released by a different thread (not possible to do with a normal lock)
	- read/write = allows unlimited number of readers or 1 writer
	- spinlock: no thread sleeping, mostly used at kernel level, inefficient for user level code

- instantiating new responseparser vs shared object and passed around
	- what overhead operations do I need to consider?
- how to properly benchmark?

- what importing files really is 
	- what is stored in memory and when does it happen
	
https://stackoverflow.com/questions/2332765/what-is-the-difference-between-lock-mutex-and-semaphore