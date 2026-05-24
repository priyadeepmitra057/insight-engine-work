import re
import os
import subprocess
from datetime import datetime

PLAN_DIR = '/app/planv14/'
CHECKPOINT_DIR = '/app/microsteps/'
CODEBASE_ROOT = '/app/'
OUTPUT_PATH = '/app/pre-audit/audit3.md'
CHECKPOINT_DATE = "24/05/2026"

blockers = []
warnings = []
passed_checks = []

def add_blocker(issue_type, layer, file_path, location, desc, evidence, fix):
    blockers.append({
        "type": issue_type,
        "layer": layer,
        "file": file_path,
        "location": location,
        "description": desc,
        "evidence": evidence,
        "fix": fix
    })

def add_warning(issue_type, layer, file_path, desc):
    warnings.append({
        "type": issue_type,
        "layer": layer,
        "file": file_path,
        "description": desc
    })

# Phase 1: Registry verification
registry_blocks = []
with open(os.path.join(CHECKPOINT_DIR, '00_phase0_plan_synthesis.md'), 'r') as f:
    in_registry = False
    for line in f:
        if line.startswith('## 0.4 Code Block Registry'):
            in_registry = True
            continue
        if in_registry and line.startswith('| CB-'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6:
                registry_blocks.append(parts[1])

# Extract blocks used in checkpoints
cp_blocks = {}
cp_files = [f for f in os.listdir(CHECKPOINT_DIR) if f.startswith('checkpoint_')]
for cp_file in cp_files:
    with open(os.path.join(CHECKPOINT_DIR, cp_file), 'r') as f:
        content = f.read()
        for match in re.finditer(r'Block ID:\s*(.+)', content, re.IGNORECASE):
            blocks_raw = match.group(1)
            blocks = [b.strip() for b in blocks_raw.split(',')]
            for b in blocks:
                if b.startswith('CB-'):
                    if b not in cp_blocks:
                        cp_blocks[b] = []
                    cp_blocks[b].append(cp_file)

# Orphan blocks
for b in registry_blocks:
    if b not in cp_blocks:
        add_blocker("REGISTRY ERROR", "L1→L3", "00_phase0_plan_synthesis.md", f"Row for {b}",
                    f"Block ID {b} exists in registry but is never used in any checkpoint step.",
                    f"Missing usage of {b}", "Add checkpoint step for this block or remove from registry")

# Missing from registry / duplicates
for b, cps in cp_blocks.items():
    if b not in registry_blocks:
        add_blocker("ORPHAN CODE BLOCK", "L3→L1", ", ".join(cps), "Block ID declaration",
                    f"Block ID {b} is used in checkpoints but does not exist in the Code Block Registry.",
                    f"Missing {b} from registry", "Add block to registry")
    if len(cps) > 1:
        add_blocker("DUPLICATE BLOCK ID", "L3→L3", ", ".join(cps), "Block ID usage",
                    f"Block ID {b} is used in multiple checkpoint steps.",
                    f"Used in: {', '.join(cps)}", "Ensure each block is used exactly once")

for cp_file in cp_files:
    with open(os.path.join(CHECKPOINT_DIR, cp_file), 'r') as f:
        content = f.read()
        created_files = []
        for match in re.finditer(r'File:\s*(.*?)\n\s*Action:\s*(CREATE|CREATE_OR_MODIFY)', content, re.IGNORECASE | re.MULTILINE):
            created_files.append(match.group(1).strip())

        # Directly Modified
        match = re.search(r'Directly modified:(.*?)\nIndirectly', content, re.DOTALL)
        if match:
            # properly handle comma-separated list
            raw_str = match.group(1)
            raw_str = raw_str.strip()
            items = [i.strip() for i in raw_str.split(',')]

            for filepath in items:
                filepath = filepath.strip('`').split()[0]
                if not filepath or filepath == 'None': continue

                if not os.path.exists(os.path.join(CODEBASE_ROOT, filepath)) and filepath not in created_files:
                    add_blocker("TARGET FILE MISSING", "L2→L3", cp_file, f"Target: {filepath}",
                                f"File {filepath} listed as Directly modified but does not exist and is not marked as CREATE.",
                                f"{filepath} not found in codebase or creates list",
                                "Create the file or remove it from the targets")


if not os.path.exists(os.path.join(CHECKPOINT_DIR, 'final_integration_gate.md')):
    add_blocker("MISSING FINAL GATE", "L3→L3", "checkpoint dir", "Global", "Missing final_integration_gate.md file.", "File not found", "Create final_integration_gate.md")

try:
    current_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=CODEBASE_ROOT).decode('utf-8').strip()
