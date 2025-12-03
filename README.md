# 🗂️ Code File Organizer

> **"I hate organizing 200+ coding practice files, so I built this."**

Automatically organize messy coding files (.cpp, .py, .java) into topic-based folders using intelligent keyword-based classification. Built with Kiro AI assistance for rapid development.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI for Bharat](https://img.shields.io/badge/AI%20for%20Bharat-Week%202-orange.svg)](https://aiforBharat.org)

## 🎯 The Problem

Ever had a folder with hundreds of coding practice files named `test.cpp`, `solution2.py`, `final_final.java`? Searching for that binary search solution you wrote last month becomes a nightmare. Manual organization is tedious and time-consuming.

## ✨ The Solution

An intelligent Python script that reads your code files, analyzes their content, and automatically organizes them into topic-based folders like Arrays, Trees, Graphs, Dynamic Programming, and more!

## ✨ Features

- 🤖 **Automatic Classification**: Analyzes file content and filenames using 100+ regex patterns
- 📁 **16 Topic Categories**: Arrays, Strings, LinkedList, Trees, Graphs, DynamicProgramming, Recursion, Sorting, Searching, HashTable, Stack, Queue, Heap, Math, BitManipulation, Greedy, and Miscellaneous
- 🎯 **Smart Detection**: Uses keyword scoring algorithm to determine the best topic match
- 🛡️ **Safe Operation**: Copies files (preserves originals) with dry-run mode available
- ⚡ **Zero Dependencies**: Uses only Python standard library
- 🚀 **Fast**: Processes hundreds of files in seconds
- 🔧 **Customizable**: Easy to add new topics or modify keywords

## 🤖 Built with Kiro AI

This project was developed with assistance from Kiro AI, which accelerated development by:
- Generating comprehensive keyword dictionaries for 16 algorithm categories
- Creating robust error handling and file encoding support
- Building example files for testing
- Setting up project structure with `.kiro` steering rules and hooks
- Producing documentation and usage examples

**Development Time**: ~2 hours with Kiro vs estimated 8+ hours manually

## Installation

No external dependencies required! Uses only Python standard library.

```bash
# Make the script executable (optional)
chmod +x organize_code_files.py
```

## Usage

### Basic Usage

Organize files in the current directory:

```bash
python organize_code_files.py
```

### Specify Source and Output Directories

```bash
python organize_code_files.py --source ./my_code --output ./organized
```

### Dry Run (Preview Without Moving)

```bash
python organize_code_files.py --dry-run
```

### Command Line Options

- `--source DIR`: Source directory containing files to organize (default: current directory)
- `--output DIR`: Output directory for organized files (default: `organized_code`)
- `--dry-run`: Show what would be done without actually moving files

## Example

Try it with the included example files:

```bash
# Run on example files
python organize_code_files.py --source example_files --output organized_examples

# Or preview first
python organize_code_files.py --source example_files --output organized_examples --dry-run
```

## How It Works

1. **Scans** the source directory for .cpp, .py, and .java files
2. **Reads** each file's content and filename
3. **Analyzes** using regex patterns to match topic keywords
4. **Scores** each topic based on keyword frequency
5. **Classifies** file to the highest-scoring topic
6. **Organizes** by copying files into topic-based folders

## Topic Categories & Keywords

- **Arrays**: array, list, subarray, sort, merge, two-pointer, sliding window
- **Strings**: string, substring, palindrome, anagram, pattern matching
- **LinkedList**: linked list, node, head, next, cycle
- **Trees**: tree, binary tree, BST, traversal, inorder, preorder, postorder
- **Graphs**: graph, vertex, edge, DFS, BFS, dijkstra, shortest path
- **DynamicProgramming**: DP, memoization, knapsack, LCS, LIS, fibonacci
- **Recursion**: recursion, backtrack, permutation, combination
- **Sorting**: quicksort, mergesort, heapsort, bubble sort
- **Searching**: binary search, linear search, find target
- **HashTable**: hash, map, dict, set, hashmap
- **Stack**: stack, push, pop, LIFO, valid parentheses
- **Queue**: queue, deque, FIFO, enqueue, priority queue
- **Heap**: heap, heapify, kth largest/smallest
- **Math**: prime, GCD, LCM, modulo, factorial
- **BitManipulation**: bit, XOR, shift, mask, bitwise
- **Greedy**: greedy, interval, activity selection

## Example Output

```
Code File Organizer
============================================================
Source directory: /path/to/example_files
Output directory: /path/to/organized_code
Supported extensions: .cpp, .py, .java
============================================================

Found 6 coding files to organize

Organized: binary_search.cpp -> Searching/
Organized: two_sum.py -> Arrays/
Organized: TreeTraversal.java -> Trees/
Organized: dijkstra_graph.py -> Graphs/
Organized: knapsack_dp.cpp -> DynamicProgramming/
Organized: palindrome_string.java -> Strings/

============================================================
ORGANIZATION SUMMARY
============================================================
Total files organized: 6

Arrays: 1 file(s)
  - two_sum.py
DynamicProgramming: 1 file(s)
  - knapsack_dp.cpp
Graphs: 1 file(s)
  - dijkstra_graph.py
Searching: 1 file(s)
  - binary_search.cpp
Strings: 1 file(s)
  - palindrome_string.java
Trees: 1 file(s)
  - TreeTraversal.java
============================================================
```

## Customization

To add or modify topic categories, edit the `TOPIC_KEYWORDS` dictionary in the `CodeOrganizer` class:

```python
TOPIC_KEYWORDS = {
    'YourTopic': [
        r'\bkeyword1\b',
        r'\bkeyword2\b',
        # Add more regex patterns
    ]
}
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add support for more programming languages
- Improve classification accuracy
- Add new topic categories
- Enhance the keyword patterns

## 📝 Blog Post

Read the full story of how this project was built on [AWS Builder Center](https://community.aws/builderacademy) (link coming soon).

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as part of AI for Bharat Week 2: Lazy Automation Challenge
- Developed with Kiro AI assistance
- Inspired by the pain of organizing 200+ messy coding files

## 📧 Contact

Have questions or suggestions? Feel free to open an issue or reach out!

---

**⭐ If this tool saved you time, please star the repository!**
