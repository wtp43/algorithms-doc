## GPU

- power limit 
```shell
limit=211
for i in $(seq 0 5);
do
nvidia-smi -i $i -pl $limit
done
```