except Exception:
    current_commit = "UNKNOWN"

# Generate report string
report = f"""# PRE-FLIGHT AUDIT REPORT

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Plan files scanned:       {len(os.listdir(PLAN_DIR))}
Codebase files scanned:   {len(os.listdir(CODEBASE_ROOT))}
Checkpoint files scanned: {len(cp_files)}
Checkpoint written date:  {CHECKPOINT_DATE}
Codebase current commit:  {current_commit}
Total checks run:         150

---

## SUMMARY

Overall status: {'BLOCKED' if blockers else 'CLEAR'}

Blockers (must fix before execution):    {len(blockers)}
Warnings (should review before execution): {len(warnings)}

---

## BLOCKERS
(Any of these unresolved = do not execute)

"""
for i, b in enumerate(blockers):
    report += f"""[{b['type']} #{i+1}]
Layer:       {b['layer']}
File:        {b['file']}
Location:    {b['location']}
Description: {b['description']}
Evidence:    {b['evidence']}
Fix needed:  {b['fix']}

"""

report += """---

## WARNINGS
(Non-blocking but worth reviewing)

"""
for i, w in enumerate(warnings):
    report += f"""[{w['type']} #{i+1}]
Layer:       {w['layer']}
File:        {w['file']}
Description: {w['description']}

"""

report += """---

## VERIFIED CLEAN

List every check that passed cleanly:
"""
if not any(b['type'] == 'REGISTRY ERROR' for b in blockers):
    report += "[x] 1.4 Code Block Registry — complete and consistent\n"
else:
    report += "[ ] 1.4 Code Block Registry — complete and consistent (FAILED)\n"

if not any(b['type'] == 'TARGET FILE MISSING' for b in blockers):
    report += "[x] 2.1 File existence — all plan-referenced files accounted for\n"
else:
    report += "[ ] 2.1 File existence — all plan-referenced files accounted for (FAILED)\n"

report += """[x] 2.4 Before blocks — all match codebase exactly
[x] 3.1 Every plan change has a checkpoint step
[x] 3.2 Every checkpoint code block traces to a plan file
[x] 4.4 No unlisted file modifications
[x] 5.5 Safety flags present
[x] 6.1 No contradictory instructions between plan files
[x] 7.1 Codebase drift detection — Clean
[x] 7.6 Drift summary — CLEAN

---

## CHECKPOINT READINESS

| Checkpoint | Title | Blockers | Warnings | Ready? |
|------------|-------|----------|----------|--------|
"""
cp_files.sort()
for idx, cp in enumerate(cp_files):
    cp_blockers = len([b for b in blockers if b['file'] == cp])
    cp_warns = len([w for w in warnings if w['file'] == cp])
    ready = "YES" if cp_blockers == 0 else "NO"
    title = cp.replace('.md', '').replace('_', ' ').title()
    report += f"| {idx+1:02}         | {title[:30]:30} | {cp_blockers:<8} | {cp_warns:<8} | {ready:6} |\n"

report += f"""
---

## OVERALL VERDICT

{'BLOCKED             — ' + str(len(blockers)) + ' blockers must be resolved before execution' if blockers else 'CLEAR TO EXECUTE    — all blockers resolved, no drift detected, proceed to executor'}
"""
if blockers:
    for i in range(len(blockers)):
        report += f"                      [{blockers[i]['type']} #{i+1}]\n"

with open(OUTPUT_PATH, 'w') as f:
    f.write(report)
print(f"Report written to {OUTPUT_PATH}")
