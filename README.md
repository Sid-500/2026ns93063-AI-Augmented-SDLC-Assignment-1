# AI-Augmented SDLC & Harness Engineering

This repository implements **Specification-Driven Development (SDD)** and automated **Harness Engineering** for BITS Pilani (SE ZG534) Assignment 1. It features a deterministic CLI application and a non-deterministic AI agent evaluated via automated verification pipelines.

---

## 📁 Repository Layout

```text
Assignment-1/
├── Part-1A/                  # Deterministic Task CLI
│   ├── speckit.*.md          # Spec Kit Artifacts (Constitution, Spec, Plan, Tasks)
│   ├── src/todo.py           # Core Application Logic
│   ├── tests/test_todo.py    # Unit & Contract Assertions
│   ├── .harness/run_harness.py # Multi-Gate Runner (Ruff, Bandit, Pytest)
│   └── evidence/             # Harness Execution Logs
└── Part-1B/                  # Non-Deterministic Natural-Language Reminder Agent
    ├── speckit.*.md          # Spec Kit Artifacts (Contract, Invariants, Thresholds)
    ├── src/agent.py          # AI Parsing Agent
    ├── evals/dataset.json    # 15-Case Benchmark Evaluation Dataset
    ├── .harness/eval_runner.py # 3-Layer Evaluation Pipeline
    └── evidence/             # Evaluation Results & Audit Log
```

---

## ⚡ Quick Start & Verification

### Prerequisites
```bash
pip install pytest ruff bandit
```

### Run Harness Verification

```bash
# Part 1A: Deterministic Harness (Linting, Security SAST, Unit Tests)
python Part-1A/.harness/run_harness.py

# Part 1B: 3-Layer Non-Deterministic Evaluation Pipeline
python Part-1B/.harness/eval_runner.py
```

---

## 📊 Harness Results Summary

| Component | Architecture | Gates / Layers | Target | Status |
| :--- | :--- | :--- | :---: | :---: |
| **Part 1A** | Deterministic CLI | Syntax (`Ruff`), Security (`Bandit`), Tests (`Pytest`) | Pass all gates | **PASS** |`
| **Part 1B** | AI Reminder Agent | Layer 1 Schema, Layer 2 Invariants, Layer 3 Quality | ≥ 85.0% | **100.0% PASS** |
