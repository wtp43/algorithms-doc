## GPU

- power limit 
```shell
limit=211
for i in $(seq 0 5);
do
nvidia-smi -i $i -pl $limit
done
```


## CPU
### Clock Cycles
A CPU with a clock speed of 3.2 GHz executes 3.2 billion cycles per second.
If you run perfectly parallelizable processes, then a three-core CPU can effectively perform operations at three times the capacity of a single-core CPU at the same clock speed.

## RAM

ECC stands for Error Correcting Code. The RAM has extra bits in memory that it uses to compare what's being written to it, and make corrections if they don't match up. It's a little more complex than that and you can read about different methods on Wikipedia, but this is the gist of what it does.

Registered (aka buffered) memory does a different task. It places an area of ultra fast memory between the system's CPU memory controller and the RAM itself. It takes some of the load off the memory controller. Generally this isn't an issue with desktops and laptops which usually support two or for sticks of RAM max. The controller isn't going to get bogged down. In servers with lots of ram modules, it can help maintain system stability.


### RDIMM: Registerd DIMM
RDIMMs use a register (also called a register chip) to buffer the address and command signals between the memory controller and the memory chips. This reduces the electrical load on the memory controller, allowing the system to support more memory modules and maintain stability.
### LRDIMM: Load-Reduced DIMM
- LRDIMMs go a step further by using a memory buffer chip, which buffers not only the address and command signals but also the data signals. This significantly reduces the load on the memory bus, enabling the use of even higher capacity memory modules and improving overall system scalability.
- supports much higher memory capacities than RDIMM

### Timings/CAS Latency
CL: tRCD: tRP: tRAS
- CAS Latency
	-  # of clock cycles to respond to a read cycle
- RAS to CAS Delay
	-  # of clock cycles required between activation of a row of memory and reading or writing of data to that row
- Row Precharge Time
	-  # of clock cycles needed to deactivate a row of memory before another row can be activated
- Row Active Time
	- Minimum # of clock cycles that a row must remain active to ensure data integrity before it can be closed
Lower is better
Higher clock speeds can compensate for higher timings