import argparse
import json
from .scanner import walk_directory
from colorama import Fore, Style

def run_cli():
    parser = argparse.ArgumentParser(description="LLM-powered secret scanner")
    parser.add_argument("path", help="Path to the codebase")
    parser.add_argument("--output", default="llm_scan_results.json", help="Output JSON file name")
    args = parser.parse_args()

    print(f"{Fore.CYAN}Scanning {args.path}...{Style.RESET_ALL}")
    results = walk_directory(args.path)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"{Fore.GREEN}Scan complete. Results saved to {args.output}{Style.RESET_ALL}")
