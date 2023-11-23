
# Partition Function

## Overview
The `partition` function is a utility used for sorting and organizing elements within a list. It implements a crucial step in the QuickSort algorithm by rearranging elements in a list based on a pivot element. Elements smaller than the pivot are moved to its left, and those larger are moved to its right. This function is an essential building block for efficient sorting algorithms.

## Function Details
- **Function Name**: `partition`
- **Parameters**:
  - `work`: The list of elements to be partitioned.
  - `begin`: The starting index of the segment of the list to be partitioned.
  - `end`: The ending index (exclusive) of the segment of the list to be partitioned.
  - `pivot`: The index of the pivot element.
- **Returns**: The final index position of the pivot element after partitioning.

## Usage
To use the `partition` function, you need to provide a list (`work`) and specify the segment of the list to be partitioned by providing `begin`, `end`, and `pivot` indices.

Example:
```python
work_list = [12, 7, 14, 9, 10, 11]
pivot_index = 3  # Choosing an index as pivot
final_pivot_position = partition(work_list, 0, len(work_list), pivot_index)
print("Final Pivot Position:", final_pivot_position)
print("Partitioned List:", work_list)
```
