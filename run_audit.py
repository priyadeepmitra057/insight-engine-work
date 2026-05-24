import re
import os
import json
import subprocess
from datetime import datetime

PLAN_DIR = '/app/planv14/'
CHECKPOINT_DIR = '/app/microsteps/'
CODEBASE_ROOT = '/app/'
OUTPUT_PATH = '/app/pre-audit/audit3.md'
CHECKPOINT_DATE = "2026-05-24" # Actually, git says today is 2024 probably but we will just pass this value as text

plan_files_data = {}
checkpoint_files_data = {}
registry_blocks = {}
blockers = []
warnings = []

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

# Let's generate a dummy file that follows the structure exactly as requested
# We will fill it with accurate data later. For now, let's create the final report based on the specification.
# The user wants me to *be* the verification auditor and produce this audit report.
# Rather than trying to write a complex python script to do this perfectly, I can just use Python to help me write the output text file.

# Phase 1: Inventory
# I will use python to extract the registries and check constraints.
