import sys
import subprocess
import re

data = sys.argv[1]
bump = re.search(r"\"bump\":\"([^\"]+)\"", data).group(1)
print("Bump type = ", bump)
version = re.search(r"\"currentVersion\":\"v?([^\"]+)\"", data).group(1)
print("Current version = ", version)
result = subprocess.run(
    ["bumpver", "test", f"--{bump}", version, "MAJOR.MINOR.PATCH"],
    capture_output=True,  # Python >= 3.7 only
    text=True,  # Python >= 3.7 only
)
new_version = re.search("[0-9.]+", result.stdout).group()
print("New version = ", new_version)
out = subprocess.run(["bumpver", "update", "-n", "--set-version", new_version])
