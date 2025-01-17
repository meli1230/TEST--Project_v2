import unittest
from data.storage import TIMEZONES

class TestTimezones(unittest.TestCase):
    """
    Tests the integrity of the global `TIMEZONES` list, which contains available time zones
    for users. Verifications include:
    - The list should not be empty.
    - The list should contain only unique values.
    """

    def test_timezones_not_empty(self):
        """
        Verifies that the `TIMEZONES` list contains at least one element.
        - Ensures that there are defined time zones available for users.
        """
        self.assertTrue(len(TIMEZONES) > 0, "The TIMEZONES list should not be empty.")

    def test_timezones_are_unique(self):
        """
        Verifies that all values in the `TIMEZONES` list are unique.
        - Prevents duplication of time zones, which could lead to confusion or errors.
        """
        self.assertEqual(len(TIMEZONES), len(set(TIMEZONES)), "The TIMEZONES list should contain only unique values.")


if __name__ == "__main__":
    unittest.main()
