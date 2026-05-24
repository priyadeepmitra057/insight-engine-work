import re
import os

PLAN_DIR = '/app/planv14/'
CHECKPOINT_DIR = '/app/microsteps/'
CODEBASE_ROOT = '/app/'

# Check file existence for Directly modified and Indirectly affected
missing_files = []
cp_files = [f for f in os.listdir(CHECKPOINT_DIR) if f.startswith('checkpoint_')]
for cp_file in cp_files:
    with open(os.path.join(CHECKPOINT_DIR, cp_file), 'r') as f:
        content = f.read()

        # Action: CREATE
        creates = re.findall(r'Action:\s*CREATE\s*(.+)', content, re.IGNORECASE)
        created_files = [c.strip() for c in creates]

        # Directly modified
        match = re.search(r'Directly modified:(.*?)(?=\n- |\n\w+)', content, re.DOTALL)
        if match:
            for line in match.group(1).split('\n'):
                line = line.strip().strip('-').strip()
                if line and not line.startswith('None'):
                    # remove trailing comments
                    filepath = line.split()[0].strip('`')
                    if not os.path.exists(os.path.join(CODEBASE_ROOT, filepath)) and filepath not in created_files:
                        if "Action: CREATE" in content and filepath in content: # simplistic check
                            pass
                        else:
                            # check actual content for Action: CREATE
                            if f"Action: CREATE" in content and filepath in content:
                                pass
                            else:
                                print(f"Missing target file {filepath} in {cp_file}")
