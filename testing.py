import unittest

from Rod_Conversions import *


class MyFirstTests(unittest.TestCase):

    def test_conversion_meter(self):
        self.assertEqual(conversion_meter(10), 50.292)

    def test_custom_num_list(self):
        self.assertEqual(len(create_list(10)), 10)
        