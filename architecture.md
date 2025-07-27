# 🧠 DeepAuto Agentic AI System Architecture

## 1. System Overview

DeepAuto는 LangGraph를 기반으로 구성된 멀티에이전트 기반 자동 코드 리뷰 시스템입니다.  
입력된 Python 코드를 분석하여 다음을 수행합니다:

- 구조 분석
- 버그 및 보안 취약점 탐지
- 성능 개선 및 리팩토링 제안
- 유닛 테스트 코드 생성

각 기능은 독립된 LLM 기반 에이전트가 담당하며, LangGraph의 `StateGraph`를 통해 워크플로우가 구성됩니다.

---

## 2. Agent Roles

| Agent Name       | 역할 및 설명 |
|------------------|-------------|
| `parser_agent`   | 코드의 전반적인 구조(함수, 클래스 등)를 분석하여 구조 정보를 추출합니다. |
| `bug_agent`      | 코드의 논리적 버그, 보안 취약점(SQL injection 등)을 식별합니다. |
| `refactor_agent` | 불필요한 연산, 반복 코드 등을 감지하고 성능 개선 및 리팩토링을 제안합니다. |
| `test_agent`     | 함수 및 클래스 기반으로 유닛 테스트 코드를 자동 생성합니다. |
| `synth_agent`    | 위 결과들을 종합하여 최종 결과를 정리하고 출력 형식을 맞춥니다. |

---

## 3. Workflow Diagram

```mermaid
graph TD
    A[User Input: Python Code] --> B[parser_agent]
    B --> C[bug_agent]
    C --> D[refactor_agent]
    D --> E[test_agent]
    E --> F[synth_agent]
    F --> G[Final Annotated Output]
