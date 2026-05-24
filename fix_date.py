import re

with open('/pre-audit/audit3.md', 'r') as f:
    content = f.read()

# Replace any Checkpoint written date output formatting
content = re.sub(r'Checkpoint written date:.*?(\n)', r'Checkpoint written date:  24/05/2026\1', content)

with open('/pre-audit/audit3.md', 'w') as f:
    f.write(content)
