---
inclusion: always
---

# Code Organization Standards

This project uses an intelligent code file organizer that classifies coding files into topic-based folders.

## Classification System

The organizer uses keyword-based classification with regex patterns to analyze:
- File content (comments, variable names, function names)
- Filenames and their semantic meaning
- Code structure and algorithms used

## Supported Topics

- **Arrays**: Array manipulation, sorting, searching within arrays
- **Strings**: String processing, pattern matching, palindromes
- **LinkedList**: Linked list operations and algorithms
- **Trees**: Binary trees, BST, tree traversals
- **Graphs**: Graph algorithms, DFS, BFS, shortest paths
- **DynamicProgramming**: DP problems, memoization, optimization
- **Recursion**: Recursive algorithms, backtracking
- **Sorting**: Sorting algorithms implementations
- **Searching**: Search algorithms (binary search, etc.)
- **HashTable**: Hash-based data structures
- **Stack/Queue/Heap**: Linear and priority-based data structures
- **Math**: Mathematical algorithms
- **BitManipulation**: Bitwise operations
- **Greedy**: Greedy algorithms

## Best Practices

1. Always run with `--dry-run` first to preview changes
2. Keep original files intact (script copies, not moves)
3. Review classification results and adjust keywords if needed
4. Use descriptive filenames that hint at the problem type
5. Include comments in code that describe the algorithm/data structure used

## Customization

To modify topic categories or keywords, edit the `TOPIC_KEYWORDS` dictionary in `CodeOrganizer` class.
