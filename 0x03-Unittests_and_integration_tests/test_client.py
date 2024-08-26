#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
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
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Unit-test GithubOrgClient._public_repos_url method."""
        expected_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(result, expected_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Unit-test GithubOrgClient.public_repos method."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"
            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            # Test that the list of repos is correct
            self.assertEqual(repos, ["repo1", "repo2"])

            # Test that the mocked property was called once
            mock_public_repos_url.assert_called_once()

            # Test that the mocked get_json was called once with the correct argument
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos")


if __name__ == '__main__':
    unittest.main()
