import os
from typing import Optional

# Remove lines 1-38, keep only:
PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"[A-Za-z0-9/+=]{40}",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Slack Token": r"xox[baprs]-([0-9a-zA-Z]{10,48})",
    "GitHub Token": r"gh[pousr]_[A-Za-z0-9_]{36,251}",
    "Generic API Key": r"[A-Za-z0-9_\-]{32,45}",
    "JWT Token": r"eyJ[A-Za-z0-9_\-]*\.[A-Za-z0-9_\-]*\.[A-Za-z0-9_\-]*",
    "Private Key": r"-----BEGIN [A-Z ]+PRIVATE KEY-----"
}