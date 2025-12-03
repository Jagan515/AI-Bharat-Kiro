#!/bin/bash

# Test script for Code File Organizer
# This script runs various tests to ensure everything works correctly

echo "=================================="
echo "Code File Organizer - Test Suite"
echo "=================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Test 1: Dry run on example files
echo "Test 1: Dry run on example files"
echo "-----------------------------------"
python3 organize_code_files.py --source example_files --output test_output --dry-run
echo ""

# Test 2: Actual organization
echo "Test 2: Actual organization"
echo "-----------------------------------"
python3 organize_code_files.py --source example_files --output test_output
echo ""

# Test 3: Verify output structure
echo "Test 3: Verify output structure"
echo "-----------------------------------"
if [ -d "test_output" ]; then
    echo "✅ Output directory created"
    echo "Folders created:"
    ls -1 test_output/
    echo ""
    echo "Total files organized:"
    find test_output -type f -name "*.cpp" -o -name "*.py" -o -name "*.java" | wc -l
else
    echo "❌ Output directory not found"
fi
echo ""

# Test 4: Check .kiro directory
echo "Test 4: Check .kiro directory"
echo "-----------------------------------"
if [ -d ".kiro" ]; then
    echo "✅ .kiro directory exists"
    echo "Contents:"
    find .kiro -type f
else
    echo "❌ .kiro directory not found"
fi
echo ""

# Cleanup
echo "Cleanup"
echo "-----------------------------------"
read -p "Remove test_output directory? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf test_output
    echo "✅ Cleaned up test_output"
fi

echo ""
echo "=================================="
echo "All tests completed!"
echo "=================================="
