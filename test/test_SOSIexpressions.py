import os
import unittest
import functions
from qgis.core import *

class testSOSI(unittest.TestCase):
    
    
    def test_rotate_from_vector00(self):
        field="0 0"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),90,f"trying {field}")
    
    
    def test_rotate_from_vector01(self):
        field="0 1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),90,f"trying {field}")
        
    def test_rotate_from_vector02(self):
        field="1 1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),45,f"trying {field}")
        
    def test_rotate_from_vector03(self):
        field="1 0"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),0,f"trying {field}")

    def test_rotate_from_vector04(self):
        field="1 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),135,f"trying {field}")

    def test_rotate_from_vector05(self):
        field="0 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),180,f"trying {field}")
                
    def test_rotate_from_vector06(self):
        field="-1 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),225,f"trying {field}")

    

