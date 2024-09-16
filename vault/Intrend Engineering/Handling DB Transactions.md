https://www.reddit.com/r/golang/comments/148uc6v/how_did_you_solve_the_problem_of_transactions/l


This is far beyond Go and is a legitimately hard problem. This is coming from someone who has worked on an eventually consistent distributed data store for years.

One of the many issues involved is the situation where other changes are happening while the "transaction" is going on, so a rollback will wipe out or invalidate or otherwise affect intermediate changes. Even a successful transaction will potentially do that to smaller changes that begin and end inside the lifetime of the larger transaction. You basically have the same problem as merge conflicts in git, except you can't just bail out and say, "let the humans sort it out" like git does.

One way to solve that particular issue is by restricting your operations to only commutative ones: operations that end up giving the same result regardless of the order they're applied. This has implications on available data models - for example, you can't have sequences (two operations of "insert into index 3" will overwrite each other so the last one wins, so order always matters), but you can have set insertion (inserting two elements consecutively will always have those two items in the set regardless of the order), etc. The technical name for this approach is [CRDT](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type).

In order for the results to be correct, you also need to make sure that the successful operation and its inverse (the rollback) are both commutative so that you can mix and match all of them.

And that's all before you consider that the different services will have different availability - that one might be down and needs to retry while the other services are in limbo. Causing a number of different systems to independently converge on eventual consistency to each other... that's a beast of a problem.

There's no general solution to this problem - you'll need tradeoffs.


## Ingest/Buffer Tables
  https://www.reddit.com/r/mysql/comments/1cksiu0/need_to_store_data_fast_in_ram_for_later_bulk/
the idea is different database servers for the ingest. increase throughput. and then they hold the backlog for prod to handle. so you can record them in real time and then process into the main db at a manageable speed. doing bulk inserts of 50/100/etc records at once to the main db instead of 100 individual inserts will also be faster. so hammer the crap out of the intake dbs and then do the bulk processing and inserts from there to the primary db. you can scale up and won’t exhaust open connections that way either.

do a round robbin type approach on which intake to send data to on each request. and you can add more as needed. it’s cheaper to scale horizontally than it is vertically. so a bunch of low end ingest dbs will be cheaper than one high end db to handle same load. memory is expensive

but i do have to say. mysql is prob not the answer for ingest. something like lavinmq, rabbitmq, etc would be better (not redis because your massive amounts of data coming in would require too much memory). need one that primarily works from disk. i use lavinmq for my queues and love it. handle millions of jobs with barely and memory usage and hdd is super cheap

## 