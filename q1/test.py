import unittest

from program import Main
from program_2.py import Display

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_function_1(self): 
        self.assertEqual( Main.function_01(1,2), "1 2")
  
    #def test_function_2(self):
       # self.assertEqual( Main.function_02("three","four"), "three\nfour")
	
    #def test_function_3(self):
        #self.assertEqual( Main.function_02("one","four"), "one\nfour")

if __name__ == '__main__':
	unittest.main()

	
