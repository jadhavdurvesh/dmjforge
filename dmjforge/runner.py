import subprocess

def run_solution(path):
    try:
        result = subprocess.run(
            ["python3", path],
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout

    except Exception as e:
        return str(e)
