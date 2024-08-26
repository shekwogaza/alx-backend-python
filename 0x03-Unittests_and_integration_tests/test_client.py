#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """_summary_

        Args:
            org_name (_type_): _description_
            mock_get_json (_type_): _description_
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """_summary_
        """
        expected_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        with patch.object(GithubOrgClient, 'org', new_callable=property) as mock_org:
            mock_org.return_value = expected_payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(result, expected_payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
