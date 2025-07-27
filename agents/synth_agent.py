# agents/synth_agent.py

def synth_agent(results: dict) -> str:
    return f"""
# Code Review Summary

## Bugs & Security Issues
{results.get('bugs')}

## Performance Issues
{results.get('perf')}

## Refactoring Suggestions
{results.get('refactor')}

## Unit Tests
{results.get('tests')}
"""
