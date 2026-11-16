import json
import os
import subprocess
import sys

# Set working directory to Part-1A folder
script_dir = os.path.dirname(os.path.abspath(__file__))
part_1a_dir = os.path.abspath(os.path.join(script_dir, ".."))
os.chdir(part_1a_dir)

# Set PYTHONPATH so Pytest can resolve the src module
env = os.environ.copy()
env["PYTHONPATH"] = part_1a_dir


def run_gate(name, cmd):
  res = subprocess.run(
      cmd, shell=True, capture_output=True, text=True, env=env
  )
  return {
      "gate": name,
      "passed": res.returncode == 0,
      "stdout": res.stdout,
      "stderr": res.stderr,
  }


def main():
  print("=== Running Part 1A Deterministic Harness Gates ===")
  gates = [
      run_gate("Syntax & Lint Guard (Ruff)", "python -m ruff check src/"),
      run_gate("Security SAST Guard (Bandit)", "python -m bandit -r src/"),
      run_gate("Deterministic Unit Tests (Pytest)", "python -m pytest tests/"),
  ]
  all_passed = all(g["passed"] for g in gates)
  report = {"overall_passed": all_passed, "gates": gates}
  print(json.dumps(report, indent=2))
  sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
  main()