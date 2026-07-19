import json
import sys


def main():
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input") or {}
    tool_response = data.get("tool_response") or {}
    file_path = (
        tool_response.get("filePath")
        or tool_input.get("file_path")
        or tool_input.get("notebook_path")
        or ""
    )
    if not file_path.endswith(".ipynb"):
        return
    try:
        with open(file_path, encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        print(json.dumps({
            "decision": "block",
            "reason": f"Invalid notebook JSON in {file_path}: {e}",
        }))


if __name__ == "__main__":
    main()
