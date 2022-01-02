import unittest

class TestCalifornia(unittest.TestCase):

    def test_california_zip_codes(self):
        """All objects in entities.zip_codes.california are a list of int with at least 1 element"""
        from burnday.entities.zip_codes import california


        county_zip_code_list_names = [
            county_zip_codes for county_zip_codes in dir(california) 
            if not county_zip_codes.startswith("_")
        ]

        for county_zip_code_name in county_zip_code_list_names:
            zip_code_import_list = getattr(california, county_zip_code_name)

            self.assertEqual(type(zip_code_import_list), list)
            self.assertGreater(len(zip_code_import_list), 0)

            [self.assertEqual(type(individual_zip), int) for individual_zip in zip_code_import_list]

