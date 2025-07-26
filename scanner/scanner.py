import os
import re
import json
from colorama import Fore, Style
from .patterns import PATTERNS
from .entropy import shannon_entropy
from .context import extract_context
from .llm import ask_llm

def scan_file(filepath, results, entropy_threshold=4.5):
    """
    Scan a single file for potential secrets.
    
    Args:
        filepath: Path to file to scan
        results: List to append results to
        entropy_threshold: Minimum entropy to trigger LLM analysis
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"{Fore.YELLOW}[x] Could not read {filepath}: {e}{Style.RESET_ALL}")
        return

    for lineno, line in enumerate(lines, 1):
        for key, pattern in PATTERNS.items():
            try:
                match = re.search(pattern, line)
                if match:
                    value = match.group()
                    entropy = shannon_entropy(value)
                    
                    if entropy >= entropy_threshold:
                        print(f"{Fore.RED}[!] {key} at {filepath}:{lineno}{Style.RESET_ALL}")
                        print(f"    > {line.strip()}")
                        print(f"    > Entropy: {entropy:.2f}")
                        
                        # Extract context and get LLM verdict
                        context = extract_context(lines, lineno)
                        try:
                            verdict = ask_llm(context)
                        except Exception as e:
                            verdict = f"LLM_ERROR: {str(e)[:50]}"
                        
                        print(f"    > LLM verdict: {verdict}\n")

                        results.append({
                            "type": key,
                            "file": filepath,
                            "line": lineno,
                            "value": value,
                            "entropy": round(entropy, 2),
                            "llm_verdict": verdict,
                            "context": context
                        })
                        
            except re.error as e:
                print(f"{Fore.YELLOW}[x] Regex error in pattern '{key}': {e}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}[x] Error processing line {lineno} in {filepath}: {e}{Style.RESET_ALL}")

def walk_directory(directory):
    """
    Walk directory tree and scan relevant files for secrets.
    
    Args:
        directory: Root directory to scan
        
    Returns:
        List of detection results
    """
    results = []
    file_extensions = (
        '.py', '.js', '.ts', '.jsx', '.tsx',  # Code files
        '.env', '.environment',                # Environment files
        '.txt', '.md',                        # Text files
        '.json', '.yml', '.yaml',             # Config files
        '.xml', '.ini', '.config',            # More config files
        '.properties', '.conf',               # Properties files
        '.sh', '.bash', '.zsh',              # Shell scripts
        '.dockerfile', '.docker-compose'       # Docker files
    )
    
    scanned_count = 0
    
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(file_extensions) or file.lower() in ['dockerfile', '.env', '.gitignore']:
                    filepath = os.path.join(root, file)
                    scan_file(filepath, results)
                    scanned_count += 1
        
        print(f"{Fore.CYAN}Scanned {scanned_count} files{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[!] Error walking directory {directory}: {e}{Style.RESET_ALL}")
    
    return results
