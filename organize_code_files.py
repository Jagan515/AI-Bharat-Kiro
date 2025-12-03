#!/usr/bin/env python3
"""
Code File Organizer
Automatically organizes coding files (.cpp, .py, .java) into topic-based folders
by analyzing file content and filenames using keyword-based classification.
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Set


class CodeOrganizer:
    """Organizes coding files into topic-based folders."""
    
    # Define keywords for each topic category
    TOPIC_KEYWORDS = {
        'Arrays': [
            r'\barray\b', r'\blist\b', r'\bsubarray\b', r'\brotate\b',
            r'\bsort\b', r'\bmerge\b', r'\bpartition\b', r'\btwo.?pointer',
            r'\bsliding.?window\b', r'\bkadane\b', r'\bmax.?sum\b'
        ],
        'Strings': [
            r'\bstring\b', r'\bsubstring\b', r'\bpalindrome\b', r'\banagram\b',
            r'\bpattern\b', r'\bmatch\b', r'\bkmp\b', r'\brabin.?karp\b',
            r'\blongest.?common\b', r'\breverse.?string\b'
        ],
        'LinkedList': [
            r'\blinked.?list\b', r'\bnode\b', r'\bhead\b', r'\bnext\b',
            r'\breverse.?list\b', r'\bcycle\b', r'\bmerge.?lists\b'
        ],
        'Trees': [
            r'\btree\b', r'\bbinary.?tree\b', r'\bbst\b', r'\btrie\b',
            r'\bleft\b.*\bright\b', r'\broot\b', r'\btraversal\b',
            r'\binorder\b', r'\bpreorder\b', r'\bpostorder\b', r'\blca\b'
        ],
        'Graphs': [
            r'\bgraph\b', r'\bvertex\b', r'\bedge\b', r'\badjacency\b',
            r'\bdfs\b', r'\bbfs\b', r'\bdijkstra\b', r'\btopological\b',
            r'\bshortest.?path\b', r'\bmst\b', r'\bkruskal\b', r'\bprim\b'
        ],
        'DynamicProgramming': [
            r'\bdp\b', r'\bdynamic.?programming\b', r'\bmemoization\b',
            r'\bknapsack\b', r'\blcs\b', r'\blis\b', r'\bfibonacci\b',
            r'\bsubsequence\b', r'\boptimal\b.*\bsubstructure\b'
        ],
        'Recursion': [
            r'\brecursion\b', r'\brecursive\b', r'\bbacktrack\b',
            r'\bpermutation\b', r'\bcombination\b', r'\bn.?queens\b'
        ],
        'Sorting': [
            r'\bquick.?sort\b', r'\bmerge.?sort\b', r'\bheap.?sort\b',
            r'\bbubble.?sort\b', r'\binsertion.?sort\b', r'\bselection.?sort\b'
        ],
        'Searching': [
            r'\bbinary.?search\b', r'\blinear.?search\b', r'\bsearch\b',
            r'\bfind\b.*\btarget\b', r'\blower.?bound\b', r'\bupper.?bound\b'
        ],
        'HashTable': [
            r'\bhash\b', r'\bmap\b', r'\bdict\b', r'\bset\b',
            r'\bhash.?map\b', r'\bhash.?set\b', r'\bhash.?table\b'
        ],
        'Stack': [
            r'\bstack\b', r'\bpush\b', r'\bpop\b', r'\blifo\b',
            r'\bvalid.?parentheses\b', r'\bbalanced\b'
        ],
        'Queue': [
            r'\bqueue\b', r'\bdeque\b', r'\bfifo\b', r'\benqueue\b',
            r'\bdequeue\b', r'\bpriority.?queue\b'
        ],
        'Heap': [
            r'\bheap\b', r'\bpriority.?queue\b', r'\bheapify\b',
            r'\bkth.?largest\b', r'\bkth.?smallest\b'
        ],
        'Math': [
            r'\bmath\b', r'\bprime\b', r'\bgcd\b', r'\blcm\b',
            r'\bmodulo\b', r'\bfactorial\b', r'\bpower\b', r'\bsieve\b'
        ],
        'BitManipulation': [
            r'\bbit\b', r'\bxor\b', r'\band\b.*\bor\b', r'\bshift\b',
            r'\bmask\b', r'\bbitwise\b', r'\bset.?bit\b', r'\bclear.?bit\b'
        ],
        'Greedy': [
            r'\bgreedy\b', r'\binterval\b', r'\bactivity.?selection\b',
            r'\bminimum.?coins\b', r'\bjob.?scheduling\b'
        ]
    }
    
    def __init__(self, source_dir: str = '.', output_dir: str = 'organized_code'):
        """
        Initialize the organizer.
        
        Args:
            source_dir: Directory containing files to organize
            output_dir: Directory where organized files will be placed
        """
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.supported_extensions = {'.cpp', '.py', '.java'}
        
    def read_file_content(self, file_path: Path) -> str:
        """Read file content with error handling."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}")
                return ""
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return ""
    
    def classify_file(self, file_path: Path) -> str:
        """
        Classify a file based on its content and filename.
        
        Args:
            file_path: Path to the file to classify
            
        Returns:
            Topic name (folder name) for the file
        """
        # Read file content
        content = self.read_file_content(file_path)
        filename = file_path.stem.lower()
        
        # Combine filename and content for analysis
        text_to_analyze = f"{filename} {content}".lower()
        
        # Score each topic based on keyword matches
        topic_scores: Dict[str, int] = {}
        
        for topic, keywords in self.TOPIC_KEYWORDS.items():
            score = 0
            for keyword_pattern in keywords:
                # Count matches for each keyword pattern
                matches = len(re.findall(keyword_pattern, text_to_analyze, re.IGNORECASE))
                score += matches
            
            if score > 0:
                topic_scores[topic] = score
        
        # Return topic with highest score, or 'Miscellaneous' if no matches
        if topic_scores:
            best_topic = max(topic_scores, key=topic_scores.get)
            return best_topic
        else:
            return 'Miscellaneous'
    
    def organize_files(self, dry_run: bool = False) -> Dict[str, List[str]]:
        """
        Organize all coding files in the source directory.
        
        Args:
            dry_run: If True, only show what would be done without moving files
            
        Returns:
            Dictionary mapping topics to lists of files
        """
        # Find all coding files
        coding_files = []
        for ext in self.supported_extensions:
            coding_files.extend(self.source_dir.glob(f'*{ext}'))
            # Also search in subdirectories (one level deep)
            coding_files.extend(self.source_dir.glob(f'*/*{ext}'))
        
        if not coding_files:
            print(f"No coding files found in {self.source_dir}")
            return {}
        
        print(f"Found {len(coding_files)} coding files to organize\n")
        
        # Classify and organize files
        organization: Dict[str, List[str]] = {}
        
        for file_path in coding_files:
            # Skip files already in the output directory
            if self.output_dir in file_path.parents:
                continue
            
            # Classify the file
            topic = self.classify_file(file_path)
            
            if topic not in organization:
                organization[topic] = []
            organization[topic].append(str(file_path))
            
            # Create topic folder if it doesn't exist
            topic_folder = self.output_dir / topic
            if not dry_run:
                topic_folder.mkdir(parents=True, exist_ok=True)
            
            # Move or copy the file
            destination = topic_folder / file_path.name
            
            if dry_run:
                print(f"[DRY RUN] Would move: {file_path} -> {destination}")
            else:
                try:
                    # Use copy instead of move to preserve originals
                    shutil.copy2(file_path, destination)
                    print(f"Organized: {file_path.name} -> {topic}/")
                except Exception as e:
                    print(f"Error moving {file_path}: {e}")
        
        return organization
    
    def print_summary(self, organization: Dict[str, List[str]]):
        """Print a summary of the organization results."""
        print("\n" + "="*60)
        print("ORGANIZATION SUMMARY")
        print("="*60)
        
        total_files = sum(len(files) for files in organization.values())
        print(f"Total files organized: {total_files}\n")
        
        for topic in sorted(organization.keys()):
            files = organization[topic]
            print(f"{topic}: {len(files)} file(s)")
            for file_path in sorted(files):
                print(f"  - {Path(file_path).name}")
        
        print("="*60)


def main():
    """Main function with example usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Organize coding files into topic-based folders'
    )
    parser.add_argument(
        '--source',
        default='.',
        help='Source directory containing files to organize (default: current directory)'
    )
    parser.add_argument(
        '--output',
        default='organized_code',
        help='Output directory for organized files (default: organized_code)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without actually moving files'
    )
    
    args = parser.parse_args()
    
    # Create organizer instance
    organizer = CodeOrganizer(source_dir=args.source, output_dir=args.output)
    
    print("Code File Organizer")
    print("="*60)
    print(f"Source directory: {organizer.source_dir.absolute()}")
    print(f"Output directory: {organizer.output_dir.absolute()}")
    print(f"Supported extensions: {', '.join(organizer.supported_extensions)}")
    print("="*60 + "\n")
    
    # Organize files
    organization = organizer.organize_files(dry_run=args.dry_run)
    
    # Print summary
    if organization:
        organizer.print_summary(organization)
        
        if args.dry_run:
            print("\nThis was a dry run. Use without --dry-run to actually organize files.")
    else:
        print("No files to organize.")


if __name__ == '__main__':
    main()
