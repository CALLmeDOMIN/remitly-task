import json
import sys

def verify_json_input(file_path, silent=False):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        policy_document = data['PolicyDocument']
        for statement in policy_document['Statement']:
            if 'Resource' in statement and statement['Resource'] == '*':
                return False
        return True

    except json.JSONDecodeError:
        if not silent:
            print("Error: Invalid JSON file.")
        return False
    except FileNotFoundError:
        if not silent:
            print("Error: File not found.")
        return False
    except Exception as e:
        if not silent:
            print(f"Unexpected error: {e}")
        return False
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_json_input.py path_to_json_file")
        sys.exit(1)

    file_path = sys.argv[1]
    result = verify_json_input(file_path)
    print("Verification result:", result)
