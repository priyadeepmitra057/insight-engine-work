# CHECKPOINT 11: Infrastructure and Test Configuration

Directly modified:   .github/workflows/deploy.yml, pyproject.toml, requirements.txt, tests/conftest.py
Indirectly affected: Deployment, Test execution
Code blocks used:    CB-P7-01, CB-P7-02, CB-P7-03, CB-P7-04
Risk:                MEDIUM
Depends on:          CHECKPOINT 10

---
EXECUTOR DIRECTIVE
You are an executor. Not a decision maker.
Follow each step exactly as written.
Do not infer. Do not improvise. Do not skip.
Do not reformat or alter any code block.
If a step is unclear → STOP and ask.
If a pre-condition fails → STOP and report.
If any validation fails → STOP. Do not continue.
Never modify files not listed in the current step.
Confirm each step complete before moving to next.
Treat every silent success as a potential silent failure until validation proves otherwise.
Never self-fix a failed test. HALT and wait for instruction.
---

CONTEXT
Updating deployment workflows, project dependencies, and test fixtures to support the passion engine.

PRE-CONDITIONS
[ ] Checkpoint 10 passed.

STEPS

  STEP [11.1]
  File:           .github/workflows/deploy.yml
  Action:         CONDITIONAL_MODIFY
  Source file:    passion_plan_part7.md
  Source section: 19. Infrastructure (deploy.yml)
  Block ID:       CB-P7-01
  Flags:          [SECURITY SENSITIVE]

  Pre-condition:
  [ ] If .github/workflows/deploy.yml does not exist, mark this step N/A and continue.
  [ ] If it exists, apply the exact replacement below.
  [ ] Do not create a new deploy workflow unless GitHub Actions deployment is intentionally used by this repository.

  Before:
  ```yaml
      - name: Validate secrets
        run: |
          if [ -z "$INSIGHT_ENGINE_SECRET" ]; then
            echo "Warning: INSIGHT_ENGINE_SECRET not set"
          fi
        env:
          INSIGHT_ENGINE_SECRET: ${{ secrets.INSIGHT_ENGINE_SECRET }}
  ```

  Instruction:
  If the file exists, replace the exact literal code block above.
  If the file exists but the exact Before block is not found exactly once, STOP.
  If the file does not exist, record:
  "deploy.yml absent; deployment secret validation N/A for this repo."

  After:
  ```yaml
      - name: Validate required secrets
        run: |
          if [ -z "$INSIGHT_ENGINE_SECRET" ]; then
            echo "CRITICAL: INSIGHT_ENGINE_SECRET is not set. Aborting."
            exit 1
          fi
          clean_secret=$(printf '%s' "$INSIGHT_ENGINE_SECRET" | tr -d '\r\n')
          byte_len=$(printf '%s' "$clean_secret" | wc -c)
          if [ "$byte_len" -lt 32 ]; then
            echo "CRITICAL: INSIGHT_ENGINE_SECRET too short (min 32 bytes)."
            exit 1
          fi
        env:
          INSIGHT_ENGINE_SECRET: ${{ secrets.INSIGHT_ENGINE_SECRET }}
  ```

  Rollback:
  If deploy.yml existed and was modified, revert .github/workflows/deploy.yml.
  If deploy.yml did not exist, no rollback action.

  Validation:
  [ ] If deploy.yml exists, YAML parses successfully.
  [ ] If deploy.yml exists, the secret validation step remains under the same steps list.
  [ ] If deploy.yml does not exist, final gate records deploy workflow secret validation as N/A, not failed.

  STEP [11.2]
  File:           pyproject.toml
  Action:         CREATE_OR_MODIFY
  Source file:    passion_plan_part7.md
  Source section: 19. Infrastructure (pyproject.toml)
  Block ID:       CB-P7-02
  Flags:          NONE

  Before:
  ```text
  FILE MAY OR MAY NOT EXIST
  ```

  Instruction:
  If `pyproject.toml` does not exist:
  - create it with this full content:
  ```toml
  [project]
  requires-python = ">=3.11"

  [tool.pytest.ini_options]
  log_cli_level = "INFO"
  filterwarnings = [
      # FIX 20: Do not globally error every UserWarning
      "error::RuntimeWarning",
      "default::DeprecationWarning",
      "default::FutureWarning",
      "default::PendingDeprecationWarning",
      "ignore::RuntimeWarning:numpy",
      "ignore::UserWarning:pandas",
  ]
  ```

  If `pyproject.toml` exists:
  - preserve all unrelated sections.
  - if `[project]` exists and `requires-python` exists, update `requires-python` to `>=3.11`.
  - if `[project]` exists and `requires-python` is absent, add `requires-python = ">=3.11"` inside `[project]`.
  - if `[project]` is absent, add:
    ```toml
    [project]
    requires-python = ">=3.11"
    ```
  - if `[tool.pytest.ini_options]` exists, replace only that block with the provided pytest block.
  - if `[tool.pytest.ini_options]` is absent, append the provided pytest block.
  - if more than one `[tool.pytest.ini_options]` block exists, STOP.

  Provided pytest block:
  ```toml
[tool.pytest.ini_options]
log_cli_level = "INFO"
filterwarnings = [
    # FIX 20: Do not globally error every UserWarning
    "error::RuntimeWarning",
    "default::DeprecationWarning",
    "default::FutureWarning",
    "default::PendingDeprecationWarning",
    "ignore::RuntimeWarning:numpy",
    "ignore::UserWarning:pandas",
]
  ```

  Rollback: Restore original pyproject.toml.

  STEP [11.3]
  File:           requirements.txt
  Action:         VERIFY_OR_MODIFY
  Source file:    passion_plan_part7.md
  Source section: 19. Infrastructure (requirements.txt)
  Block ID:       CB-P7-03
  Flags:          NONE

  Before:
  ```python
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
lightgbm>=4.0.0
scipy>=1.14.0
  ```

  Instruction:
  If requirements.txt already contains the target dependency block exactly, mark Step 11.3 complete.
  If it contains the old dependency block exactly once, replace it with the target dependency block.
  If neither old nor target dependency block is found exactly once, STOP.

  After:
  ```text
numpy>=2.0,<3
pandas>=3.0,<4
scikit-learn>=1.8,<2
lightgbm>=4.6,<5
scipy>=1.17,<2
  ```

  Rollback: Restore original requirements.txt.

  STEP [11.4]
  File:           tests/conftest.py
  Action:         CREATE_OR_MODIFY
  Source file:    passion_plan_part7.md
  Source section: 19. Infrastructure (conftest.py)
  Block ID:       CB-P7-04
  Flags:          NONE

  Before:
  ```text
  FILE MAY OR MAY NOT EXIST
  ```

  Instruction:
  If tests/conftest.py does not exist:
  - create tests/conftest.py with the full fixture content from the After block.

  If tests/conftest.py exists:
  - replace the exact literal old fixture block if found exactly once.
  - if the file exists but the exact old fixture block is not found exactly once, STOP.
  - do not merge fixtures manually.

  After:
  ```python
import os
import threading
import pytest

# FIX M1: REMOVED module-level os.environ mutations.
# Previously: os.environ.setdefault("ENV", "test")
# If CI has ENV=production already set, setdefault is a no-op.
# _ensure_initialized then rejects SKIP_STARTUP_CHECKS, breaking all tests.
# Now uses a session-scoped autouse fixture that saves/restores original values.

@pytest.fixture(autouse=True, scope="session")
def _set_test_env():
    """Force test environment for entire session, restore originals on teardown."""
    # C1: Save and forcibly set BOTH env vars. Do not rely on CI or developer
    # shell state: if ENV is already 'production', SKIP_STARTUP_CHECKS would be
    # rejected by _ensure_initialized, breaking the entire test session.
    # Setting ENV=test here overrides any ambient value for the session.
    _keys = ("INSIGHT_ENGINE_SKIP_STARTUP_CHECKS", "ENV")
    original = {k: os.environ.get(k) for k in _keys}
    os.environ["INSIGHT_ENGINE_SKIP_STARTUP_CHECKS"] = "true"
    os.environ["ENV"] = "test"

    # C1: Reset passion_pipeline init state NOW, after env vars are set.
    # Stale _init_complete from a previous session would cause _ensure_initialized
    # to skip the env-var checks entirely and use whatever state was cached.
    import sys
    if "passion_pipeline" in sys.modules:
        import passion_pipeline as _pp
        _pp._init_complete.clear()
        _pp._init_failed.clear()

    yield
    for k, v in original.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


# P1.8 + P2.8: Reset threading.Event for _init_complete between tests.
# FIX M2: Also reset _init_lock. If a test crashes while holding the lock,
# subsequent tests would deadlock without this reset.
# FIX-10: Also reset _init_failed event.
# FIX 5: Reset _init_in_progress to False to prevent thread state contamination.
@pytest.fixture(autouse=True)
def _reset_pipeline_initialized(monkeypatch):
    import sys
    if "passion_pipeline" in sys.modules:
        monkeypatch.setattr("passion_pipeline._init_complete", threading.Event())
        monkeypatch.setattr("passion_pipeline._init_lock", threading.Lock())
        monkeypatch.setattr("passion_pipeline._init_failed", threading.Event())
        monkeypatch.setattr("passion_pipeline._init_in_progress", False)
    yield


# FIX L5 + FIX-T1-01: _secret_cache reset between tests.
@pytest.fixture(autouse=True)
def _reset_dev_secret():
    from log_utils import _reset_secret_cache
    _reset_secret_cache()
    yield

@pytest.fixture
def real_startup_env(monkeypatch):
    monkeypatch.setenv("ENV", "test")
    monkeypatch.delenv("INSIGHT_ENGINE_SKIP_STARTUP_CHECKS", raising=False)
    from log_utils import _reset_secret_cache
    _reset_secret_cache()
    import passion_pipeline
    monkeypatch.setattr(passion_pipeline, "_init_complete", threading.Event())
    monkeypatch.setattr(passion_pipeline, "_init_failed", threading.Event())
    monkeypatch.setattr(passion_pipeline, "_init_lock", threading.Lock())
    monkeypatch.setattr(passion_pipeline, "_init_in_progress", False)
    yield
  ```

  Rollback:
  If file was newly created, delete tests/conftest.py.
  If file existed, restore original tests/conftest.py.

  Validation:
  [ ] tests/conftest.py exists.
  [ ] python3 -m py_compile tests/conftest.py succeeds.
  [ ] pytest --version succeeds.
  [ ] pytest --collect-only succeeds after CP12.

POST-EXECUTION VALIDATION
[ ] If deploy.yml exists, deploy.yml parses as valid YAML.
[ ] If deploy.yml exists, the secret validation step remains under the same steps list as the original block.
[ ] If deploy.yml exists, the step exits non-zero when INSIGHT_ENGINE_SECRET is empty.
[ ] If deploy.yml exists, the step exits non-zero when INSIGHT_ENGINE_SECRET is shorter than 32 bytes.
[ ] If deploy.yml does not exist, deploy workflow validation is recorded as N/A.
[ ] python3 -c "import tomllib; tomllib.load(open('pyproject.toml','rb'))" succeeds.
[ ] pyproject.toml contains requires-python = ">=3.11".
[ ] pyproject.toml contains exactly one [tool.pytest.ini_options] block.
[ ] pyproject.toml does not contain "error::UserWarning".
[ ] `requirements.txt` updated.
[ ] `tests/conftest.py` includes `_set_test_env`.
[ ] `pytest --version` works.

GO / NO-GO
All checks pass → proceed to CHECKPOINT [12]
