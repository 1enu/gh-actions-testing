import sys
import subprocess
import re

data = sys.argv[1]
bump = re.search(r"\"bump\":\"([^\"]+)\"", data).group(1)
version = re.search(r"\"currentVersion\":\"([^\"]+)\"", data).group(1)
result = subprocess.run(
    ['bumpver', 'test', f"--{bump}", version, "MAJOR.MINOR.PATCH"],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)

new_version = re.search("[0-9.]+", result.stdout)

out = subprocess.run(
['bumpver', 'update', "--set-version", new_version, "MAJOR.MINOR.PATCH"])