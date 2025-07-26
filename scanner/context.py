# scanner/context.py (CORRECT)
import os
from typing import Optional

def extract_context(lines, lineno, context_size=3):
    """
    Extract context around a line for LLM analysis.
    
    Args:
        lines: List of file lines
        lineno: Line number (1-indexed)
        context_size: Number of lines before/after to include
    
    Returns:
        String with context lines
    """
    # Convert to 0-indexed for array access
    line_idx = lineno - 1
    
    # Calculate context window
    start = max(0, line_idx - context_size)
    end = min(len(lines), line_idx + context_size + 1)
    
    # Extract context lines with line numbers for clarity
    context_lines = []
    for i in range(start, end):
        marker = ">>> " if i == line_idx else "    "
        context_lines.append(f"{marker}{i+1:3d}: {lines[i].rstrip()}")
    
    return "\n".join(context_lines)
