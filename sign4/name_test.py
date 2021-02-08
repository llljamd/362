import unittest
import name

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(name.fullName("Alex", "Nguyen"), "Alex Nguyen")

	def test2(self):
		with self.assertRaises(Exception):
			name.fullName("word")
	
	def test3(self):
		with self.assertRaises(Exception):
			name.fullName(-3, "word")

if __name__ == '__main__':
	unittest.main()
