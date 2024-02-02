#!/usr/bin/python3
"""unittest using u-test python module"""

import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
	"""unit tests class"""

	def test_int(self):
		self.assertEqual(max_integer([10, 7, 3]), 10)
		self.assertEqual(max_integer([1, 4, 2]), 4)
		self.assertEqual(max_integer([3, 5, 15]), 15)


	