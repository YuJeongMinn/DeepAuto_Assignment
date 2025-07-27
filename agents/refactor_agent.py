# agents/refactor_agent.py

def refactor_agent(code: str) -> str:
    prompt = f"""
You are a senior software engineer.

Refactor the following Python code to improve:
- readability
- maintainability
- simplicity

Do NOT change the core functionality.

✅ Special Instruction:
If the code calculates a filtered list and it ends up empty, do NOT return an empty list. 
Instead, return a list of 0s with the same length as the input list to preserve output shape.

Provide the refactored code with a brief explanation of what was changed and why.

Code:
{code}
"""
    return prompt