#!/usr/bin/env python3
"""Unit tests for the client.GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {"org_payload": fixtures.org_payload, "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos, "apache2_repos": fixtures.apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            """_summary_

            Args:
                url (_type_): _description_

            Returns:
                _type_: _description_
            """
            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                return cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are run."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method returns the correct list of repos."""
        client = GithubOrgClient(self.org_payload['login'])
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method filters repos by license when provided."""
        client = GithubOrgClient(self.org_payload['login'])
        result = client.public_repos(license_key="apache-2.0")
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
