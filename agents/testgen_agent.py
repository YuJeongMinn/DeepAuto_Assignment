# agents/testgen_agent.py

def testgen_agent(code: str) -> str:
    prompt = f"""
You are a Python testing expert.

Based on the following code, write unit tests using pytest. Cover edge cases and normal use cases.

Code:
{code}
"""
    return prompt
