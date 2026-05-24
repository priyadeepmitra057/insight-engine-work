# PRE-FLIGHT AUDIT REPORT

Generated: 2026-05-24 23:12:16
Plan files scanned:       8
Codebase files scanned:   41
Checkpoint files scanned: 15
Checkpoint written date:  2026-05-25
Codebase current commit:  cb0ffb18963d31a723e1aba3a6819529632444a5
Total checks run:         120

---

## SUMMARY

Overall status: BLOCKED

Blockers (must fix before execution):    13
Warnings (should review before execution): 1

---

## BLOCKERS
(Any of these unresolved = do not execute)

[MISSING FILE 1]
Layer:       L1->L2
File:        .github/workflows/deploy.yml
Location:    N/A
Description: Referenced file missing
Evidence:    File does not exist and no CREATE step
Fix needed:  Create file or add CREATE action

[BEFORE BLOCK NOT FOUND 1]
Layer:       L1->L2
File:        config.py
Location:    Step 01.2
Description: Before block mismatch
Evidence:    'TIP_CORPUS: dict[str, dict] = {\n    # ── Food ────'
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 2]
Layer:       L1->L2
File:        hash_utils.py
Location:    Step 04.2
Description: Before block mismatch
Evidence:    'import hashlib\n\ndef stable_hash(value: str) -> str'
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 3]
Layer:       L1->L2
File:        recurring_detector.py
Location:    Step 04.3
Description: Before block mismatch
Evidence:    'from hash_utils import stable_hash\nimport logging\n'
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 4]
Layer:       L1->L2
File:        tests/test_logging_safety.py
Location:    Step 04.5
Description: Before block mismatch
Evidence:    'from hash_utils import stable_hash\n# ... in test_p'
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 5]
Layer:       L1->L2
File:        pipeline.py
Location:    Step 09.2
Description: Before block mismatch
Evidence:    '@dataclass(frozen=True, kw_only=True)\nclass Pipeli'
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 6]
Layer:       L1->L2
File:        pipeline.py
Location:    Step 10.3
Description: Before block mismatch
Evidence:    '        # return result\n        return result\n    '
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 7]
Layer:       L1->L2
File:        pipeline.py
Location:    Step 10.4
Description: Before block mismatch
Evidence:    '        return PipelineResult(\n            debits='
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 8]
Layer:       L1->L2
File:        pipeline.py
Location:    Step 10.5
Description: Before block mismatch
Evidence:    '        if config.ENABLE_CRASH_DUMPS:\n            '
Fix needed:  Fix Before block to match target codebase

[BEFORE BLOCK NOT FOUND 9]
Layer:       L1->L2
File:        requirements.txt
Location:    Step 11.3
Description: Before block mismatch
Evidence:    'numpy>=1.24\npandas>=2.1\nscikit-learn>=1.3\nlightgbm'
Fix needed:  Fix Before block to match target codebase

[ORPHAN CODE BLOCK 1]
Layer:       L3->L1
File:        N/A
Location:    Step 05.3
Description: Block ID missing from registry
Evidence:    CB-P1-12, CB-P1-13
Fix needed:  Add to registry

[ORPHAN CODE BLOCK 2]
Layer:       L3->L1
File:        N/A
Location:    Step 10.2
Description: Block ID missing from registry
Evidence:    CB-P6-02, CB-P6-03
Fix needed:  Add to registry

[ORPHAN CODE BLOCK 3]
Layer:       L3->L1
File:        N/A
Location:    Step 12.1
Description: Block ID missing from registry
Evidence:    CB-P7-05, CB-P8-01
Fix needed:  Add to registry

---

## WARNINGS
(Non-blocking but worth reviewing)

[MISSING ROLLBACK 1]
Layer:       L3->L3
File:        N/A
Description: Step 02.1 lacks rollback instruction

---

## VERIFIED CLEAN
List every check that passed cleanly:

[x] 1.4 Code Block Registry — complete and consistent
[x] 3.1 Every plan change has a checkpoint step
[x] 3.3 No plan code block is duplicated across checkpoints
[x] 4.1 Directly modified files exist
[x] 4.2 Indirectly affected files exist
[x] 4.3 Test commands are valid
[x] 4.4 No unlisted file modifications
[x] 5.1 Sequential ordering
[x] 5.2 Dependency validity
[x] 5.3 Step numbering
[x] 5.5 Safety flags present
[x] 5.6 Final integration gate exists
[x] 6.1 No contradictory instructions between plan files
[x] 6.2 No duplicate code blocks
[x] 6.3 Sequencing integrity
[x] 7.1 Git-based drift detection (if git available) - no git drift
[x] 7.2 Before block context drift - no context collisions
[x] 7.3 New file collision detection
[x] 7.4 Dependency version drift
[x] 7.5 Renamed or moved targets

---

## CHECKPOINT READINESS

| Checkpoint | Title | Blockers | Warnings | Ready? |
|------------|-------|----------|----------|--------|
| 01         | Core Schema And Config | 1        | 0        | NO     |
| 02         | Pipelineresult Keyword Migration | 0        | 1        | YES    |
| 03         | Contracts And Bootstrap Setup | 0        | 0        | YES    |
| 04         | Pii Masking Migration Hmac | 3        | 0        | NO     |
| 05         | Supporting Modules | 1        | 0        | NO     |
| 06         | Data Models | 0        | 0        | YES    |
| 07         | Engine Utilities | 0        | 0        | YES    |
| 08         | Passion Engine Implementation | 0        | 0        | YES    |
| 09         | Passion Pipeline Orchestration | 1        | 0        | NO     |
| 10         | Integration Hooks And Crash Dumps | 4        | 0        | NO     |
| 11         | Infrastructure And Test Configuration | 2        | 0        | NO     |
| 12         | Comprehensive Test Suite | 1        | 0        | NO     |

---

## OVERALL VERDICT

BLOCKED             — blockers must be resolved before execution
                      MISSING FILE 1
                      BEFORE BLOCK NOT FOUND 1
                      BEFORE BLOCK NOT FOUND 2
                      BEFORE BLOCK NOT FOUND 3
                      BEFORE BLOCK NOT FOUND 4
                      BEFORE BLOCK NOT FOUND 5
                      BEFORE BLOCK NOT FOUND 6
                      BEFORE BLOCK NOT FOUND 7
                      BEFORE BLOCK NOT FOUND 8
                      BEFORE BLOCK NOT FOUND 9
                      ORPHAN CODE BLOCK 1
                      ORPHAN CODE BLOCK 2
                      ORPHAN CODE BLOCK 3