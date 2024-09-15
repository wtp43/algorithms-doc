# Self-hosting


## MinIO S3 with Tailscale
- Raid not needed
- Allows different sized drives
- MinIO cluster offers resiliance through redundancy 

- **Replication**:
    
    - MinIO replicates entire objects across clusters. This means you can use drives of different sizes, and MinIO will distribute the data across them based on the available capacity. However, if one drive fills up, MinIO won't be able to use that drive until space is freed.
    - **Use Case**: Replication is useful for backup across multiple servers or clusters. You can use different-sized drives on your NAS and desktop without any issues.
### Limitations
- **You Can’t Add New Drives**: Once your cluster is set up, you can’t just add more drives to it to increase storage.
- **You Can’t Add More Nodes**: If you have a distributed MinIO setup across multiple nodes, you can’t expand the cluster by adding more nodes to increase capacity.
- More drives can be added however when you migrate to a new cluster

- **Erasure Coding**:
    - MinIO uses erasure coding to split objects into data and parity blocks, distributing them across the available drives. While erasure coding works with different-sized drives, the overall capacity you get will depend on the smallest drive in the pool, as erasure coding needs to distribute data blocks evenly across all drives.
    - **Use Case**: You can still use different-sized drives, but the effective storage utilization will be limited by the smallest drive in the set.
    
    **Example**:
    
    - If you have three drives: 4TB, 6TB, and 8TB, the smallest drive (4TB) will be the limiting factor in terms of storage efficiency. The additional space on the larger drives will not be fully utilized in an erasure-coded setup.
### Setup
- Main storage: PC
- Backup: NAS


