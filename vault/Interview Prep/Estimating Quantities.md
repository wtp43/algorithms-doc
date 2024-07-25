# Estimating Quantities 

Source: https://www.hellointerview.com/blog/mastering-estimation
## Process
1. **Determine What to Estimate**: Figure out which quantities are load-bearing for your design.
	- Start with the crux
    
2. **Break It Down**: Start with a big problem. Slice it into smaller pieces.
    - Estimate usage amount given relationship between entities in the system 
3. **Use What You Know**: Apply basic principles and facts you're confident about.

> [!tip]
> Stick to factors of 1,000 for your interview.

Having a solid base for your mental math is important. Don't be the candidate who gets stuck trying to remember that 1 million bytes is 1mb!

### Metrics 

| Power of 1000 | Number      | Prefix |
| ------------- | ----------- | ------ |
| 0             | Unit        |        |
| 1             | Thousand    | Kilo   |
| 2             | Million     | Mega   |
| 3             | Billion     | Giga   |
| 4             | Trillion    | Tera   |
| 5             | Quadrillion | Peta   |

### Latencies

| Action                                               | Time   | Comparison |
| ---------------------------------------------------- | ------ | ---------- |
| Reading 1mb sequentially from memory                 | 0.25ms |            |
| Reading 1mb sequentially from SSD                    | 1ms    | 4x memory  |
| Reading 1mb sequentially from spinning disk          | 20ms   | 20x SSD    |
| Round trip network latency CA to Netherlands         | 150ms  |            |

### Storage

| Item                                                 | Size   |            |
| ---------------------------------------------------- | ------ | ---------- |
| A two-hour movie                                     | 1gb    |            |
| A small book of plain text                           | 1mb    |            |
| A high-resolution photo                              | 1mb    |            |
| A medium-resolution image (or a site layout graphic) | 100kb  |            | 4. **Keep It Simple**: Stick to round numbers. Precision isn't the goal; ballpark is.
    
5. **Check Yourself**: Does your answer make sense in the real world? 


### Common Mistakes

Estimation takes some practice and likely will only occupy 1-3 minutes of your 35-minute interview. But there are a few things you should try to avoid:

1. **Estimating something that doesn't matter.** Remember the crux of your problem and focus your estimation on that rather than doing estimation for its own sake.
    
2. **Getting stuck in the math.** Nothing is more frustrating than failing to remember simple arithmetic on the spot in an interview, so nothing could be more foolish than making things harder than they need to be.
    
3. **Getting quantities outrageously wrong (small mistakes are ok!).** If you think network calls over the internet take microseconds or a gigabyte of data can't easily fit in memory, your interviewer might doubt your fundamentals.

## Core Entities (~2 mins)
- Start with a small list and iterate as you go

## API or System Interface (~5 mins)
- Data flow

## High Level Design (~10-15 minutes)


## Deep Dives (~10 minutes)


> [!NOTE] 
> A common mistake candidates make is that they try to talk over their interviewer here. There is a lot to talk about, sure, and for senior candidates being proactive is important, however, it's a balance. Make sure you give your interviewer room to ask questions and probe your design. Chances are they have signal they want to get from you and you're going to miss it if you're too busy talking. Plus, you'll hurt your evaluation on [Communication and Collaboration](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery#communication-and-collaboration).
