Confirmed blockers before execution:

Fix CB-P1-14 dangling registry entry.
Add CB-P2-00 to registry.
Fix CP09 Step 9.2 schematic Before block.
Clarify CP12 placeholder scaffold.

Conditional blockers:

Exact-before mismatches from Report 2 must be verified against the live repo.
Any exact Before block not found exactly once remains a blocker until the checkpoint is updated to match real code.

Non-blocking cleanup:

Add rollback to CP02 Step 2.1.

Rejected Report 2 blockers:

Missing deploy.yml.
CB-P1-12 / CB-P1-13 orphan claim.
CB-P6-02 / CB-P6-03 orphan claim.
CB-P7-05 / CB-P8-01 orphan claim.

Execution allowed only after:

Registry grep confirms no CB-P1-14 standalone registry row.
Registry grep confirms CB-P2-00 exists.
CP09 Step 9.2 no longer contains "# (fields defined in checkpoint 06)".
CP12 explicitly forbids literal placeholder paste.
Exact-before verification passes against the live repo.
CP02 rollback note is added or consciously accepted as a warning.
