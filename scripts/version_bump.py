# version_bump.py
import re
import os

def bump_patch():
    with open("setup.py", "r") as f:
        content = f.read()
    version = re.search(r'version="([^"]+)"', content).group(1)
    major, minor, patch = map(int, version.split("."))
    new_version = f"{major}.{minor}.{patch + 1}"
    content = content.replace(f'version="{version}"', f'version="{new_version}"')
    with open("setup.py", "w") as f:
        f.write(content)
    os.environ["VERSION"] = new_version
    print(f"Bumped to {new_version}")

if __name__ == "__main__":
    bump_patch()