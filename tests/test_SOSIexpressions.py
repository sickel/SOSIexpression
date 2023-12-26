import os
import unittest
import functions
from qgis.core import *

class testSOSI(unittest.TestCase):
    """ Testing 0-length vector then one vector in each quadrant and along the axis in both direction """
    
    def test_rotate_from_vector00(self):
        """ Testing 0 vector """
        field="0 0"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),0,f"trying {field}")
    
    
    def test_rotate_from_vector01(self):
        """ Testing 0 degrees """
        field="0 1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),0,f"trying {field}")
        
    def test_rotate_from_vector02(self):
        """ Testing 45 degrees """
        field="1 1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),45,f"trying {field}")
        
    def test_rotate_from_vector03(self):
        """ Testing 90 degrees """
        field="1 0"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),90,f"trying {field}")

    def test_rotate_from_vector04(self):
        """ Testing 135 degrees """
        field="1 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),135,f"trying {field}")

    def test_rotate_from_vector05(self):
        """ Testing 180 degrees """
        field="0 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),180,f"trying {field}")
                
    def test_rotate_from_vector06(self):
        """ Testing -135 degrees """
        field="-1 -1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),-135,f"trying {field}")

    def test_rotate_from_vector07(self):
        """ Testing -90 degrees """
        field="-1 0"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),-90,f"trying {field}")


    def test_rotate_from_vector07(self):
        """ Testing -45 degrees """
        field="-1 1"
        self.assertEqual(functions.rotate_from_vector.function(field,None,None),-45,f"trying {field}")
