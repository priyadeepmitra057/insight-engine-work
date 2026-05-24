import sys
import os
import re

print("Running verification script...")

plan_dir = '/app/planv14/'
microsteps_dir = '/app/microsteps/'
repo_root = '/app/'

# Phase 1: Inventory
plan_files = [f for f in os.listdir(plan_dir) if f.endswith('.md')]
microstep_files = [f for f in os.listdir(microsteps_dir) if f.endswith('.md') and f.startswith('checkpoint')]
synthesis_file = os.path.join(microsteps_dir, '00_phase0_plan_synthesis.md')
gate_file = os.path.join(microsteps_dir, 'final_integration_gate.md')

print(f"Plan files: {plan_files}")
print(f"Microstep files: {microstep_files}")
