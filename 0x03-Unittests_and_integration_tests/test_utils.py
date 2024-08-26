#!/usr/bin/env python3
"""Unit tests for utils.get_json function."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """_summary_

        Args:
            test_url (_type_): _description_
            test_payload (_type_): _description_
            mock_get (_type_): _description_
        """
        # Configure the mock to return a response with .json() method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Check that requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Check that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
