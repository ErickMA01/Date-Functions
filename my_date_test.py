import unittest
import my_date


class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))  # Test for is leap year
        self.assertTrue(my_date.is_leap_year(2400))
        self.assertTrue(my_date.is_leap_year(2004))
        self.assertTrue(my_date.is_leap_year(2020))
        self.assertTrue(my_date.is_leap_year(2024))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))  # Test for not leap year
        self.assertFalse(my_date.is_leap_year(1900))
        self.assertFalse(my_date.is_leap_year(1999))
        self.assertFalse(my_date.is_leap_year(2005))
        self.assertFalse(my_date.is_leap_year(2023))

    def test_ordinal_date_non_leap_year(self):
        self.assertEqual(my_date.ordinal_date(2023, 3, 14), 73)  # Test if days ==73

    def test_ordinal_date_leap_year(self):
        self.assertEqual(my_date.ordinal_date(2024, 3, 14), 74)  # Test if days == 74 because it is leap year

    def test_days_elapsed1(self):
        self.assertEqual(my_date.days_elapsed(1997, 1, 1, 1997, 2, 1), 31)  # Days in same month, same year
        self.assertEqual(my_date.days_elapsed(2012, 1, 1, 2048, 12, 31), 13514)  # Days between 2 leap years
        self.assertEqual(my_date.days_elapsed(2023, 1, 1, 2023, 12, 31), 364)  # Days in the same year
        self.assertEqual(my_date.days_elapsed(2022, 12, 31, 2023, 1, 1), 1)  # Days between non-leap years
        self.assertEqual(my_date.days_elapsed(2000, 1, 1, 2001, 1, 1), 366)  # Leap year to non-leap year

    def test_day_of_week(self):
        self.assertEqual(my_date.day_of_week(2023, 9, 29), 'Friday')  # Check day of the week
        self.assertEqual(my_date.day_of_week(1987, 2, 28), 'Saturday')  # Check day of the week for not a leap year
        self.assertEqual(my_date.day_of_week(1956, 12, 31), 'Monday')  # Check day of the week, end of year
        self.assertEqual(my_date.day_of_week(2013, 1, 1), 'Tuesday')  # Check day of the week beginning of year


def test_to_str1(self):
    self.assertEqual(my_date.to_str(2024, 8, 2), 'Friday, 02 August 2024')  # Basic test case
    self.assertEqual(my_date.to_str(2023, 9, 29), 'Friday, 29 September 2023')  # Basic test case
    self.assertEqual(my_date.to_str(1753, 1, 1), 'Monday, 01 January 1753')  # Basic test case

    self.assertEqual(my_date.to_str(1, 1, 1), 'Tuesday, 01 January 1')  # Edge case: year 1
    self.assertEqual(my_date.to_str(9999, 12, 31), 'Friday, 31 December 9999')  # Edge case:Year 9999

    self.assertEqual(my_date.to_str(2000, 2, 29), 'Tuesday, 29 February 2000')  # Leap year
    self.assertEqual(my_date.to_str(2100, 2, 29), 'Monday, 29 February 2100')  # Not a leap year

    self.assertEqual(my_date.to_str(2023, 3, 15), 'Wednesday, 15 March 2023')  # March
    self.assertEqual(my_date.to_str(2023, 12, 25), 'Monday, 25 December 2023')  # December


if __name__ == '__main__':
    unittest.main()
