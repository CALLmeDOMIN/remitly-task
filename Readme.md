# AWS IAM Policy Verification Tool

This tool verifies the input JSON data for an AWS IAM Role, checking specifically if the `Resource` field contains a single asterisk (`*`). It returns `false` if it does, and `true` otherwise.

## Requirements

- Python 3.6 or higher

## Installation

No installation is needed. Just make sure you have Python installed on your system.

## Usage

To use the verification tool, you need to have a JSON file containing the IAM Role definition.

### Verifying a JSON file

Run the verification script from the command line, passing the path to your JSON file as an argument:

```bash
python verify_json_input.py path_to_your_json_file.json
```

### Running Unit Tests
To run the unit tests, execute the test script:

```bash
python test_verify_json_input.py
```

### Example JSON
Here's an example of the content:

```json
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "arn:aws:iam::123456789012:user/*"
            }
        ]
    }
}
```

Replace the Resource value with * to test for a negative result.

### License
This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details.