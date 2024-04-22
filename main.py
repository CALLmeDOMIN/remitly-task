import json
import sys

def verify_json_input(file_path, silent=False):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if data.get('Version') != '2012-10-17':
            return False

        statements = data.get('Statement')
        if not statements or not isinstance(statements, list):
            return False

        for statement in statements:
            if 'Effect' not in statement or statement['Effect'] not in ['Allow', 'Deny']:
                return False
            if 'Action' not in statement or (not isinstance(statement['Action'], list) and not isinstance(statement['Action'], str)):
                return False
            if 'Resource' not in statement:
                return False

            resource = statement['Resource']
            if resource == '*' or (isinstance(resource, list) and '*' in resource):
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
