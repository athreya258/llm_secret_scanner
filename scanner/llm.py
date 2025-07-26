import os
from typing import Optional

def ask_llm(context_block: str) -> str:
    """
    Ask LLM to analyze context and determine if a detected pattern is a real secret.
    Returns a fallback message if OpenAI API is unavailable.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Fallback when no API key is provided
    if not api_key:
        return "UNKNOWN - OpenAI API key not provided. Pattern detected but not verified by LLM."
    
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=api_key)
        
        prompt = f"""You are a code security assistant.
Here is a code snippet:

{context_block}

Is there a real secret (like an API key or access token) in this snippet?
Answer YES or NO and briefly explain."""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
        
    except ImportError:
        return "ERROR - OpenAI library not properly installed."
    except Exception as e:
        return f"ERROR - LLM analysis failed: {str(e)[:100]}"
