from itertools import combinations
from statistics import mean, median

def max_val(n, a):
    max_value = float('-inf')
    for r in range(1, n+1):  
        for comb in combinations(a, r):
            mean_val = mean(comb)
            median_val = median(comb)
            val_s = mean_val - median_val
            if val_s > max_value:
                max_value = val_s
    
    return max_value
