def last_element(lst):
    """Return last item in list (None if list is empty.
    """
    if len(lst) == 0:
        return"None"
    else:   
        return lst[len(lst)-1]


print(last_element([1,2,3,4,5,6,7,8,9,1245,3525,236,2346342,634]))