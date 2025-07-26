import re
from scanner.patterns import PATTERNS

def test_aws_key_pattern():
    test_string = "AKIA1234567890TESTKEY"
    assert re.search(PATTERNS["AWS Access Key"], test_string)
