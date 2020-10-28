import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables_exist(self) :
       self.assertTrue( "L" in globals(), "no variable called L has been defined" )
       self.assertTrue( "U" in globals(), "no variable called U has been defined" )
       
   def test_variables_correct(self) : 
      myx = np.loadtxt("data.dat")
      myl, myu = min(myx), max(myx)
      self.assertTrue( np.abs(myl - L)<1e-7, "the variable called L has not been set correctly" )
      self.assertTrue( np.abs(myu - U)<1e-7, "the variable called U has not been set correctly" )
    
