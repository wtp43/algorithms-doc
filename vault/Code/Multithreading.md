# Multi-threading

## Locks
**In semaphore, mutex will have value 1 or 0, but if used as counting semaphore it can have different values**. In uniprocessor system spinlock are not very useful because they will keep the processor busy every time while polling for the lock , thus disabling any other process from running.


### Read Write Lock vs Mutex
When you lock a mutex, you get mutable access to the contained data. In Rust, mutable references are unique, so no other thread has access.

When you lock an RwLock, you choose whether you want immutable or mutable access. Similar to Rust's borrowing rules, a RwLock either has 1 writer, or many readers, but never both at the same time.

All of these operations acquire a lock, and are relatively slow (lock acquisition overhead is likely totally acceptable in a web server, but probably bad in a tight loop).

Mutex can be unnecessarily restrictive in read-heavy contexts

Mutex is Sync in more cases than RwLock

RwLock can cause writer starvation, where readers consistently keep acquiring the lock and don't let writers "get a turn". Though this behaviour is platform specific, and some platforms have mechanisms in place to prevent this. Mutex cannot have this issue, as it doesn't distinguish between readers and writers