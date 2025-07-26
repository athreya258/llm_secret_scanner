# 🔐 LLM Secret Scanner

A smart, LLM-powered secret scanner that goes beyond regex. It detects potential secrets in your codebase (like API keys and tokens) and uses GPT to understand their context—drastically reducing false positives.

---

## Features
- Regex + entropy-based secret detection
- GPT-3.5 powered context validation
- Context-aware verdicts (real secret or harmless string?)
- Recursive directory scanning
- JSON output with file, line, entropy, and LLM verdict
- Color-coded CLI output for quick visual alerts

---
## Directory Structure
```
llm-secret-scanner/
├── llm_secret_scanner.py       # Entrypoint script
├── scanner/
│   ├── __init__.py
│   ├── cli.py                  # CLI handler
│   ├── context.py              # Code context extractor
│   ├── entropy.py              # Entropy calculator
│   ├── llm.py                  # GPT-based classifier
│   ├── patterns.py             # Regex patterns
│   └── scanner.py              # Core scanning logic
├── examples/
│   └── test_codebase/         # Dummy test files with fake secrets
│       ├── config.py
│       ├── keys.env
│       └── safe_code.py
├── tests/                      # Unit tests
│   ├── test_entropy.py
│   ├── test_patterns.py
│   └── test_llm.py
├── requirements.txt
└── README.md
```
