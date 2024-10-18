"""
Name : Prabash 
      
"""


def are_all_members_same(lst):
    """If the list is empty, return True"""
    if not lst:
        return True

    return all(element == lst[0] for element in lst)

