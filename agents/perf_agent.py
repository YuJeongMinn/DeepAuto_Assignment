# agents/perf_agent.py

def perf_agent(code: str) -> str:
    prompt = f"""
You are a performance optimization assistant.

Analyze the following Python code and identify any performance bottlenecks, such as:
- unnecessary loops
- redundant calculations
- inefficient data structures
- repeated operations in a loop

Suggest improvements with explanations.

Code:
{code}
"""
    return prompt  # 실제론 LLM으로 이 프롬프트 넣고 응답 받아야 함 (LangGraph에서 처리)
