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
        
    def test_empty_statement_list(self):
        # Test with an empty Statement list
        with open('test_empty_statement.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": []
                }
            }, file)
        self.assertFalse(verify_json_input('test_empty_statement.json', True))

    def test_no_version(self):
        # Test with missing Version
        with open('test_no_version.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
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
        self.assertFalse(verify_json_input('test_no_version.json', True))

    def test_wrong_effect_value(self):
        # Test with wrong Effect value
        with open('test_wrong_effect.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "IamListAccess",
                            "Effect": "Maybe",
                            "Action": ["iam:ListRoles", "iam:ListUsers"],
                            "Resource": "arn:aws:iam::123456789012:user/*"
                        }
                    ]
                }
            }, file)
        self.assertFalse(verify_json_input('test_wrong_effect.json', True))

    def test_action_string_instead_of_list(self):
        # Test with Action as a string instead of a list
        with open('test_action_string.json', 'w') as file:
            json.dump({
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "IamListAccess",
                            "Effect": "Allow",
                            "Action": "iam:ListRoles",
                            "Resource": "arn:aws:iam::123456789012:user/*"
                        }
                    ]
                }
            }, file)
        self.assertTrue(verify_json_input('test_action_string.json', True))


if __name__ == '__main__':
    unittest.main()
