def min_subsequences(source, target):
    source_set = set(source)
    
    for char in target:
        if char not in source_set:
            return -1

    i, count = 0, 1
    for char in target:
        if char in source[i:]:
            i = source.index(char, i) + 1
        else:
            count += 1
            i = source.index(char) + 1
            
    return count
