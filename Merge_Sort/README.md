# Merge Sort Implementation in Python

This repository contains a simple implementation of the **Merge Sort** algorithm using Python. Merge Sort is a classic divide-and-conquer algorithm that recursively splits the list into smaller sublists and merges them in sorted order.

## 📂 File Description

- `merge_sort.py` – Contains the implementation of the merge sort algorithm.

## 🚀 How It Works

1. The input list is split into two halves recursively until each sublist has a single element.
2. These sublists are then merged in sorted order.

## 🧪 Example

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]


Output:


Unsorted array: 
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array: 
[1, 2, 4, 5, 6, 8, 10, 14]
🔧 How to Run
bash
Copy code
python merge_sort.py
📌 Note
Make sure you're using Python 3.x to run this script.

🧠 Algorithm Time Complexity
Best-case performance: O(n log n)

Average-case performance: O(n log n)

Worst-case performance: O(n log n)

Space complexity: O(n)