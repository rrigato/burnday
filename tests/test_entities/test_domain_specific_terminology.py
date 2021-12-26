import unittest

class TestDomainSpecificTerminology(unittest.TestCase):

    def test_domain_specific_terminology(self):
        """Domain specific technical terms are all str"""
        from burnday.entities import domain_specific_terminology

        [
            self.assertEqual(type(getattr(domain_specific_terminology, domain_terminology)), str) 
            for domain_terminology in dir(domain_specific_terminology) 
            if not domain_terminology.startswith("_")
        ]

