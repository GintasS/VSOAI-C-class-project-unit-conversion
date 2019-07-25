import os
import unittest

from VSOAI_c_project.ConvertClass import Convert

# Basic unit tests.


class Test_convert(unittest.TestCase):
    # Temporary structure for testing.
    all_units = {
        "length": {
            "name": "metre", "symbol": "m", "units":
            [
                {"desc": "a", "unit": "metre", "value": "1"},
                {"desc": "a", "unit": "kilometre", "value": "1000"}
            ]
        }
    }

    # Test 1 - simple conversion from 1 km to m.Should yeald 1000 metres.
    def test_length_kilometre_to_metre(self):
        result = Convert.convert_unit(
            self.all_units, "length", "kilometre", "metre", 1.0)
        self.assertEqual(result, 1000.0)

    # Test 2 - backwards conversion of Test 1 - metres to kilometres. should
    # yeald 0.001 m.
    def test_length_metre_to_kilometre(self):
        result = Convert.convert_unit(
            self.all_units, "length", "metre", "kilometre", 1.0)
        self.assertEqual(result, 0.001)

    # Test 3 - conversion from metre to metre, should yeald 1.
    def test_length_metre_to_metre(self):
        result = Convert.convert_unit(
            self.all_units, "length", "metre", "metre", 1.0)
        self.assertEqual(result, 1.0)

    # Test 4 - try to convert negative value, should yield error message.
    def test_length_negative_amount(self):
        result = Convert.convert_unit(
            self.all_units, "length", "metre", "metre", -1.0)
        self.assertEqual(result, "Negative amount.")

    # Test 5 - missing unit to, should yield error message.
    def test_length_invalid_unit_to(self):
        result = Convert.convert_unit(self.all_units, "length", "metre", "", 0)
        self.assertEqual(result, "Invalid data.")

    # Test 6 - missing unit from, should yield error message.
    def test_length_invalid_unit_from(self):
        result = Convert.convert_unit(
            self.all_units, "length", "", "kilometre", 0)
        self.assertEqual(result, "Invalid data.")

    # Test 7 - missing unit category, should yield error message.
    def test_length_invalid_category(self):
        result = Convert.convert_unit(
            self.all_units, "", "metre", "kilometre", 0)
        self.assertEqual(result, "Invalid data.")

    # Test 8 - invalid unit category, should yield error message.
    def test_length_missing_category(self):
        result = Convert.convert_unit(
            self.all_units, "test", "metre", "kilometre", 0)
        self.assertEqual(result, "Invalid Unit Category.")

    # Test 9 - empty main dictionary, should yield error message.
    def test_length_invalid_main_units(self):
        result = Convert.convert_unit({}, "length", "metre", "kilometre", 0)
        self.assertEqual(result, "Invalid data.")

    # Test 10 - invalid unit from, should yield error message.
    def test_length_invalid_units(self):
        result = Convert.convert_unit(
            self.all_units, "length", "test", "kilometre", 0)
        self.assertEqual(result, "Invalid Unit(s).")


if __name__ == '__main__':
    unittest.main()
