# Unsupervised Learning 
>  Learns through unlabeled data
- Extracts structure in the data

##  Clustering
- Group a set of objects in such a way that similar objects fall into the same group

using unsupervised learning to cluster time series and use the cluster to forecast .


## Time Series Clustering
### Time Series k-means
- 3 variants: Euclidean, Dynamic Time Warping(DTW), Soft-DTW
#### Dynamic Time Warping
- Measures similarity between two temporal sequences that do not align exactly in time, speed, or length
#### Cluster Evaluation
- Silhouette Score: $s=\frac{b-a}{max(a,b)}$ where $a =$  Mean distance between a sample and all other points in the same class, $b=$ mean distance between a sample and all other points in the next nearest cluster
- The score is bounded between -1 for incorrect clustering and +1 for highly dense clustering
- Scores around 0 indicate overlapping clusters
### Kernel k-means
- Limitations: cluster centroid/center can't be computed

### KShape
- based on cross correlation to cluster time series

## Temporal Clustering

The goal of temporal clustering is to create a method that can self-cluster identical mobility trends. A **clustering framework** was thus developed to achieve this task.
![](https://miro.medium.com/v2/resize:fit:1105/1*ZukNcXRp66qLX8_aE8dnsw.png)

# Part 2: Spatial Clustering

Spatial clustering aims to identify places of the same trend for each time cluster. With the time clusters produced from Part 1, I would obtain the **weekly trend line** for each cell and perform spatial clustering using similar framework for temporal.
https://towardsdatascience.com/time-series-clustering-deriving-trends-and-archetypes-from-sequential-data-bb87783312b4
# Trend Analysis

Data preprocessing technique is developed to remove the unwanted noises.
• Dynamic time wrapping discovers the correlation within the data objects for
cluster formation.


Trend analysis using agglomerative hierarchical clustering…
• Agglomerative hierarchical clustering algorithm is developed the map to reduce
framework for forming the time sequence data-based clustering.
• Trend analysis is utilized to predict the factors for finding the road accidents
location.



### Intrend
Classification:
- Timeless trend
- Dying trend
- Pre trend
- In trend
- Not a trend

Object:
- Image count rate increase over 1 month
- Image count rate increase over 6 month
- Season
- 

- given a set of objects ()