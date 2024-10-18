"""
Name : Prabash 
      
"""


def is_the_list_in_order(lst):
    """If the list is empty or contains only one element, it is considered in order"""
    if len(lst) <= 1:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

