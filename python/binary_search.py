"""
Binary Search Implementation

- List must be ordered

"""


def binary_search(search_list, search_item):
    """
    Given an ordered list find the search_item.

    Complexity
    - Best: O(1)
    - Average: O(log n)
    - Worst: O(log n)
    """
    
    li_len = len(search_list)
    
    mid_idx = li_len / 2
    mid_val = search_list[mid_idx]

    if li_len == 1 and mid_val != search_item:
        return None
    
    if mid_val == search_item:
        return mid_val
    elif search_item < mid_val:
        return binary_search(search_list[:mid_idx], search_item)
    elif search_item > mid_val:
        return binary_search(search_list[(mid_idx+1):], search_item)

