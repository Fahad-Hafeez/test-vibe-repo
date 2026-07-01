# Khwand Demo Repo

This repository is a minimal demonstration for Khwand, an AI-powered self-healing code platform.

It contains a simple Python module with realistic but deliberate bugs, plus a pytest suite designed so all tests fail until those bugs are fixed.

Files:
- `calculator.py`: a small calculator module with six buggy functions and a `@vibe(...)` decorator storing intended behavior.
- `test_calculator.py`: pytest tests covering each function and the expected correct behavior.

The goal is to demonstrate how an AI-based repair system can read descriptions, identify subtle logic errors, and restore the intended behavior.
