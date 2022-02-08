def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = 0
    for i in lst:
        if i == search_term: count += 1
    return count

print(frequency([1,2,3,4,5,6,7,7,6,5,4,7,7,7,7,7,7], 7))