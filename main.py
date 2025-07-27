from dotenv import load_dotenv
import os
load_dotenv()

from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_openai import ChatOpenAI

from agents.parser_agent import parser_agent
from agents.bug_agent import bug_agent
from agents.perf_agent import perf_agent
from agents.refactor_agent import refactor_agent
from agents.testgen_agent import testgen_agent
from agents.synth_agent import synth_agent

class CodeReviewState(TypedDict):
    code: str
    structure: str
    bugs: str
    perf: str
    refactor: str
    tests: str
    summary: str

# LLM 설정
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# LangGraph 노드 래핑
def wrap_agent(agent_fn, input_key: str, output_key: str):
    def node(state: CodeReviewState) -> CodeReviewState:
        result = llm.invoke(agent_fn(state["code"]))
        state[output_key] = result.content
        return state
    return node

def synth_node(state: CodeReviewState) -> CodeReviewState:
    result = synth_agent(state)
    state["summary"] = result
    return state

# 그래프 구성
builder = StateGraph(CodeReviewState)
builder.add_node("parser", wrap_agent(parser_agent, "code", "structure"))
builder.add_node("bug", wrap_agent(bug_agent, "code", "bugs"))
builder.add_node("perf", wrap_agent(perf_agent, "code", "perf"))
builder.add_node("refactor", wrap_agent(refactor_agent, "code", "refactor"))
builder.add_node("testgen", wrap_agent(testgen_agent, "code", "tests"))
builder.add_node("synth", synth_node)

# 흐름 정의
builder.set_entry_point("parser")
builder.add_edge("parser", "bug")
builder.add_edge("bug", "perf")
builder.add_edge("perf", "refactor")
builder.add_edge("refactor", "testgen")
builder.add_edge("testgen", "synth")
builder.set_finish_point("synth")

graph = builder.compile()

if __name__ == "__main__":
    code1 = '''
def process_user_input(user_data):
    # Contains SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_data['id']}"
    
    # Contains buffer overflow risk
    buffer = [0] * 10
    for i in range(len(user_data['items'])):
        buffer[i] = user_data['items'][i]
    return query, buffer
'''

    code2 = '''
def calculate_statistics(data_list):
    # Inefficient list operations
    result = []
    for i in range(len(data_list)):
        # Repeated calculations
        mean = sum(data_list) / len(data_list)
        # Unnecessary list creation
        filtered = [x for x in data_list if x > mean]
        result.append(sum(filtered))
    return result    
'''

    code3 = '''
class UserAuthentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def validate_credentials(self):
        if len(self.password) < 8:
            return False
        if not any(c.isupper() for c in self.password):
            return False
        return True
    
    def generate_token(self):
        if self.validate_credentials():
            return f"token_{self.username}_{len(self.password)}"
        return None
'''

    code4 = '''
# Python code with embedded SQL and JavaScript
class DataProcessor:
    def process_data(self):
        # SQL stored procedure
        sql = """
        CREATE PROCEDURE calculate_metrics
        AS
        BEGIN
            SELECT AVG(value) as avg_value
            FROM metrics
            GROUP BY category;
        END;
        """
        
        # Embedded JavaScript for frontend
        js_code = """
        function updateMetrics(data) {
            data.forEach(item => {
                if(!item.value) return;
                calculations.push(item.value * 2);
            });
        }
        """
        
        return sql, js_code
'''

    code = code4
    result = graph.invoke({"code": code})
    print(result["summary"])
