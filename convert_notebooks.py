#!/usr/bin/env python3
"""
Script to convert Jupyter notebooks to Python files.
This script extracts code cells from .ipynb files and converts them to .py files,
while preserving markdown cells as comments.
"""

import json
import os
import sys
from pathlib import Path


def convert_notebook_to_py(notebook_path, output_path=None):
    """
    Convert a Jupyter notebook to a Python file.
    
    Args:
        notebook_path (str): Path to the .ipynb file
        output_path (str): Path for the output .py file (optional)
    """
    # Read the notebook file
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Error reading {notebook_path}: {e}")
        return False
    
    # Generate output path if not provided
    if output_path is None:
        output_path = notebook_path.replace('.ipynb', '.py')
    
    # Extract cells and convert to Python
    python_code = []
    
    # Add header comment
    python_code.append(f"# Converted from {os.path.basename(notebook_path)}")
    python_code.append("# Auto-generated Python file from Jupyter notebook")
    python_code.append("")
    
    cell_count = 0
    for cell in notebook.get('cells', []):
        cell_count += 1
        cell_type = cell.get('cell_type', '')
        
        if cell_type == 'markdown':
            # Convert markdown to comments
            python_code.append(f"# =============================================================================")
            python_code.append(f"# Markdown Cell {cell_count}")
            python_code.append(f"# =============================================================================")
            
            for line in cell.get('source', []):
                # Remove newline characters and add comment prefix
                line = line.rstrip('\n')
                python_code.append(f"# {line}")
            python_code.append("")
            
        elif cell_type == 'code':
            # Add code cells directly
            python_code.append(f"# Code Cell {cell_count}")
            python_code.append("# " + "="*75)
            
            # Get the source code
            source_lines = cell.get('source', [])
            if source_lines:
                for line in source_lines:
                    # Remove trailing newlines but preserve the code structure
                    python_code.append(line.rstrip('\n'))
            python_code.append("")
    
    # Write the Python file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(python_code))
        print(f"Successfully converted {notebook_path} to {output_path}")
        return True
    except Exception as e:
        print(f"Error writing {output_path}: {e}")
        return False


def main():
    """Main function to convert notebooks."""
    # Get the current directory
    current_dir = Path.cwd()
    
    # List of notebooks to convert
    notebooks = ['assignment_4.ipynb', 'assignment_5.ipynb']
    
    print("Jupyter Notebook to Python Converter")
    print("="*50)
    
    converted_count = 0
    for notebook in notebooks:
        notebook_path = current_dir / notebook
        
        if notebook_path.exists():
            print(f"\nConverting {notebook}...")
            if convert_notebook_to_py(str(notebook_path)):
                converted_count += 1
        else:
            print(f"Warning: {notebook} not found in current directory")
    
    print(f"\nConversion complete! {converted_count} notebook(s) converted successfully.")
    
    # List the created files
    print("\nGenerated Python files:")
    for notebook in notebooks:
        py_file = notebook.replace('.ipynb', '.py')
        py_path = current_dir / py_file
        if py_path.exists():
            print(f"  - {py_file}")


if __name__ == "__main__":
    main()
