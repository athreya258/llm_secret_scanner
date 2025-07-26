from scanner.llm import ask_llm

def test_mock_llm(monkeypatch):
    def mock_response(context_block):
        return "NO. This appears to be a dummy/test key."
    monkeypatch.setattr("scanner.llm.ask_llm", mock_response)

    result = ask_llm("fake context")
    assert result.startswith("NO")
