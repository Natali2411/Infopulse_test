import unittest
from followClass import ITEmployee

class ITEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee('Nataliia', 'Tiutiunnyk', 'QA')

    def test_names(self):
        self.assertEqual(self.emp.name, 'Nataliia')
        self.assertEqual(self.emp.surname, 'Tiutiunnyk')

