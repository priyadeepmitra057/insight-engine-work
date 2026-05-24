import re
import os
import subprocess
from datetime import datetime

PLAN_DIR = '/app/planv14/'
CHECKPOINT_DIR = '/app/microsteps/'
CODEBASE_ROOT = '/app/'
OUTPUT_PATH = '/app/pre-audit/audit3.md'
CHECKPOINT_DATE = "2026-05-24" # 24/05/2026 as per prompt

# Data structures
plan_files_data = {}
codebase_files_data = {}
checkpoint_files_data = {}
registry_blocks = {}
blockers = []
warnings = []
verified_clean = []

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

def read_files():
    # 1.1 Plan files inventory
    for f in os.listdir(PLAN_DIR):
        if not f.endswith('.md'): continue
        with open(os.path.join(PLAN_DIR, f), 'r') as file:
            content = file.read()
            # rudimentary parsing for headings, code blocks
            headings = re.findall(r'^#+\s+(.*)', content, re.MULTILINE)
            code_blocks = len(re.findall(r'```', content)) // 2
            plan_files_data[f] = {
                "headings": headings,
                "code_blocks_count": code_blocks,
                "content": content
            }

    # 1.3 Checkpoint files inventory
    for f in os.listdir(CHECKPOINT_DIR):
        if not f.endswith('.md'): continue
        with open(os.path.join(CHECKPOINT_DIR, f), 'r') as file:
            content = file.read()
            checkpoint_files_data[f] = {
                "content": content
            }

read_files()
print(f"Read {len(plan_files_data)} plan files, {len(checkpoint_files_data)} checkpoint files.")
