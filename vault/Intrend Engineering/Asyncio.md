https://stackoverflow.com/questions/75349496/using-httpx-to-send-100k-get-requests
https://www.youtube.com/watch?v=E_oIU4IU2W9
## Asyncio.Queue

### Asynchronously produce and batch consume
```python
import asyncio

queue = asyncio.Queue()
async def producer():
    for i in range(1, 7):
        await queue.put(i)
        print(f"Produced item {i}")
        await asyncio.sleep(0.5)
        
async def consumer():
    while True:
        if queue.qsize() < 3:
            await asyncio.sleep(0)
            continue
        tasks = [asyncio.create_task(queue.get()) for _ in range(3)]
        items = await asyncio.gather(*tasks)
        print(f"Consumed items {items}")
        await asyncio.sleep(1)
async def main():
    tasks = [asyncio.create_task(producer()), asyncio.create_task(consumer())]
    await asyncio.gather(*tasks)
asyncio.run(main())

```

### Synchronous Tasks
```python
await loop.run_in_executor(...)
```
