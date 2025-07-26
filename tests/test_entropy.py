from scanner.entropy import shannon_entropy

def test_entropy_high():
    assert shannon_entropy("AKIA1234567890TESTKEY") > 4.0

def test_entropy_low():
    assert shannon_entropy("hello") < 4.0
