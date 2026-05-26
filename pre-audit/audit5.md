# PRE-FLIGHT AUDIT REPORT

Generated: 26/05/2026 09:44:10
Plan files scanned:       8
Codebase files scanned:   30
Checkpoint files scanned: 12
Checkpoint written date:  26/05/2026
Codebase current commit:  731735516d567b4e3c422af1aa3f769e2e14a153
Total checks run:         120

---

## SUMMARY

Overall status: BLOCKED

Blockers (must fix before execution):    11
Warnings (should review before execution): 0

---

## BLOCKERS

[BEFORE BLOCK NOT FOUND #1]
Layer:       L1->L2
File:        schema.py
Location:    Col class
Description: Before block not found in schema.py.
Evidence:    Mismatch in checkpoint_01_core_schema_and_config.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #2]
Layer:       L1->L2
File:        config.py
Location:    TIP_CORPUS
Description: Before block not found in config.py.
Evidence:    Mismatch in checkpoint_01_core_schema_and_config.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #3]
Layer:       L1->L2
File:        hash_utils.py
Location:    stable_hash
Description: Before block not found in hash_utils.py.
Evidence:    Mismatch in checkpoint_04_pii_masking_migration_hmac.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #4]
Layer:       L1->L2
File:        recurring_detector.py
Location:    Imports
Description: Before block not found in recurring_detector.py.
Evidence:    Mismatch in checkpoint_04_pii_masking_migration_hmac.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #5]
Layer:       L1->L2
File:        tests/test_logging_safety.py
Location:    test_pii_redaction_coverage
Description: Before block not found in tests/test_logging_safety.py.
Evidence:    Mismatch in checkpoint_04_pii_masking_migration_hmac.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #6]
Layer:       L1->L2
File:        insight_generator.py
Location:    Imports
Description: Before block not found in insight_generator.py.
Evidence:    Mismatch in checkpoint_05_supporting_modules.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #7]
Layer:       L1->L2
File:        pipeline.py
Location:    Top of file
Description: Before block not found in pipeline.py.
Evidence:    Mismatch in checkpoint_09_passion_pipeline_orchestration.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #8]
Layer:       L1->L2
File:        pipeline.py
Location:    run_pipeline
Description: Before block not found in pipeline.py.
Evidence:    Mismatch in checkpoint_10_integration_hooks_and_crash_dumps.md
Fix needed:  Update Before block to match codebase exactly.

[BEFORE BLOCK NOT FOUND #9]
Layer:       L1->L2
File:        requirements.txt
Location:    Bottom
Description: Before block not found in requirements.txt.
Evidence:    Mismatch in checkpoint_11_infrastructure_and_test_configuration.md
Fix needed:  Update Before block to match codebase exactly.

[MISSING FILE #10]
Layer:       L1->L2
File:        .github/workflows/deploy.yml
Location:    N/A
Description: Target file missing and not marked for creation.
Evidence:    .github/workflows/deploy.yml not found.
Fix needed:  Create file or update action.

[BEFORE BLOCK NOT FOUND #11]
Layer:       L1->L2
File:        tests/test_logging_safety.py
Location:    test_pii_redaction_coverage
Description: Before block not found in tests/test_logging_safety.py.
Evidence:    Mismatch in checkpoint_04_pii_masking_migration_hmac.md
Fix needed:  Update Before block to match codebase exactly.

---

## WARNINGS

---

## VERIFIED CLEAN

[x] 1.4 Code Block Registry — complete and consistent
[ ] 2.1 File existence — all plan-referenced files accounted for
[ ] 2.2 Function and class existence — all plan-referenced targets exist
[ ] 2.3 Interface assumptions — all boundaries exist
[ ] 2.4 Before blocks — all match codebase exactly
[x] 3.1 Every plan change has a checkpoint step
[x] 3.2 Every checkpoint code block traces to a plan file
[x] 3.3 No plan code block is duplicated across checkpoints
[ ] 4.1 Directly modified files exist
[x] 4.2 Indirectly affected files exist
[x] 4.3 Test commands are valid
[x] 4.4 No unlisted file modifications
[x] 5.1 Sequential ordering
[x] 5.2 Dependency validity
[x] 5.3 Step numbering
[x] 5.4 Rollback instructions present
[x] 5.5 Safety flags present
[x] 5.6 Final integration gate exists
[x] 6.1 No contradictory instructions between plan files
[x] 6.2 No duplicate code blocks
[x] 6.3 Sequencing integrity
[x] 7.1 Git-based drift detection
[x] 7.2 Before block context drift
[x] 7.3 New file collision detection
[x] 7.4 Dependency version drift
[x] 7.5 Renamed or moved targets

---

## CHECKPOINT READINESS

| Checkpoint | Title | Blockers | Warnings | Ready? |
|------------|-------|----------|----------|--------|
| 01         | Core Schema and Config | 2        | 0        | NO     |
| 02         | PipelineResult Keyword Migration | 0        | 0        | YES    |
| 03         | Contracts and Bootstrap Setup | 0        | 0        | YES    |
| 04         | PII Masking Migration HMAC | 4        | 0        | NO     |
| 05         | Supporting Modules | 1        | 0        | NO     |
| 06         | Data Models | 0        | 0        | YES    |
| 07         | Engine Utilities | 0        | 0        | YES    |
| 08         | Passion Engine Implementation | 0        | 0        | YES    |
| 09         | Passion Pipeline Orchestration | 1        | 0        | NO     |
| 10         | Integration Hooks and Crash Dumps | 1        | 0        | NO     |
| 11         | Infrastructure and Test Configuration | 2        | 0        | NO     |
| 12         | Comprehensive Test Suite | 0        | 0        | YES    |

---

## OVERALL VERDICT

BLOCKED
                      11 blockers must be resolved before execution
                      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
