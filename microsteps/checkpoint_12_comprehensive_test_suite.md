# CHECKPOINT 12: Comprehensive Test Suite
Directly modified:   tests/test_passion_engine.py
Indirectly affected: Validation
Code blocks used:    CB-P7-05, CB-P8-01
Risk:                LOW
Depends on:          CHECKPOINT 11

---
EXECUTOR DIRECTIVE
Follow each step exactly as written.
Do not reformat or alter any code block.
---

CONTEXT
Deploying the complete 174-test suite for the passion detection engine.

PRE-CONDITIONS
[ ] Checkpoint 11 passed.
[ ] passion_plan_part7.md and passion_plan_part8.md are available locally.
[ ] CB-P7-05 and CB-P8-01 are extracted exactly.
[ ] tests/test_passion_engine.py does not contain placeholder text like <verbatim code from ...>.

STEPS

  STEP [12.1]
  File:           tests/test_passion_engine.py
  Action:         CREATE
  Source file:    passion_plan_part7.md, passion_plan_part8.md
  Source section: 20. tests/test_passion_engine.py (first half), 21. tests/test_passion_engine.py (second half)
  Block ID:       CB-P7-05, CB-P8-01
  Flags:          NONE

  Instruction:
  Create tests/test_passion_engine.py by concatenating the actual extracted Python code from CB-P7-05 and CB-P8-01.
  Add seam marker comments around each extracted section.
  Do not paste placeholder text.
  Do not paste angle-bracket scaffold text.
  If CB-P7-05 or CB-P8-01 cannot be extracted exactly from the source plan files, STOP.

  Required final structure:
  ```python
  # BEGIN_CB_P7_05
  # actual extracted Python code from CB-P7-05 goes here
  # END_CB_P7_05

  # BEGIN_CB_P8_01
  # actual extracted Python code from CB-P8-01 goes here
  # END_CB_P8_01
  ```

  Validation:
  [ ] grep -n "<verbatim code from" tests/test_passion_engine.py returns no matches.
  [ ] grep -n "actual extracted Python code" tests/test_passion_engine.py returns no matches.
  [ ] python3 -m py_compile tests/test_passion_engine.py succeeds.
  [ ] pytest --collect-only tests/test_passion_engine.py succeeds.
  [ ] pytest tests/test_passion_engine.py passes all tests.

  Rollback:
  Delete tests/test_passion_engine.py if newly created.
  If replacing an existing file, restore the previous version.

POST-EXECUTION VALIDATION
[ ] `grep -n "BEGIN_CB_P7_05" tests/test_passion_engine.py`
[ ] `grep -n "BEGIN_CB_P8_01" tests/test_passion_engine.py`
[ ] `python3 -m py_compile tests/test_passion_engine.py` succeeds.
[ ] `pytest --collect-only tests/test_passion_engine.py` succeeds.
[ ] `tests/test_passion_engine.py` exists and is a valid python file.
[ ] `pytest tests/test_passion_engine.py` passes all tests.

GO / NO-GO
All checks pass → proceed to FINAL INTEGRATION GATE
