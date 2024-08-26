#!/usr/bin/env python3
"""Unit tests for utils.memoize decorator."""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_memoize(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        class TestClass:

            def a_method(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_obj = TestClass()
            mock_method.return_value = 42

            # Call a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Check that both calls return the correct result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Check that a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
