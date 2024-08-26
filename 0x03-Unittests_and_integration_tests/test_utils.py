#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map function."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected (_type_): _description_
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected_error (_type_): _description_
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_error}'")


if __name__ == '__main__':
    unittest.main()
