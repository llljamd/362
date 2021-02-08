import unittest
import cube

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(cube.volume(3), 27)

	def test2(self):
		with self.assertRaises(TypeError):
			cube.volume("word")
	
	def test3(self):
		with self.assertRaises(Exception):
			cube.volume(-3)

if __name__ == '__main__':
	unittest.main()
