import unittest

from program import Main

Main.function_01(Main.variable_01, Main.variable_02)
Main.function_02(Main.variable_01, Main.variable_02)

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_increment_one_1(self): 
        self.assertEqual( Main.function_01(1,2), "1 2")
  
    def test_increment_one_2(self):
        self.assertEqual( Main.function_02("three","four"), "three\nfour")

if __name__ == '__main__':
	unittest.main()

	
