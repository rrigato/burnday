from copy import deepcopy
import unittest

class TestInputValidators(unittest.TestCase):
    def test_validate_str_input(self):
        """Happy Path valid str input"""
        from burnday.entry.input_valdiators import validate_str_input

        mock_str_inputs = [
            ["A", 1], 
            ["ABCd"*50, 250], 
            ["ABCd_e76", 8]
        ]
        for mock_str_input in mock_str_inputs:
            with self.subTest(mock_str_input=mock_str_input):
                self.assertIsNone(validate_str_input(
                    str_input=mock_str_input[0],
                    max_len=mock_str_input[1]
                ))


    def test_validate_str_input_bad_input(self):
        """Unhappy Path, incorrect data type or string length"""
        from burnday.entry.input_valdiators import validate_str_input

        mock_str_inputs = [
            ["AB", 1], 
            ["ABCd"*500, 250], 
            [1.2, 10],
            [[], 10],
            [5, 10],
            [None, 10]
        ]

        for mock_str_input in mock_str_inputs:
            with self.subTest(mock_str_input=mock_str_input):
                self.assertEqual(
                    type(
                        validate_str_input(
                            str_input=mock_str_input[0],
                            max_len=mock_str_input[1]
                        )
                    ),
                    str
                )