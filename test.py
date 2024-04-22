import unittest
import json
# Ensure this import matches your script name and function
from main import verify_json_input


class TestVerifyJsonInput(unittest.TestCase):

    def test_resource_asterisk(self):
        # Test with the Resource field containing an asterisk
        with open('test_asterisk.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "IamListAccess",
                            "Effect": "Allow",
                            "Action": ["iam:ListRoles", "iam:ListUsers"],
                            "Resource": "*"
                        }
                    ]
                }
            }, file)
        self.assertFalse(verify_json_input('test_asterisk.json', True))

    def test_resource_specific(self):
        # Test with the Resource field containing a specific ARN
        with open('test_specific.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "IamListAccess",
                            "Effect": "Allow",
                            "Action": ["iam:ListRoles", "iam:ListUsers"],
                            "Resource": "arn:aws:iam::123456789012:user/*"
                        }
                    ]
                }
            }, file)
        self.assertTrue(verify_json_input('test_specific.json', True))

    def test_invalid_json(self):
        # Test with invalid JSON data
        with open('test_invalid.json', 'w') as file:
            file.write("{ this is : 'not a valid json'}")
        self.assertFalse(verify_json_input('test_invalid.json', True))

    def test_file_not_found(self):
        # Test file not found scenario
        self.assertFalse(verify_json_input('non_existent_file.json', True))


if __name__ == '__main__':
    unittest.main()
