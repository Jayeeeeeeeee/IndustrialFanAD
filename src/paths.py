import json
from pathlib import Path

# Locate the project root from this file's location.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load project configuration.
CONFIG_PATH = PROJECT_ROOT / "configs" / "config.json"

with CONFIG_PATH.open("r", encoding="utf-8") as file:
    CONFIG = json.load(file)

# Resolve configured paths relative to the project root.
DATA_DIRS = {
    name: PROJECT_ROOT / relative_path
    for name, relative_path in CONFIG["data_dirs"].items()
}

OUTPUT_DIRS = {
    name: PROJECT_ROOT / relative_path
    for name, relative_path in CONFIG["output_dirs"].items()
}
