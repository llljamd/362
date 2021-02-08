import unittest
import average

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(average.avg([1, 2, 3, 4, 5]), 3)

	def test2(self):
		self.assertEqual(average.avg([]), "No values.")
			
	def test3(self):
		self.assertEqual(average.avg("words"), "Error, not all numbers")

if __name__ == '__main__':
	unittest.main()
