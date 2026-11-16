import json
import os
import sys

# Automatically set working directory to Part-1B folder and add to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
part_1b_dir = os.path.abspath(os.path.join(script_dir, ".."))
os.chdir(part_1b_dir)
if part_1b_dir not in sys.path:
  sys.path.insert(0, part_1b_dir)

from src.agent import parse_reminder


def run_eval():
  print("=== Running Part 1B Non-Deterministic Evaluation Pipeline ===")
  eval_path = os.path.join("evals", "dataset.json")

  with open(eval_path, "r", encoding="utf-8") as f:
    dataset = json.load(f)

  passed_count = 0
  results = []

  for item in dataset:
    output = parse_reminder(item["input"])

    # Layer 1: Schema Structural Check
    l1_pass = isinstance(output, dict) and all(
        k in output
        for k in [
            "intent",
            "title",
            "datetime",
            "requires_clarification",
            "clarification_prompt",
        ]
    )

    # Layer 2: Invariants / Property Check (Clarification logic match)
    l2_pass = output["requires_clarification"] == item["should_clarify"]

    # Layer 3: Quality / Intent Match
    l3_pass = output["intent"] == item["expected_intent"]

    case_passed = l1_pass and l2_pass and l3_pass
    if case_passed:
      passed_count += 1

    results.append({
        "case_id": item["id"],
        "input": item["input"],
        "passed": case_passed,
        "layer_scores": {
            "L1_Schema": l1_pass,
            "L2_Invariant": l2_pass,
            "L3_Quality": l3_pass,
        },
    })

  score_pct = (passed_count / len(dataset)) * 100
  overall_pass = score_pct >= 85.0

  summary = {
      "total_cases": len(dataset),
      "passed_cases": passed_count,
      "score_percentage": score_pct,
      "threshold": 85.0,
      "overall_passed": overall_pass,
      "details": results,
  }

  os.makedirs("evidence", exist_ok=True)
  with open("evidence/eval-results.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

  print(
      f"Evaluation Finished: {passed_count}/{len(dataset)} Passed ("
      f" {score_pct:.1f}% )"
  )
  print(f"Overall Pass Gate (>=85.0%): {overall_pass}")
  return overall_pass


if __name__ == "__main__":
  success = run_eval()
  sys.exit(0 if success else 1)