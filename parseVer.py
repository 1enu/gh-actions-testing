import sys
import json
import subprocess
import re

data = json.load(sys.argv[1])
bump = data["bump"]
version = data["currentVersion"]
result = subprocess.run(
    ['bumpver', 'test', f"--{bump}", version, "MAJOR.MINOR.PATCH"],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)

new_version = re.match("[0-9.]+", result.stdout)

out = subprocess.run(
['bumpver', 'update', "--set-version", new_version, "MAJOR.MINOR.PATCH"])