import sys
import subprocess
import re

data = sys.argv[1]
print(data)
bump = re.search(r"\"bump\":\"([^\"]+)\"", data).group(1)
print(bump)
version = re.search(r"\"currentVersion\":\"v?([^\"]+)\"", data).group(1)
print(version)
result = subprocess.run(
    ['bumpver', 'test', f"--{bump}", version, "MAJOR.MINOR.PATCH"],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
print("STDOUT = ",result.stdout)
new_version = re.match("[0-9.]+", result.stdout).group()
print(new_version)
out = subprocess.run(
['bumpver', 'update', "--set-version", new_version, "MAJOR.MINOR.PATCH"])